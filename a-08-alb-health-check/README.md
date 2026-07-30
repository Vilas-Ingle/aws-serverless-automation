# Application Load Balancer Health Monitoring Using AWS Lambda, Boto3, SNS, and EventBridge

## Project Overview

This project demonstrates an automated monitoring solution for an AWS Application Load Balancer (ALB). A Lambda function periodically checks the health of EC2 instances registered in an ALB Target Group. If any target becomes unhealthy, an Amazon SNS notification is sent to administrators.

This implementation simulates a production-style monitoring workflow using AWS serverless services.

---

## Architecture

```
EventBridge Scheduler
        │
        ▼
AWS Lambda
        │
        ▼
Elastic Load Balancer API
        │
        ▼
Describe Target Health
        │
        ▼
Healthy? ─────────────► Yes → Log Status
        │
        ▼
No
        │
        ▼
Amazon SNS
        │
        ▼
Email Notification
```

---

## AWS Services Used

- AWS Lambda
- Elastic Load Balancer (Application Load Balancer)
- Target Groups
- Amazon EC2
- Amazon SNS
- Amazon EventBridge Scheduler
- AWS IAM
- Amazon CloudWatch
- Boto3

---

## Features

- Periodically monitors ALB Target Group health.
- Detects unhealthy EC2 instances.
- Sends email alerts through Amazon SNS.
- Uses EventBridge Scheduler for automation.
- Logs monitoring activities in CloudWatch.
- Uses least-privilege IAM permissions.

---

## Project Structure

```
a-08-alb-health-check/
│
├── README.md
├── architecture.md
├── deployment.md
├── lambda_function.py
└── screenshots/
```

---

## Workflow

1. EventBridge Scheduler invokes Lambda every 5 minutes.
2. Lambda queries ALB Target Group health.
3. Lambda identifies unhealthy targets.
4. SNS sends an email notification if unhealthy targets exist.
5. CloudWatch stores execution logs.

---

## Testing

The solution was tested by:

- Deploying an Apache web server on Ubuntu EC2.
- Registering the EC2 instance with an ALB Target Group.
- Stopping the Apache service.
- Verifying the Target Group became unhealthy.
- Confirming that Lambda detected the unhealthy target.
- Receiving an SNS email notification.
- Restarting Apache and confirming recovery.

---

## Outcome

Successfully implemented an automated ALB health monitoring solution capable of detecting unhealthy targets and notifying administrators through Amazon SNS.
