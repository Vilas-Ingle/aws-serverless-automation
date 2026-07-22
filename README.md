# AWS Serverless Automation

A collection of production-inspired AWS serverless automation projects built using AWS Lambda, EventBridge, SNS, S3, EC2, IAM, CloudWatch, and GitHub Actions.

The purpose of this repository is to demonstrate event-driven automation, Infrastructure as Code concepts, secure IAM practices, and CI/CD deployment for AWS Lambda functions.

---

## Technologies Used

- AWS Lambda
- Amazon EventBridge
- Amazon EC2
- Amazon S3
- Amazon SNS
- AWS IAM
- Amazon CloudWatch
- GitHub Actions
- Python (boto3)

---

## Projects

| Assignment | Description |
|------------|-------------|
| A-01 | EC2 Instance Start/Stop Automation |
| A-02 | Automatically Tag EC2 Instances |
| A-03 | S3 Bucket Cleanup Automation |
| A-04 | Detect Unencrypted S3 Buckets |
| A-05 | EC2 State Change Email Alerts |

---

## Repository Structure

```text
aws-serverless-automation/

├── a-01-ec2-instance-management
├── a-02-auto-tag-ec2
├── a-03-s3-bucket-cleanup
├── a-04-monitor-unencrypted-s3
├── a-05-ec2-state-change-alert
└── .github/workflows
```

---

## Features

- Event-driven serverless automation
- Secure IAM implementation
- GitHub Actions CI/CD
- CloudWatch monitoring
- Automated notifications
- Least Privilege IAM policies
- Production-style project organization

---

## CI/CD

Each project contains an independent GitHub Actions workflow that:

- Packages the Lambda function
- Deploys automatically after push to `main`
- Uses AWS CLI
- Uses GitHub Secrets
- Updates Lambda without manual deployment

---

## Skills Demonstrated

- Python Automation
- AWS Lambda
- EventBridge
- SNS
- EC2 Automation
- S3 Automation
- IAM Policies
- CloudWatch
- GitHub Actions
- Serverless Architecture
- DevOps Best Practices

---

## Author

**Vilas Ingle**

AWS | DevOps | Python | Automation
