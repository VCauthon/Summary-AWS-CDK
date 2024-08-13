from aws_cdk import Stack
from constructs import Construct

from api_lambda_dynamodb.backend.api.infrastructure import ApiGetWayNews
from api_lambda_dynamodb.backend.database.infrastructure import ApiLambdaDynamoDbStack


class ApiLambdaDynamodbStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = ApiLambdaDynamoDbStack(self, "DatabaseService")

        endpoints = ApiGetWayNews(self, "ApiService", table.table.table_name)
        table.allow_read_access(endpoints.lambda_get_new.lambda_function)
        table.allow_write_access(endpoints.lambda_post_new.lambda_function)
