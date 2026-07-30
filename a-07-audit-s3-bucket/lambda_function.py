import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:429965676677:s3-public-bucket-alerts"

def lambda_handler(event, context):

    public_buckets = []

    try:

        buckets = s3.list_buckets()["Buckets"]

        logger.info(f"found {len(buckets)} buckets.")

        for bucket in buckets:

            bucket_name = bucket["Name"]

            try:

                response = s3.get_bucket_policy_status(
                    Bucket=bucket_name
                )

                is_public = response["PolicyStatus"]["IsPublic"]

                if is_public:
                    public_buckets.append(bucket_name)

                    logger.warning(
                        f"Public bucket detected: {bucket_name}"
                    )
            except s3.exceptions.from_code("NoSuchBucketPolicy"):
                logger.info(
                    f"No bucket policy found for {bucket_name}"
                )

            except Exception as e:
                logger.error(
                    f"Error checking bucket {bucket_name}: {e}"
                )

        if public_buckets:

            message = (
                "Public S3 Buckets Detected\n\n"
                + "\n".join(public_buckets)
            )

            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="Public S3 Buckets Alert",
                Message=message
            )

            logger.info("Notification sent for public buckets.")

        else:

            logger.info("No public buckets detected.")

        return {
            "statusCode": 200,
            "body": "S3 bucket audit completed successfully."
        }

    except Exception:
        logger.exception("Failed to audit S3 buckets.")
        raise
