# Automated S3 Bucket Cleanup using AWS Lambda

## Project Overview

This project automates the cleanup of Amazon S3 objects older than a specified retention period using AWS Lambda.

The Lambda function scans the configured S3 bucket, identifies objects older than the configured retention period (30 days), and deletes them automatically. During development, the retention period was temporarily reduced to 0 days to validate the functionality before restoring it to 30 days.

---

## Architecture

```
            +----------------------+
            |   Amazon S3 Bucket   |
            +----------+-----------+
                       |
                       |
                List Objects
                       |
                       ▼
             +------------------+
             |  AWS Lambda      |
             | S3 Bucket Cleanup|
             +------------------+
                       |
          Check LastModified Date
                       |
         +-------------+-------------+
         |                           |
   Older than 30 Days         Less than 30 Days
         |                           |
 Delete Object                 Keep Object
```

---

## Features

- Automatically scans S3 bucket objects.
- Deletes objects older than the configured retention period.
- CloudWatch logging for monitoring.
- GitHub Actions CI/CD deployment.
- IAM least privilege for GitHub deployment.
- Easy configuration using retention period.

---

## Project Structure

```
a-03-s3-bucket-cleanup/
│
├── lambda_function.py
├── github-actions-policy.json
├── requirements.txt
├── README.md
├── architecture.md
└── screenshots/
```

---

## Prerequisites

- AWS Account
- Amazon S3
- AWS Lambda
- IAM
- GitHub Actions
- AWS CLI
- Python 3.14

---

## Deployment

1. Create S3 bucket.
2. Upload sample files.
3. Create Lambda execution role.
4. Deploy Lambda.
5. Configure GitHub Actions.
6. Push code to GitHub.
7. GitHub Actions automatically deploys the latest Lambda code.

---

## Testing

### Functional Testing

During testing:

- RETENTION_DAYS was temporarily configured as **0**.
- Uploaded sample files.
- Executed Lambda.
- Verified files were deleted.
- Verified CloudWatch logs.

Before submission:

- RETENTION_DAYS restored to **30**.

---

## Screenshots

- S3 bucket before cleanup
- S3 bucket after cleanup
- Lambda configuration
- Lambda source code
- Successful test execution
- CloudWatch logs
- GitHub Actions deployment

---

## Future Improvements

- Read retention period from Lambda environment variables.
- Trigger cleanup using Amazon EventBridge.
- Store deleted object information in DynamoDB.
- Add notification using Amazon SNS.

---

## Author

Vilas Ingle
