/# EC2 State Change Alert using AWS Lambda, EventBridge, and SNS

## Project Overview

This project automatically sends an email notification whenever an EC2 instance changes its state (Running or Stopped).

The solution is fully serverless and event-driven using AWS EventBridge, AWS Lambda, and Amazon SNS.

---

## Architecture

EC2 Instance
↓

Amazon EventBridge

↓

AWS Lambda

↓

Amazon SNS

↓

Email Notification

---

## AWS Services Used

- Amazon EC2
- Amazon EventBridge
- AWS Lambda
- Amazon SNS
- AWS IAM
- Amazon CloudWatch
- GitHub Actions

---

## Features

- Detect EC2 state changes automatically
- Trigger Lambda using EventBridge
- Publish notification using SNS
- Send email alerts
- CloudWatch logging
- Automated Lambda deployment using GitHub Actions

---

## Project Structure

a-05-ec2-state-change-alert/
├── README.md
├── architecture.md
├── deployment-guide.md
├── github-actions-policy.json
├── lambda_function.py
├── requirements.txt
└── screenshots/
---


---

## Outcome

Whenever an EC2 instance enters the Running or Stopped state, an email notification is automatically delivered to the subscribed email address.
