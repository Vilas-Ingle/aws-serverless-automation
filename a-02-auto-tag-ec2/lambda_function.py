import boto3
import logging

ec2 = boto3.client("ec2")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEFAULT_TAGS = [
    {
        "Key": "Environment",
        "Value": "Development"
    },
    {
        "Key": "Owner",
        "Value": "DevOps-Team"
    },
    {
        "Key": "Project",
        "Value": "AWS-Serverless-Automation"
    }
]


def apply_ec2_tags(resource_id: str, tags: list[dict]) -> None:
    """
    Apply tags to the specified EC2 resource.
    """

    ec2.create_tags(
        Resources=[resource_id],
        Tags=tags
    )

    logger.info(f"Successfully tagged resource: {resource_id}")


def lambda_handler(event, context):
    """
    Lambda handler triggered by EventBridge when an EC2 instance is launched.
    """

    try:
        items = event["detail"]["responseElements"]["instancesSet"]["items"]

        for instance in items:
            instance_id = instance["instanceId"]

            apply_ec2_tags(instance_id, DEFAULT_TAGS)

        return {
            "statusCode": 200,
            "body": "EC2 instances tagged successfully."
        }

    except Exception:
        logger.exception("Failed to tag EC2 instances.")
        raise