# Deployment Guide

## Objective

Deploy an automated monitoring solution that periodically checks the health of EC2 instances behind an Application Load Balancer (ALB) and sends an Amazon SNS email notification whenever any target becomes unhealthy.

---

## Deployment Steps

### 1. Launch EC2 Instance
- Created an Ubuntu 24.04 EC2 instance.
- Installed and started Apache Web Server.
- Configured the Security Group to allow SSH (22) and HTTP (80).

### 2. Create Target Group
- Created an HTTP Target Group.
- Registered the EC2 instance.
- Verified the target health status as **Healthy**.

### 3. Create Application Load Balancer
- Created an Internet-facing ALB.
- Configured an HTTP (Port 80) listener.
- Forwarded traffic to the Target Group.
- Updated the ALB Security Group to allow inbound HTTP traffic.
- Verified the Apache page using the ALB DNS.

### 4. Configure Amazon SNS
- Created an SNS Standard Topic: **alb-health-alerts**.
- Added an email subscription.
- Confirmed the subscription through email.

### 5. Create IAM Role
Created a Lambda execution role with the following permissions:
- ElasticLoadBalancingReadOnly
- AmazonSNSFullAccess
- AWSLambdaBasicExecutionRole

### 6. Create Lambda Function
- Runtime: Python 3.14
- Configured Boto3 clients for ELBv2 and SNS.
- Retrieved Target Group health using `describe_target_health()`.
- Sent SNS notifications when unhealthy targets were detected.
- Logged execution details to CloudWatch.

### 7. Configure EventBridge Scheduler
- Created an EventBridge Scheduler.
- Configured it to invoke the Lambda function every **5 minutes**.

---

## Testing

### Healthy Scenario
- Apache service running.
- Lambda executed successfully.
- CloudWatch logs reported **All targets are healthy**.
- No SNS notification was sent.

### Unhealthy Scenario
- Stopped Apache using:

```bash
sudo systemctl stop apache2
```

- Target Group status changed to **Unhealthy**.
- EventBridge triggered the Lambda.
- Lambda detected the unhealthy target.
- SNS successfully delivered an email notification.

Restarted Apache:

```bash
sudo systemctl start apache2
```

Target health returned to **Healthy**.

---

## Issues Encountered

- ALB was initially inaccessible due to missing HTTP inbound rule in the ALB Security Group. Resolved by allowing **HTTP (80)** from **0.0.0.0/0**.
- SNS notifications initially failed because the **Subscription ARN** was mistakenly used instead of the **SNS Topic ARN**. Updating the correct Topic ARN resolved the issue.

---

## Result

Successfully implemented an automated ALB health monitoring solution using **Application Load Balancer, Target Groups, AWS Lambda, EventBridge Scheduler, Amazon SNS, CloudWatch, IAM, and Boto3**. The solution continuously monitors target health and automatically notifies administrators whenever an unhealthy target is detected.
