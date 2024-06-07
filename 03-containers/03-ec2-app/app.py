
from flask import Flask, render_template, request, redirect, url_for
import boto3
import datetime

# boto3 set credentials from environment variables

app = Flask(__name__)
ec2 = boto3.resource('ec2', region_name='us-east-1')
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

                    

@app.route('/')
def index():
    instances = ec2.instances.all() 
    return render_template('index.html', instances=instances)

@app.route('/action', methods=['POST'])
def action():
    instance_id = request.form.get('id')
    action = request.form.get('action')
    
    instance = ec2.Instance(instance_id)
    
    if action == 'Detener':
        instance.stop()
    elif action == 'Iniciar':
        instance.start()
 
    return redirect(url_for('index'))

# Dynamic id page to show cloudwatch metrics
@app.route('/instance/<id>')
def show_metrics(id):
    instance = ec2.Instance(id)
    # Get metrics from cloudwatch
    response = cloudwatch.get_metric_statistics(
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

    datapoints = [{
        'Timestamp':point['Timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
        'Average': point['Average']
    } for point in response['Datapoints']]

    # Order datapoints by timestamp
    datapoints.sort(key=lambda x: x['Timestamp'])
    
    return render_template('metrics.html', instance=instance, cpu_metrics=datapoints)
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)