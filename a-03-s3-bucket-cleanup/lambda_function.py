import boto3
import logging
from datetime import datetime, timedelta, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

BUCKET_NAME = "vilas-s3-cleanup"


RETENTION_DAYS = 30


def delete_old_objects(bucket_name: str, retention_days: int) -> None:
    """
    Delete S3 objects older than the specified retention period.
    """

    cutoff_date = datetime.now(timezone.utc) - timedelta(days=retention_days)

    response = s3.list_objects_v2(Bucket=bucket_name)

    if "Contents" not in response:
        logger.info("Bucket is empty.")
        return

    for obj in response["Contents"]:

        key = obj["Key"]
        last_modified = obj["LastModified"]

        if last_modified < cutoff_date:

            logger.info(f"Deleting {key}")

            s3.delete_object(
                Bucket=bucket_name,
                Key=key
            )

        else:
            logger.info(f"Keeping {key}")


def lambda_handler(event, context):

    delete_old_objects(
        BUCKET_NAME,
        RETENTION_DAYS
    )

    return {
        "statusCode": 200,
        "body": "Cleanup completed successfully."
    }