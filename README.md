#  AWS Serverless Automation – EC2 Instance Management

![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-success)
![License](https://img.shields.io/badge/Status-Completed-brightgreen)

---

##  Project Overview

This project automates the management of Amazon EC2 instances using **AWS Lambda** and **Python (Boto3)**. EC2 instances are automatically started or stopped based on predefined resource tags.

To follow modern DevOps practices, the project also implements a **CI/CD pipeline using GitHub Actions**, enabling automatic deployment of the Lambda function whenever code is pushed to the **main** branch.

This project demonstrates cloud automation, Infrastructure Operations, secure IAM practices, and deployment automation using AWS services.

---

#  Project Objectives

- Automate EC2 instance management using AWS Lambda
- Reduce manual operational effort
- Implement secure IAM permissions using the Principle of Least Privilege
- Build an automated deployment pipeline with GitHub Actions
- Gain hands-on experience with AWS serverless services

---

#  Features

-  Automatic EC2 Start
-  Automatic EC2 Stop
-  Tag-based EC2 Management
-  AWS Lambda using Python (Boto3)
-  CloudWatch Logging
-  GitHub Actions CI/CD Pipeline
-  Secure GitHub Secrets
-  IAM Least Privilege Policy
-  Automated Lambda Deployment

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Cloud | AWS |
| Compute | AWS Lambda |
| Virtual Machines | Amazon EC2 |
| Programming Language | Python 3.14 |
| SDK | Boto3 |
| Monitoring | Amazon CloudWatch |
| IAM | AWS IAM |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |
| Deployment | AWS CLI |

---

#  Project Structure

```
aws-serverless-automation/
│
├── .github/
│   └── workflows/
│       └── deploy-lambda.yml
│
├── a-01-ec2-instance-management/
│   ├── lambda_function.py
│   ├── iam-policy.json
│   ├── architecture.md
│   ├── requirements.txt
│   └── README.md
│
├── docs/
│   ├── architecture/
│   ├── screenshots/
│   └── deployment-guide.md
│
└── README.md
```

---

# Solution Architecture

```
                    Developer
                        │
                 Code Changes
                        │
                        ▼
                 Git Push (main)
                        │
                        ▼
               GitHub Repository
                        │
                        ▼
            GitHub Actions Workflow
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
Checkout Code   Configure AWS    Package Lambda
                  Credentials
                        │
                        ▼
              Deploy Lambda Function
                        │
                        ▼
                AWS Lambda Function
                        │
                        ▼
          Read EC2 Tags using Boto3
                │               │
                ▼               ▼
     Action = Auto-Stop   Action = Auto-Start
                │               │
                ▼               ▼
      Stop EC2 Instance   Start EC2 Instance
                        │
                        ▼
                 CloudWatch Logs
```

---

#  CI/CD Pipeline

Whenever code is pushed to the **main** branch:

1. GitHub Actions is triggered.
2. Source code is checked out.
3. AWS credentials are securely loaded from GitHub Secrets.
4. Lambda deployment package is created.
5. AWS CLI deploys the updated Lambda function.
6. Latest code becomes immediately available in AWS Lambda.

---

# GitHub Actions Workflow

The workflow performs the following steps:

- Checkout Repository
- Configure AWS Credentials
- Package Lambda Function
- Deploy Lambda using AWS CLI

---

#  Security Implementation

Security best practices implemented:

- Dedicated IAM User for GitHub Actions
- Principle of Least Privilege
- GitHub Repository Secrets
- No AWS credentials stored in source code
- Secure deployment using AWS CLI

---

#  Monitoring & Logging

Amazon CloudWatch Logs are used for:

- Lambda execution monitoring
- Error tracking
- Deployment verification
- Troubleshooting

The project uses Python's built-in **logging** module instead of print statements to produce structured logs.

---

#  Testing Performed

The following scenarios were successfully validated:

-  Start EC2 instance using `Action=Auto-Start`
-  Stop EC2 instance using `Action=Auto-Stop`
-  Lambda execution
-  CloudWatch log generation
-  GitHub Actions deployment
-  Code deployment verification

---

#  Git Workflow

The project follows a standard Git workflow:

```
Feature Branch
      │
      ▼
Code Changes
      │
      ▼
Commit
      │
      ▼
Push
      │
      ▼
Pull Request
      │
      ▼
Code Review
      │
      ▼
Merge to Main
      │
      ▼
GitHub Actions Deployment
```

---

#  Project Screenshots

The project includes screenshots demonstrating:

- GitHub Repository
- GitHub Actions Successful Run
- AWS Lambda Function
- CloudWatch Logs
- IAM Configuration

Screenshots are available under:

```
docs/screenshots/
```

---

#  Future Enhancements

- EventBridge Scheduled Execution
- OIDC Authentication for GitHub Actions
- Infrastructure as Code using Terraform
- Multi-Environment Deployment (Dev/QA/Prod)
- Automated Unit Testing

---

#  Skills Demonstrated

This project demonstrates practical experience with:

- AWS Lambda
- Amazon EC2
- Boto3
- IAM Roles & Policies
- CloudWatch
- Git
- GitHub
- GitHub Actions
- CI/CD
- AWS CLI
- Python Automation
- DevOps Best Practices

---

# Author

**Vilas Ingle**

GitHub: https://github.com/Vilas-Ingle

---

##  Project Status

**Completed Successfully**

This project was developed as part of a serverless automation assignment while following industry-inspired DevOps practices including Git workflow, secure IAM configuration, CI/CD automation, structured logging, and automated cloud deployments.
