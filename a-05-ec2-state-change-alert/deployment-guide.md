# Deployment Guide

## Prerequisites

- AWS Account
- IAM permissions
- AWS CLI configured
- GitHub repository
- GitHub Actions secrets configured

---

## Deployment Steps

### 1. Create SNS Topic

- Create an SNS Standard Topic.
- Create an email subscription.
- Confirm the subscription.

---

### 2. Create Lambda Function

- Runtime: Python 3.14
- Upload lambda_function.py
- Configure execution role.

---

### 3. Configure IAM

Grant the Lambda execution role permission to:

- sns:Publish

Attach AWSLambdaBasicExecutionRole.

---

### 4. Create EventBridge Rule

Event Pattern

Service:

EC2

Event Type:

EC2 Instance State-change Notification

States:

- running
- stopped

Target:

Lambda Function

---

### 5. Test

Start or Stop an EC2 instance.

Expected Result:

- Lambda executes
- CloudWatch logs generated
- Email notification received

---

### 6. CI/CD

Push code to GitHub.

GitHub Actions:

- Packages Lambda
- Deploys updated code
- Reports workflow status
