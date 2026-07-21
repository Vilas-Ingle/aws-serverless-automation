# EC2 Auto Tagging using AWS Lambda and EventBridge

## Project Overview

This project automatically applies predefined tags to newly launched Amazon EC2 instances using AWS Lambda and Amazon EventBridge. Whenever a new EC2 instance is created, EventBridge captures the `RunInstances` API event from AWS CloudTrail and invokes a Lambda function, which adds the required tags to the instance.

This solution helps organizations enforce consistent resource tagging for cost allocation, governance, automation, and resource management.

---

## Architecture

```
EC2 Instance Launch
        │
        ▼
AWS CloudTrail
        │
        ▼
Amazon EventBridge
        │
        ▼
AWS Lambda
        │
        ▼
Amazon EC2
(Add Default Tags)
```

---

## Features

- Automatically tags newly launched EC2 instances.
- Event-driven architecture using Amazon EventBridge.
- AWS Lambda processes EC2 launch events.
- CloudWatch Logs for monitoring and troubleshooting.
- Automated deployment using GitHub Actions.
- Uses least-privilege IAM permissions.

---

## Project Structure

```
a-02-auto-tag-ec2/
├── lambda_function.py
├── requirements.txt
├── README.md
├── architecture.md
├── deployment-guide.md
└── screenshots/
```

---

## Technologies Used

- AWS Lambda
- Amazon EventBridge
- Amazon EC2
- AWS CloudTrail
- Amazon CloudWatch
- IAM
- Python 3.14
- Boto3
- GitHub Actions

---

## Default Tags Applied

| Key | Value |
|------|-------|
| Environment | Development |
| Owner | DevOps-Team |
| Project | AWS-Serverless-Automation |

---

## Prerequisites

- AWS Account
- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- AWS CloudTrail
- IAM
- GitHub Actions
- Python 3.14

---

## Deployment

1. Create the Lambda execution role.
2. Deploy the Lambda function.
3. Configure Amazon EventBridge to capture EC2 `RunInstances` events.
4. Grant EventBridge permission to invoke Lambda.
5. Configure GitHub Actions for automated deployment.
6. Push changes to the main branch.

---

## Testing

- Launch a new EC2 instance.
- Verify EventBridge invokes the Lambda function.
- Confirm default tags are automatically applied.
- Verify CloudWatch logs.
- Verify GitHub Actions deployment.

---

## Screenshots

- Lambda Function
- Lambda Configuration
- EventBridge Rule
- CloudWatch Logs
- EC2 Instance Tags
- GitHub Actions Workflow Success

---

## Future Improvements

- Configure tags using environment variables.
- Skip instances that already contain mandatory tags.
- Send SNS notifications after successful tagging.
- Support Auto Scaling Group instances.

---

## Author

Vilas Ingle
