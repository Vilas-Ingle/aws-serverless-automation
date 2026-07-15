import boto3

ec2 = boto3.client("ec2")

def get_instances(action):

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Action",
                "Values": [action]
            },
            {
                "Name": "instance-state-name",
                "Values": ["running", "stopped"]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])
    return instance_ids

def lambda_handler(event, context):
    # find ec2 instance based on action tag
    auto_stop_instances = get_instances("Auto-Stop")
    if auto_stop_instances:
        ec2.stop_instances(InstanceIds=auto_stop_instances)
        print(f"Stopped instances: {auto_stop_instances}")

    auto_start_instances = get_instances("Auto-Start")
    if auto_start_instances:
        ec2.start_instances(InstanceIds=auto_start_instances)
        print(f"Started instances: {auto_start_instances}")

    return {
        "statusCode": 200,
        "body": "ec2 instance management completed successfully."
    }