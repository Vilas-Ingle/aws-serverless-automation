import boto3
import logging

ec2 = boto3.client("ec2")

AUTO_STOP = "Auto-Stop"
AUTO_START = "Auto-Start"

RUNNING = "running"
STOPPED = "stopped"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_instances(action, state):
    """
    Retrieve EC2 instance IDs matching the specified Action tag
    and instance state.

    Args:
        action (str): Value of the Action tag.
        state (str): Desired EC2 instance state.

    Returns:
        list: List of matching EC2 instance IDs.
    """

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Action",
                "Values": [action]
            },
            {
                "Name": "instance-state-name",
                "Values": [state]
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
    try:
        auto_stop_instances = get_instances(
            "AUTO_STOP", 
            "RUNNING"
            )

        if auto_stop_instances:
            ec2.stop_instances(InstanceIds=auto_stop_instances)
            logger.info(f"Stopped instances: {auto_stop_instances}")

        auto_start_instances = get_instances(
            "AUTO_START",
            "STOPPED"
            )

        if auto_start_instances:
            ec2.start_instances(InstanceIds=auto_start_instances)
            logger.info(f"Started instances: {auto_start_instances}")

        return {
            "statusCode": 200,
            "body": "ec2 instance management completed successfully."
        }

    except Exception:
        logger.exception("Failed to manage ec2 instances.")
        raise
