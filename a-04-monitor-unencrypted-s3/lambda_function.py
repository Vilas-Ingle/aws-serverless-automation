import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")


def check_bucket_encryption(bucket_name: str) -> None:
    """
    Check whether the specified S3 bucket has default encryption enabled.
    """

    try:
        s3.get_bucket_encryption(Bucket=bucket_name)

        logger.info(f"Bucket '{bucket_name}' is encrypted.")

    except ClientError as e:

        error_code = e.response["Error"]["Code"]

        if error_code == "ServerSideEncryptionConfigurationNotFoundError":

            logger.warning(f"Bucket '{bucket_name}' is NOT encrypted.")

        else:
            raise


def lambda_handler(event, context):
    """
    Check encryption status for all S3 buckets.
    """

    response = s3.list_buckets()

    for bucket in response["Buckets"]:

        bucket_name = bucket["Name"]

        check_bucket_encryption(bucket_name)

    return {
        "statusCode": 200,
        "body": "S3 bucket encryption check completed."
    }