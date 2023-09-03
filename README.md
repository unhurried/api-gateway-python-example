# backend-example-serverless-python

An example of Python-based Restful API implemented with AWS Cloud Development Kit (CDK).    
This project also includes devcontainer.json that can be used to run AWS CDK CLI commands.

To setup the AWS CDK working environment:

```bash
# Create a virtualenv. (only for the first time)
python3 -m venv .venv
# Activate the virtualenv.
source .venv/bin/activate
# Install depencies required for the template generation.
pip install -r requirements.txt
```

To generate an AWS CloudFormation template using AWS CDK:

```bash
# Install dependencies for the app to inlude a Lambda Layer
pip install -r lambda_layer/requirements.txt -t lambda_layer/python
# Generate an AWS CloudFormation template.
cdk synth
```

To run the api locally using AWS SAM CLI:

```bash
sam local start-api -t ./cdk.out/BackendExampleServerlessPythonStack.template.json 
```

To deploy the generated CloudFormation template:

```bash
cdk deploy
```
