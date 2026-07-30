import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:429965676677:dynamodb-item-change-alerts"


def lambda_handler(event, context):

    try:

        for record in event["Records"]:

            if record["eventName"] != "MODIFY":
                continue

            employee_id = record["dynamodb"]["Keys"]["EmployeeID"]["S"]

            old_department = record["dynamodb"]["OldImage"]["Department"]["S"]
            new_department = record["dynamodb"]["NewImage"]["Department"]["S"]

            # Send notification only if department changed
            if old_department == new_department:
                continue

            message = f"""
Employee Record Updated

Employee ID : {employee_id}

Department Changed

Old Department : {old_department}

New Department : {new_department}
"""

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="DynamoDB Item Updated",
                Message=message
            )

            logger.info(f"Notification sent for Employee ID: {employee_id}")

        return {
            "statusCode": 200,
            "body": "Notification processed successfully."
        }

    except Exception:
        logger.exception("Failed to process DynamoDB stream.")
        raise