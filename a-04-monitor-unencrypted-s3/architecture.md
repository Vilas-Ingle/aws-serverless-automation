# Architecture

## Components

### Amazon S3

Stores buckets to be monitored.

### AWS Lambda

- Lists buckets.
- Reads encryption configuration.
- Logs encryption status.

### IAM

Execution Role

- AWSLambdaBasicExecutionRole
- s3:ListAllMyBuckets
- s3:GetEncryptionConfiguration

Deployment User

- Lambda UpdateFunctionCode
- Lambda GetFunction
- Lambda GetFunctionConfiguration

### GitHub Actions

Automatically deploys Lambda when changes are pushed to the main branch.

---

## Workflow

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

1. Lambda lists all S3 buckets.
2. Reads bucket encryption configuration.
3. Logs encryption status.
4. CloudWatch stores execution logs.
