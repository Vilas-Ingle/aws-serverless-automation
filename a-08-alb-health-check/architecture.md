# Architecture

## Overview

This solution continuously monitors the health of EC2 instances registered behind an AWS Application Load Balancer (ALB). An Amazon EventBridge Scheduler periodically invokes an AWS Lambda function, which checks the health status of targets in the ALB Target Group using the Elastic Load Balancing API.

If any target is found to be unhealthy, the Lambda function publishes an alert to an Amazon SNS topic, which immediately sends an email notification to the subscribed administrator. All execution details are logged in Amazon CloudWatch for monitoring and troubleshooting.

---

## Architecture Diagram

```text
                Amazon EventBridge Scheduler
                           │
                           ▼
                    AWS Lambda Function
                           │
                           ▼
      Elastic Load Balancing (DescribeTargetHealth)
                           │
                           ▼
                 ALB Target Group Health
                           │
          ┌────────────────┴────────────────┐
          │                                 │
          ▼                                 ▼
     Healthy Target                  Unhealthy Target
          │                                 │
          ▼                                 ▼
 CloudWatch Logs                 Amazon SNS Notification
                                           │
                                           ▼
                                   Email Alert
```

---

## Components

### Amazon EventBridge Scheduler

- Invokes the Lambda function automatically every 5 minutes.
- Eliminates the need for manual execution.

### AWS Lambda

- Performs health monitoring logic.
- Retrieves the target health status using Boto3.
- Detects unhealthy instances.
- Sends notifications through SNS.
- Writes execution logs to CloudWatch.

### Application Load Balancer

- Routes incoming traffic to registered EC2 instances.
- Performs continuous health checks on targets.

### Target Group

- Maintains registered EC2 instances.
- Reports health status for each target.

### Amazon SNS

- Delivers email notifications whenever an unhealthy target is detected.

### Amazon CloudWatch

- Stores Lambda execution logs.
- Helps verify successful executions and troubleshoot failures.

---

## Monitoring Workflow

1. EventBridge Scheduler triggers the Lambda function.
2. Lambda queries the Target Group health.
3. Lambda evaluates each registered target.
4. If all targets are healthy:
   - Execution is logged in CloudWatch.
5. If any target is unhealthy:
   - Lambda publishes an SNS notification.
   - SNS sends an email alert.
6. CloudWatch stores detailed execution logs for every invocation.
