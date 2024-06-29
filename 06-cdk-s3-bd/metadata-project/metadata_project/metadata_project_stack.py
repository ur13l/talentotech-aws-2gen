# Bibliotecas del CDK 
from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_rds as rds,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_secretsmanager as secretsmanager,
    aws_lambda_event_sources as lambda_event_sources,
    RemovalPolicy,  
    SecretValue,  
    Duration,
    Stack
)
import json


from constructs import Construct

class Metadata1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Bucket de S3 donde se almacenarán las imágenes del bucket
        bucket = s3.Bucket(self, 
            "TalentoTechBucket-Uriel-20240628", 
            removal_policy=RemovalPolicy.DESTROY, 
            auto_delete_objects=True
        )

        # Se obtiene y referencia a la VPC por default para no generar costos adicionales.
        vpc = ec2.Vpc.from_lookup(self, "DefaultVpc", is_default=True)

        # Base de datos de RDS - PostgreSQL
        db_credentials_parameter = ssm.StringParameter(self, "DBCredentialsParameter",
            parameter_name="rds-metadata-1-credentials",
            string_value=json.dumps({
                "username": "talento_tech_user",
                "password": "123asdZXC_"
            })
        )

        db_security_group = ec2.SecurityGroup(self, "DBSecurityGroup",
            vpc=vpc,
            description="Grupo de seguridad para la gestion de la base de datos de manera local.",
            allow_all_outbound=True
        )

        # Permitir conexiones desde la VPC
        db_security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc.vpc_cidr_block),
            connection=ec2.Port.tcp(5432),
            description="Permitir conexion a la base de datos desde la VPC."
        )

        db_security_group.add_ingress_rule(
            peer=ec2.Peer.ipv4("187.188.63.136/32"),
            connection=ec2.Port.tcp(5432),
            description="Permitir conexion a la base de datos desde una IP distinta."
        )

        database = rds.DatabaseInstance(self, "MetadataDB",
            engine = rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_16),
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_groups=[db_security_group],
            database_name="metadata_db",
            credentials=rds.Credentials.from_password(
                username="talento_tech_user",
                password=SecretValue.unsafe_plain_text("123asdZXC_")
            ),
            multi_az=False,
            allocated_storage=20,
            max_allocated_storage=20,
            allow_major_version_upgrade=False,
            auto_minor_version_upgrade=True,
            backup_retention=Duration.days(7),
            delete_automated_backups=True,
            removal_policy=RemovalPolicy.DESTROY,
            deletion_protection=False,
            publicly_accessible=True,

        )

        # Función lambda generada a partir de contenedor
        metadata_function = _lambda.DockerImageFunction(self, "StoreMetadataFunction",
                                                        function_name="StoreMetadataFunction",
                                                        environment={
                                                            "BUCKET_NAME": bucket.bucket_name,
                                                            "DB_SECRET": db_credentials_parameter.parameter_name,
                                                            "DB_HOST": database.db_instance_endpoint_address,
                                                            "DB_NAME": "metadata_db"
                                                        },
                                                        timeout=Duration.seconds(20),
                                                        code=_lambda.DockerImageCode.from_image_asset(
                                                            directory="lambda/metadata_function",
                                                        ))
        

        # Grant permissions
        bucket.grant_read_write(metadata_function)
        db_credentials_parameter.grant_read(metadata_function)
        database.grant_connect(metadata_function, "talento_tech_user")

        # S3 Event Source
        metadata_function.add_event_source(lambda_event_sources.S3EventSource(bucket,
            events=[s3.EventType.OBJECT_CREATED]
        ))
