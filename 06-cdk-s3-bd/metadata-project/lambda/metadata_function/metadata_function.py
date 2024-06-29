import os
import json
import boto3
import psycopg2
from urllib.parse import unquote_plus


s3 = boto3.client('s3')
ssm = boto3.client('ssm')

def handler(event, context):
    print(event)
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])

        print(f"Procesando archivo {key} de bucket {bucket_name}")

        try:
            # Obtener metadatos del objeto S3
            head_object = s3.head_object(Bucket=bucket_name, Key=key)
            metadata = {
                'name': key,
                'last_modified': head_object['LastModified'].isoformat(),
                'size': head_object['ContentLength'],
                'extension': key.split('.')[-1]
            }

            print(metadata)

            # Obtener las credenciales de la base de datos
            param = ssm.get_parameter(Name=os.environ['DB_SECRET'])
            secret = json.loads(param['Parameter']['Value'])

            print(os.environ['DB_HOST'])
            print(secret)
            print(os.environ['DB_NAME'])
            # Conectar a la base de datos
            connection = psycopg2.connect(
                dbname=os.environ.get('DB_NAME', "metadata_db"), 
                user=secret['username'],
                password=secret['password'],
                host=os.environ.get('DB_HOST', ''),
                port='5432'
            )
            cursor = connection.cursor()

            # Insertar metadatos en la base de datos
            query = """
                INSERT INTO metadata (name, last_modified, size, extension)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (metadata['name'], metadata['last_modified'], metadata['size'], metadata['extension']))
            connection.commit()
            cursor.close()
            connection.close()

            print(f"Successfully processed {key} from {bucket_name}")
        except Exception as e:
            print(f"Error processing {key} from {bucket_name}: {str(e)}")