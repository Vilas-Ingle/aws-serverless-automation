# Solution Architecture

## Overview

This project automates Amazon EC2 instance management using AWS Lambda.

EC2 instances are identified based on resource tags.

- `Action=Auto-Start`
- `Action=Auto-Stop`

The Lambda function periodically (or manually) scans EC2 instances, determines the required action, performs the start or stop operation, and records execution details in Amazon CloudWatch Logs.

The project also includes a CI/CD pipeline using GitHub Actions to automatically deploy the latest Lambda code.

---

# Architecture Diagram

```
                     Developer
                         │
                    Code Changes
                         │
                         ▼
                     Git Push
                         │
                         ▼
                 GitHub Repository
                         │
                         ▼
               GitHub Actions Workflow
                         │
         ┌───────────────┼─────────────────┐
         │               │                 │
         ▼               ▼                 ▼
   Checkout Code   Configure AWS     Package Lambda
                    Credentials
                         │
                         ▼
               Deploy Updated Code
                         │
                         ▼
                  AWS Lambda Function
                         │
                         ▼
            Describe Tagged EC2 Instances
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 Action = Auto-Stop              Action = Auto-Start
          │                             │
          ▼                             ▼
 Stop Running Instance          Start Stopped Instance
                         │
                         ▼
                Amazon CloudWatch Logs
```

---

# AWS Services Used

## AWS Lambda

Responsible for executing the automation logic.

---

## Amazon EC2

Target compute instances that are started or stopped based on resource tags.

---

## AWS IAM

Provides secure access using:

- Lambda Execution Role
- GitHub Actions IAM User

Both follow the Principle of Least Privilege.

---

## Amazon CloudWatch

Captures Lambda execution logs for:

- Monitoring
- Troubleshooting
- Execution verification

---

## GitHub Actions

Implements Continuous Deployment by automatically updating the Lambda function whenever code is pushed to the `main` branch.

---

# Execution Flow

1. Developer pushes code to GitHub.

2. GitHub Actions workflow starts.

3. Repository is checked out.

4. AWS credentials are securely loaded.

5. Lambda package is created.

6. AWS CLI updates the Lambda function.

7. Lambda executes.

8. Lambda searches for EC2 instances tagged with:

   - `Action=Auto-Start`
   - `Action=Auto-Stop`

9. Matching instances are started or stopped.

10. Execution details are written to CloudWatch Logs.

---

# Security Considerations

The solution follows AWS security best practices:

- Least Privilege IAM Policies
- GitHub Secrets for credentials
- No credentials stored in source code
- Dedicated deployment IAM user
- Separate Lambda execution role

---

# Future Enhancements

- Amazon EventBridge scheduled execution
- OIDC authentication for GitHub Actions
- Terraform deployment
- Multi-environment support
- Automated testing
