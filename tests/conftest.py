import os

import boto3
import pytest
from moto import mock_ssm

AWS_REGION = "eu-west-1"


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture(scope="function")
def mock_ssm_client(aws_credentials):
    with mock_ssm():
        client = boto3.client("ssm", region_name=AWS_REGION)

        from moto.ssm.models import ssm_backends, Parameter
        ssm_backends["123456789012"]["eu-west-1"]._parameters["/aws/service/ecs/optimized-ami/amazon-linux-2/recommended"].append(Parameter(
            account_id="123456789012",
            name="/aws/service/ecs/optimized-ami/amazon-linux-2/recommended",
            value="{\"ecs_agent_version\":\"1.63.1\",\"ecs_runtime_version\":\"Docker version 20.10.13\",\"image_id\":\"ami-002e2fef4b94f8fd0\",\"image_name\":\"amzn2-ami-ecs-hvm-2.0.20220921-x86_64-ebs\",\"image_version\":\"2.0.20220921\",\"os\":\"Amazon Linux 2\",\"schema_version\":1,\"source_image_name\":\"amzn2-ami-minimal-hvm-2.0.20220912.1-x86_64-ebs\"}",
            parameter_type="String",
            description="...",
            allowed_pattern=None,
            keyid=None,
            last_modified_date=1664230158.399,
            version=None,
            tags=[],
            data_type="text",
        ))

        yield client
