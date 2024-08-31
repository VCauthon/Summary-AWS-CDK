import os

from aws_cdk import aws_lambda as lambda_, Duration

from constructs import Construct


class LambdaGetCharacters(Construct):
    def __init__(self, scope: Construct, id: str, table_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        curr_path = os.path.dirname(os.path.realpath(__file__))

        self.lambda_function = lambda_.Function(
            self,
            "LambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset(os.path.join(curr_path, "runtime")),
            memory_size=512,
            timeout=Duration.seconds(30),
            handler="lambda_function.lambda_handler",
            environment={"TABLE_NAME": table_name},
        )
