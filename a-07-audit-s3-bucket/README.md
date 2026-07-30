# AWS Lambda – Audit S3 Bucket Permissions and Notify for Public Buckets

## Project Overview

This project demonstrates a **serverless security automation solution** using **AWS Lambda**, **Amazon S3**, **Amazon SNS**, and **Amazon EventBridge Scheduler**.

The Lambda function periodically audits all Amazon S3 buckets in the AWS account and detects buckets that are publicly accessible through **Bucket Policies**. If any public bucket is found, the function automatically sends an email notification using Amazon SNS.

This project helps automate cloud security monitoring and demonstrates how AWS serverless services can be used to continuously audit infrastructure without managing any servers.

---

## Architecture

```
                Amazon EventBridge Scheduler
                           │
                           ▼
                     AWS Lambda Function
                           │
                           ▼
                List all Amazon S3 Buckets
                           │
                           ▼
              Check Bucket Policy Status
                           │
          ┌────────────────┴────────────────┐
          │                                 │
     Public Bucket                     Private Bucket
          │                                 │
          ▼                                 ▼
     Amazon SNS                       Ignore Bucket
          │
          ▼
      Email Notification
```

---

## AWS Services Used

- AWS Lambda
- Amazon S3
- Amazon SNS
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon CloudWatch
- Boto3 (AWS SDK for Python)

---

## Features

- Serverless architecture
- Automated daily S3 security audit
- Detects publicly accessible S3 buckets using Bucket Policy Status
- Sends email notifications through Amazon SNS
- CloudWatch logging for monitoring and troubleshooting
- Least-Privilege IAM implementation
- Scheduled execution using Amazon EventBridge Scheduler

---

## Project Structure

```
a-07-audit-s3-bucket/
│
├── README.md
├── architecture.md
├── deployment.md
├── lambda_function.py
├── requirements.txt
└── screenshots/
    ├── cloudwatch-logs.png
    ├── eventbridge-scheduler.png
    ├── lambda-config.png
    ├── lambda-function-code.png
    ├── public-bucket-policy.png
    ├── s3-bucket-list.png
    └── sns-email.png
```

---

## Workflow

1. EventBridge Scheduler triggers the Lambda function on a schedule.
2. Lambda lists all S3 buckets.
3. Lambda checks each bucket's public access status using the S3 Bucket Policy Status API.
4. Public buckets are collected.
5. If any public bucket exists:
   - An SNS notification is published.
   - Subscribers receive an email alert.
6. CloudWatch Logs capture execution details.

---

## Security Best Practices

- Implemented using Least Privilege IAM permissions.
- Uses custom IAM policy instead of managed administrator policies.
- CloudWatch logging enabled for auditing.
- Test bucket permissions should be removed after validation.

---

## Testing

The solution was validated by:

- Manual Lambda invocation
- EventBridge Scheduler execution
- CloudWatch log verification
- Amazon SNS email notification
- Public S3 bucket detection

---

## Screenshots

The repository contains screenshots demonstrating:

- S3 Bucket Configuration
- Bucket Policy
- Lambda Function
- Lambda Configuration
- EventBridge Scheduler
- CloudWatch Logs
- SNS Email Notification

---

## Learning Outcomes

- AWS Lambda Development
- Amazon S3 Security
- Bucket Policy Status API
- Amazon SNS Notifications
- EventBridge Scheduler
- IAM Roles and Policies
- CloudWatch Logging
- Serverless Security Automation
