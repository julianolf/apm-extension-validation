# apm-extension-validation

Small app to test Elastic APM extension for AWS Lambda Function.

### Before deploying

This project was built using AWS SAM, it requires a AWS account and both AWS CLI and AWS-SAM CLI installed and configured. For details on how to do that follow the documentation [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html).

### Deploying

Just run the command below and follow the instructions on the screen.
```sh
sam deploy --guided
```

**About the security groups and subnets:**
In case you need the Lambda function running inside a specific VPC inform the securit group IDs and Subnet IDs when asked during the deploy, otherwise just remove the following lines from the `template.yaml` file.
```yaml
# Comment or delete VPC configuration if you don't want to specify one explicitly
VpcConfig:
  SecurityGroupIds:
    Ref: SecurityGroups
  SubnetIds:
    Ref: Subnets
```

### Testing

Run the shell script passing the queue URL returned as an output from the deploy process.
```sh
./pub.sh "https://sqs.some-region.amazonaws.com/00000000/apm-extension-validation-queue"
```
