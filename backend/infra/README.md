# AWS Deployment Guide

This document outlines the steps to deploy the application to AWS.

## Prerequisites

- Install [uv]()
- Install the [AWS Cloud Development Kit (CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- Setup security credentials for CDK, e.g. by installing [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and running `aws login`
- Navigate to the `backend/app` directory and export the dependencies to `requirements.txt`:

  ```bash
  cd ../app
  uv sync
  uv export -o requirements.txt --no-dev
  ```

## Install dependencies

```bash
uv sync
```

## Deployment

```bash
cdk deploy
```
