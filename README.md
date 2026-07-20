# AWS Serverless Automation

## Overview

This repository contains multiple AWS serverless automation projects developed using AWS Lambda, Amazon S3, Amazon EC2, IAM, CloudWatch, EventBridge, GitHub Actions, and Python.

The projects demonstrate infrastructure automation, monitoring, security, and continuous deployment using GitHub Actions.

---

## Projects

### 1. EC2 Instance Management

Automatically starts and stops EC2 instances based on resource tags.

### 2. EC2 Auto Tagging

Automatically applies default tags to newly launched EC2 instances using EventBridge and AWS Lambda.

### 3. S3 Bucket Cleanup

Deletes S3 objects older than the configured retention period.

### 4. Monitor Unencrypted S3 Buckets

Checks S3 bucket encryption status and logs results to CloudWatch.

---

## Technologies Used

- AWS Lambda
- Amazon EC2
- Amazon S3
- Amazon EventBridge
- IAM
- Amazon CloudWatch
- GitHub Actions
- Python 3.14
- Boto3

---

## Repository Structure

```
aws-serverless-automation/
├── a-01-ec2-instance-management
├── a-02-auto-tag-ec2
├── a-03-s3-bucket-cleanup
├── a-04-monitor-unencrypted-s3
└── .github/workflows
```

---

## CI/CD

GitHub Actions automatically deploys updated Lambda functions whenever changes are pushed to the `main` branch.

---

## Author

Vilas Ingle
