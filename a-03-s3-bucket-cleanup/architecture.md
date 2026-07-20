# Architecture

## Components

### Amazon S3

Stores application files to be monitored.

---

### AWS Lambda

Responsible for:

- Listing objects.
- Checking object age.
- Deleting objects older than retention period.
- Logging execution.

---

### IAM

Execution Role

- AmazonS3FullAccess
- AWSLambdaBasicExecutionRole

Deployment User

- Lambda UpdateFunctionCode
- Lambda GetFunction
- Lambda GetFunctionConfiguration

---

### GitHub Actions

Automates Lambda deployment whenever code is pushed to the main branch.

---

# Workflow

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

## Data Flow

1. Lambda lists S3 objects.
2. Reads LastModified timestamp.
3. Compares with configured retention period.
4. Deletes expired objects.
5. Logs actions in CloudWatch.

---

## Monitoring

Amazon CloudWatch Logs

Used for:

- Lambda execution logs
- Deleted object logs
- Error monitoring
