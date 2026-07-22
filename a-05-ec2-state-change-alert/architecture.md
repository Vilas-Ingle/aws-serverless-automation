# Architecture

## Workflow

1. An EC2 instance changes state.
2. Amazon EventBridge receives the EC2 State Change event.
3. EventBridge invokes the Lambda function.
4. Lambda extracts the instance ID and new state.
5. Lambda publishes a message to an SNS Topic.
6. Amazon SNS sends an email notification.
7. CloudWatch stores execution logs.

---

## Architecture Diagram

EC2 Instance

↓

EventBridge Rule

↓

Lambda Function

↓

SNS Topic

↓

Email Notification

↓

CloudWatch Logs

---

## Components

### Amazon EC2

Generates state change events.

### Amazon EventBridge

Listens for EC2 Instance State Change Notification events.

### AWS Lambda

Processes the incoming event and publishes a notification.

### Amazon SNS

Sends email notifications to subscribers.

### CloudWatch

Stores Lambda execution logs.

### GitHub Actions

Automatically deploys updated Lambda code after every push to the main branch.
