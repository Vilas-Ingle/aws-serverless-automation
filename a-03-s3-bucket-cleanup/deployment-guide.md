# Deployment Guide

## Prerequisites

- AWS Account
- Amazon S3
- AWS Lambda
- IAM
- GitHub Actions

## Deployment Steps

1. Create an S3 bucket.
2. Upload sample files.
3. Create the Lambda execution role.
4. Deploy the Lambda function.
5. Configure GitHub Actions.
6. Push changes to the main branch.

## Testing

- Upload sample files.
- Execute the Lambda function.
- Verify old files are deleted.
- Review CloudWatch logs.

## Verification

- Old objects removed.
- Lambda executed successfully.
- GitHub Actions deployment succeeded.
