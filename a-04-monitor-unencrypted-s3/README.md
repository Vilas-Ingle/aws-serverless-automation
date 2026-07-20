# Monitor Unencrypted S3 Buckets using AWS Lambda

## Project Overview

This project monitors Amazon S3 buckets and checks whether default server-side encryption is enabled. AWS Lambda scans all S3 buckets in the account and logs their encryption status to Amazon CloudWatch.

---

## Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ▼
AWS Lambda
     │
     ▼
Amazon S3
```

---

## Features

- Lists all S3 buckets.
- Checks default bucket encryption.
- Logs encrypted and unencrypted buckets.
- GitHub Actions CI/CD deployment.
- CloudWatch logging.
- Least-privilege IAM permissions.

---

## Project Structure

```
a-04-monitor-unencrypted-s3/
├── lambda_function.py
├── github-actions-policy.json
├── requirements.txt
├── README.md
├── architecture.md
└── screenshots/
```

---

## Prerequisites

- AWS Account
- Amazon S3
- AWS Lambda
- IAM
- GitHub Actions
- Python 3.14

---

## Deployment

1. Create Lambda execution role.
2. Deploy Lambda.
3. Configure GitHub Actions.
4. Push changes to GitHub.
5. GitHub Actions deploys the latest Lambda code.

---

## Testing

- Lambda executed successfully.
- Encryption status verified.
- CloudWatch logs validated.
- GitHub Actions deployment verified.

---

## Screenshots

- Lambda function
- Lambda configuration
- Successful test execution
- CloudWatch logs
- GitHub Actions success

---

## Future Improvements

- Enable encryption automatically for unencrypted buckets.
- Send SNS notifications.
- Schedule periodic scans using EventBridge.

---

## Author

Vilas Ingle
