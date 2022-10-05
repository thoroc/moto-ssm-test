import boto3
from loguru import logger


@logger.catch()
def lambda_handler(event, context):

    logger.info("even: {}", event)
    logger.info("context: {}", context)

    ssm_client = boto3.client("ssm", "eu-west-1")

    ami_param_name = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-ebs"
    ami_param_value = ssm_client.get_parameter(Name=ami_param_name)

    ecs_param_name = "/aws/service/ecs/optimized-ami/amazon-linux-2/recommended"
    ecs_param_value = ssm_client.get_parameter(Name=ecs_param_name)

    return [ami_param_value, ecs_param_value]
