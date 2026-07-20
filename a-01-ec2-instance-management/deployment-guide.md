# Deployment Guide

## Overview

This guide explains how to deploy the EC2 Instance Management Lambda function on AWS and configure GitHub Actions for automated deployments.

---

# Prerequisites

Before starting, ensure you have:

- AWS Account
- GitHub Account
- Python 3.14
- AWS CLI installed and configured
- Git installed
- An existing GitHub repository

---

# Step 1 - Create EC2 Instances

Create two EC2 instances.

Apply the following tags:

| Instance | Tag Key | Tag Value |
|----------|---------|-----------|
| Instance 1 | Action | Auto-Stop |
| Instance 2 | Action | Auto-Start |

---

# Step 2 - Create IAM Role

Create a Lambda execution role.

Attach the required EC2 permissions:

- DescribeInstances
- StartInstances
- StopInstances

CloudWatch logging permissions should also be attached.

---

# Step 3 - Create Lambda Function

Create a new Lambda function.

Configuration:

| Setting | Value |
|---------|-------|
| Runtime | Python 3.14 |
| Handler | lambda_function.lambda_handler |
| Execution Role | ec2-instance-manager-role |

Upload the project source code.

---

# Step 4 - Test Lambda

Create a test event.

Execute the function.

Verify:

- Auto-Start instance starts.
- Auto-Stop instance stops.
- CloudWatch logs are generated.

---

# Step 5 - Configure GitHub Actions

Create the following GitHub Repository Secrets:

| Secret Name |
|--------------|
| AWS_ACCESS_KEY_ID |
| AWS_SECRET_ACCESS_KEY |
| AWS_REGION |

---

# Step 6 - Create GitHub Workflow

Create:

```
.github/workflows/deploy-lambda.yml
```

The workflow performs:

- Checkout Repository
- Configure AWS Credentials
- Package Lambda
- Deploy Lambda

---

# Step 7 - Deploy

Commit the changes:

```
git add .
git commit -m "Deploy Lambda automation"
git push origin main
```

GitHub Actions automatically deploys the latest Lambda code.

---

# Step 8 - Verify Deployment

Verify:

- GitHub Actions workflow succeeds.
- Lambda code is updated.
- Lambda executes successfully.
- CloudWatch logs are generated.
- EC2 instances start and stop as expected.

---

# Deployment Completed

The project has now been successfully deployed with an automated CI/CD pipeline.

Future code changes only require:

```
git add .
git commit -m "Update Lambda"
git push origin main
```

GitHub Actions automatically handles the deployment process.
