moto 4.0.6

Solution to test ssm get_parameter when calling AWS own params:

    - /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-ebs (already present in moto)
    - /aws/service/ecs/optimized-ami/amazon-linux-2/recommended (not yet in moto)

See the test setup in /tests/conftest.py