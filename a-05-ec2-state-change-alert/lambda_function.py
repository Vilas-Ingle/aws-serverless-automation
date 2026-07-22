import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:429965676677:ec2-state-change-alerts"


def lambda_handler(event, context):
    try:
        instance_id = event["detail"]["instance-id"]
        state = event["detail"]["state"]

        message = f"""
EC2 Instance State Change Detected

Instance ID : {instance_id}
New State   : {state}
"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="EC2 Instance State Change Alert",
            Message=message
        )

        logger.info(f"Notification sent for {instance_id} -> {state}")

        return {
            "statusCode": 200,
            "body": "Notification sent successfully."
        }

    except Exception:
        logger.exception("Failed to process EC2 state change.")
        raise