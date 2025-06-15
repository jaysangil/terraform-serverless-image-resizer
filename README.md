# terraform-serverless-image-resizer

![CI](https://github.com/<your-user>/terraform-serverless-image-resizer/actions/workflows/cicd.yml/badge.svg)

## 🚀 Project Summary

A serverless Image Resizer API:

- **POST** an image URL + dimensions → **200** with a resized PNG.
- All infra via Terraform on AWS Free Tier.
- Full CI/CD via GitHub Actions.

## 🧱 Tech Stack

- **IaC**: Terraform (AWS provider)
- **Serverless**: AWS Lambda (Python 3.9)
- **API**: API Gateway
- **Libs**: Pillow, requests
- **CI/CD**: GitHub Actions
- **Tests**: pytest

## 🔨 Setup & Usage

1. **Clone & Configure**

   ```bash
    git clone https://github.com/<your-user>/terraform-serverless-image-resizer.git
    cd terraform-serverless-image-resizer

2. **Local Test**

   ```cd lambda
    pip install -r requirements.txt pytest
    pytest tests

3. **Terraform Deploy**

   ```cd terraform
    terraform init
    terraform apply -auto-approve

4. **Invoke API**

   ```export URL=$(terraform output -raw api_endpoint)
    curl "${URL}?url=https://via.placeholder.com/150&width=50&height=50" \
    --output resized.png

