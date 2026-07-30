# Architecture

## Solution Overview

This project implements a **serverless security monitoring solution** that continuously audits Amazon S3 bucket permissions.

The solution automatically detects publicly accessible S3 buckets and notifies administrators through Amazon SNS.

The architecture follows an event-driven, serverless design with no infrastructure management.

---

# Architecture Diagram

```
                    Amazon EventBridge Scheduler
                              │
                              │ Scheduled Trigger
                              ▼
                    AWS Lambda Function (Python)
                              │
          ┌───────────────────┴───────────────────┐
          │                                       │
          ▼                                       ▼
   Amazon S3 API                         Amazon CloudWatch
(List Buckets & Check Policy)               Execution Logs
          │
          ▼
 Detect Public Buckets
          │
          ▼
      Amazon SNS
          │
          ▼
   Email Notification
```

---

# Components

## Amazon EventBridge Scheduler

- Executes the Lambda function automatically on a daily schedule.
- Eliminates manual execution.
- Enables continuous security monitoring.

---

## AWS Lambda

Responsible for:

- Listing all S3 buckets.
- Checking Bucket Policy Status.
- Identifying public buckets.
- Publishing SNS notifications.
- Logging execution details to CloudWatch.

Runtime:

- Python 3.14

---

## Amazon S3

Provides the buckets being audited.

The Lambda checks each bucket using:

- ListBuckets
- GetBucketPolicyStatus

---

## Amazon SNS

Delivers email notifications whenever a public bucket is detected.

Notification includes:

- Bucket Name
- Security Alert

---

## Amazon CloudWatch

Captures Lambda execution logs for:

- Troubleshooting
- Monitoring
- Auditing

---

## AWS IAM

Implements the Principle of Least Privilege.

Lambda permissions include:

- List S3 Buckets
- Read Bucket Policy Status
- Publish SNS Messages
- Write CloudWatch Logs

---

# Execution Flow

1. EventBridge Scheduler triggers the Lambda function.
2. Lambda retrieves all S3 buckets.
3. Each bucket is inspected using the Bucket Policy Status API.
4. Public buckets are collected.
5. If one or more public buckets exist:
   - SNS notification is published.
   - Email alert is sent.
6. CloudWatch stores execution logs.

---

# Security Design

This project follows AWS security best practices:

- Serverless architecture
- Least Privilege IAM
- Automated monitoring
- Event-driven execution
- Centralized logging

---

# Design Decisions

### Why EventBridge Scheduler?

- Native AWS scheduling service
- Fully managed
- Reliable
- No infrastructure required

---

### Why AWS Lambda?

- Pay-per-use pricing
- Automatic scaling
- No server management
- Easy integration with AWS services

---

### Why SNS?

- Fully managed notification service
- Email integration
- Low operational overhead

---

### Why Bucket Policy Status API?

Instead of manually parsing bucket policies, the solution uses AWS's Bucket Policy Status API, which evaluates whether a bucket is publicly accessible and returns a simple boolean result.

This reduces complexity and improves reliability.

---

# Future Enhancements

- Detect public access through Bucket ACLs.
- Audit Object ACL permissions.
- Generate compliance reports.
- Store audit history in DynamoDB.
- Integrate with AWS Security Hub.
