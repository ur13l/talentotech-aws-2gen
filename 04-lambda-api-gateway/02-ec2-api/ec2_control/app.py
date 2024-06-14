import json
import boto3
import datetime

ec2 = boto3.resource('ec2', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

# import requests
def lambda_handler(event, context):
    
    path = event.get('path', '/')

    if (path == "/"):
        instances = ec2.instances.all()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "instances": [{
                    "InstanceId": instance.id,
                    "InstanceType": instance.instance_type,
                    "Name": instance.tags[0]['Value'] if instance.tags else "N/A",
                    "State": instance.state['Name'],
                    "PublicIpAddress": instance.public_ip_address,
                    "PrivateIpAddress": instance.private_ip_address,
                } for instance in instances]
            }),
        }
    elif (path == "/instance/{id}"):
        id = event.get('pathParameters').get('id')
        instance = ec2.Instance(id)
        cloudwatch_metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': id
            },
        ],
        StartTime=datetime.datetime.now() - datetime.timedelta(days=1),
        EndTime=datetime.datetime.now(),
        Period=3600,
        Statistics=['Average'],
        Unit='Percent'
        )

        ec2_datapoints = [{
            'Timestamp':point['Timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
            'Average': point['Average']
        } for point in cloudwatch_metrics['Datapoints']]

        # Order datapoints by timestamp
        ec2_datapoints.sort(key=lambda x: x['Timestamp'])
        return {
            "statusCode": 200,
            "body": json.dumps({
                "InstanceId": instance.id,
                "InstanceType": instance.instance_type,
                "Name": instance.tags[0]['Value'] if instance.tags else "N/A",
                "State": instance.state['Name'],
                "PublicIpAddress": instance.public_ip_address,
                "PrivateIpAddress": instance.private_ip_address,
                "CPUUtilization": ec2_datapoints
            }),
        }

