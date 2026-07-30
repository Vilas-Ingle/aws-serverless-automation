# Deployment Guide

## Prerequisites

Before deploying this project, ensure you have:

- AWS Account
- IAM permissions to create Lambda, SNS, EventBridge Scheduler, and S3 resources
- Python 3.x knowledge
- Basic understanding of AWS serverless services

---

# Step 1: Create an S3 Bucket

1. Open the AWS Management Console.
2. Navigate to **Amazon S3**.
3. Create an S3 bucket.
4. (For testing only) Create an additional bucket that will be configured as a public bucket.

---

# Step 2: Create an SNS Topic

1. Navigate to **Amazon SNS**.
2. Create a Standard Topic.

Example:

```
s3-public-bucket-alerts
```

3. Create an Email subscription.
4. Confirm the subscription from your email inbox.

---

# Step 3: Create IAM Policy

Create a custom IAM policy with permissions for:

- List S3 buckets
- Read Bucket Policy Status
- Publish SNS notifications
- Write CloudWatch Logs

Attach this policy to a new Lambda execution role.

---

# Step 4: Create Lambda Function

1. Open AWS Lambda.
2. Create a new function.

Configuration:

| Setting | Value |
|----------|-------|
| Runtime | Python 3.14 |
| Architecture | x86_64 |
| Execution Role | Custom IAM Role |

Upload:

```
lambda_function.py
```

Update the following variable:

```python
SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"
```

Deploy the function.

---

# Step 5: Configure EventBridge Scheduler

1. Open Amazon EventBridge Scheduler.
2. Create a new schedule.

Configuration:

| Setting | Value |
|----------|-------|
| Schedule Type | Rate / Cron |
| Target | AWS Lambda |
| Lambda Function | s3-public-bucket-audit |
| Execution Role | EventBridge Scheduler Role |

Save the schedule.

---

# Step 6: Configure Public Test Bucket

For testing purposes:

1. Create a temporary S3 bucket.
2. Disable **Block Public Access**.
3. Attach a Bucket Policy that allows public read access.

Example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

---

# Step 7: Test the Solution

## Manual Test

Run the Lambda function using the Test feature.

Verify:

- Lambda execution succeeds.
- CloudWatch logs are generated.
- SNS email notification is received.

---

## Scheduled Test

Allow EventBridge Scheduler to trigger the Lambda automatically.

Verify:

- Lambda executes successfully.
- Public bucket is detected.
- SNS email notification is received.

---

# CloudWatch Verification

Confirm the logs contain messages similar to:

```
Found X buckets.

Public bucket detected:
bucket-name

Notification sent for public buckets.
```

---

# Expected Outcome

The deployed solution should:

- Audit all S3 buckets.
- Detect publicly accessible buckets.
- Publish SNS notifications.
- Deliver email alerts.
- Generate CloudWatch execution logs.

---

# Cleanup

After testing:

- Remove the public Bucket Policy.
- Re-enable **Block Public Access**.
- Delete the temporary test bucket if no longer required.

This prevents unnecessary security risks and avoids repeated notification emails.

---

# Troubleshooting

## No Email Notification

Verify:

- SNS subscription is confirmed.
- Lambda execution role includes `sns:Publish`.
- A public bucket exists.
- Lambda executed successfully.

---

## No Public Bucket Detected

Verify:

- Bucket Policy has been attached.
- Block Public Access is disabled.
- Bucket Policy Status reports the bucket as public.

---

## Lambda Permission Errors

Verify:

- IAM policy is attached to the Lambda execution role.
- EventBridge Scheduler has permission to invoke Lambda.

---

# Project Validation

The deployment is considered successful when:

- Lambda executes successfully.
- EventBridge Scheduler triggers the Lambda.
- Public S3 bucket is detected.
- SNS email notification is delivered.
- CloudWatch logs confirm successful execution.
