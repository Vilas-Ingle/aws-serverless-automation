import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

elbv2 = boto3.client("elbv2")
sns = boto3.client("sns")

TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-south-1:429965676677:targetgroup/alb-health-check-tg/75c0293133e82456"
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:429965676677:alb-health-alerts"


def lambda_handler(event, context):

    try:

        response = elbv2.describe_target_health(
            TargetGroupArn=TARGET_GROUP_ARN
        )

        unhealthy_targets = []

        for target in response["TargetHealthDescriptions"]:

            instance_id = target["Target"]["Id"]
            state = target["TargetHealth"]["State"]

            logger.info(f"{instance_id} -> {state}")

            if state != "healthy":

                reason = target["TargetHealth"].get(
                    "Reason",
                    "Unknown"
                )

                description = target["TargetHealth"].get(
                    "Description",
                    "No description"
                )

                unhealthy_targets.append(
                    {
                        "InstanceId": instance_id,
                        "State": state,
                        "Reason": reason,
                        "Description": description
                    }
                )

        if unhealthy_targets:

            message = f"""
ALB Health Check Alert

Load Balancer Monitoring Report

Target Group : alb-health-check-tg

Instance ID : {unhealthy_targets[0]['InstanceId']}

Health State : {unhealthy_targets[0]['State']}

Reason :
{unhealthy_targets[0]['Reason']}

Description :
{unhealthy_targets[0]['Description']}

Region :
ap-south-1

Action Required :
Please investigate the EC2 instance or application immediately.
"""

            for target in unhealthy_targets:
                message += (
                    f"Instance ID : {target['InstanceId']}\n"
                    f"State       : {target['State']}\n"
                    f"Reason      : {target['Reason']}\n"
                    f"Description : {target['Description']}\n\n"
                )

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="ALB Health Check Alert",
                Message=message
            )

            logger.warning("SNS notification sent.")

        else:

            logger.info("All targets are healthy.")

        return {
            "statusCode": 200,
            "body": "Health check completed."
        }

    except Exception:

        logger.exception("Failed to check target health.")
        raise