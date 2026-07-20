# Deployment Guide

## Prerequisites

- AWS Account
- AWS Lambda
- Amazon EventBridge
- IAM
- GitHub Actions
- Python 3.14

## Deployment Steps

1. Create the Lambda execution role.
2. Deploy the Lambda function.
3. Create an EventBridge rule for EC2 instance launch events.
4. Add the Lambda function as the EventBridge target.
5. Grant EventBridge permission to invoke the Lambda.
6. Configure GitHub Actions for automated deployment.
7. Push changes to the main branch.

## Testing

- Launch a new EC2 instance.
- Verify Lambda invocation.
- Confirm default tags are applied.
- Review CloudWatch logs.

## Verification

- EC2 instance contains default tags.
- Lambda executed successfully.
- GitHub Actions deployment succeeded.
