#!/usr/bin/env bash

# Install AWS CDK CLI
npm install -g aws-cdk 

# Install AWS SAM CLI
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
sudo ./sam-installation/install
rm -f aws-sam-cli-linux-x86_64.zip
rm -rf ./sam-installation
