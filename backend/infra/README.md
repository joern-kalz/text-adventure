# AWS Deployment Guide

This document outlines the steps to deploy the application to AWS.

## Prerequisites

- Create an API key for Groq [here](https://console.groq.com/)
- Install Docker
- Install [uv]()
- Install the [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- Setup security credentials for CDK, e.g. by installing [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and running `aws login`
- Navigate to the `backend/app` directory and export the dependencies to `requirements.txt` with

  ```bash
  cd ../app
  uv sync
  uv export -o requirements.txt --no-dev
  ```

## Install dependencies

Install dependencies with:

```bash
uv sync
```

## Deployment

Deploy to an AWS account with:

```bash
cdk deploy
```

Navigate to Secret Manager in the AWS console and set the value of the secret GroqApiKeySecret to the API you created earlier.