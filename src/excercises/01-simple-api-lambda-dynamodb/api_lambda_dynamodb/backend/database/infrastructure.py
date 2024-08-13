from aws_cdk import (
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
)

from constructs import Construct


class ApiLambdaDynamoDbStack(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.table = dynamodb.Table(
            self,
            "NewsTable",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

    def allow_read_access(self, lambda_function: lambda_.Function):
        self.table.grant_read_data(lambda_function)

    def allow_write_access(self, lambda_function: lambda_.Function):
        self.table.grant_write_data(lambda_function)
