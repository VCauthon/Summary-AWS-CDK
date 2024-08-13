from aws_cdk import (
    aws_apigateway as apigateway,
)
from constructs import Construct

from api_lambda_dynamodb.backend.api.lambdas.get_new.infrastructure import LambdaGetNew
from api_lambda_dynamodb.backend.api.lambdas.post_new.infrastructure import (
    LambdaPostNew,
)


class ApiGetWayNews(Construct):
    def __init__(self, scope: Construct, id: str, table_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the get_new Lambda function
        self.lambda_get_new = LambdaGetNew(self, "LambdaGetNew", table_name)
        self.lambda_post_new = LambdaPostNew(self, "LambdaPostNew", table_name)

        api = apigateway.RestApi(
            self,
            "NewsApi",
            rest_api_name="News Service",
            description="This service serves news items",
        )

        # Endpoints to list and query news
        news_resource = api.root.add_resource("news")
        news_resource_by_id = news_resource.add_resource("{id}")
        for endpoint in [news_resource, news_resource_by_id]:
            endpoint.add_method(
                http_method="GET",
                integration=apigateway.LambdaIntegration(
                    self.lambda_get_new.lambda_function,
                    request_templates={"application/json": '{ "statusCode": "200" }'},
                ),
            )

        # Endpoint to post news
        news_resource.add_method(
            http_method="POST",
            integration=apigateway.LambdaIntegration(
                self.lambda_post_new.lambda_function,
                request_templates={"application/json": '{ "statusCode": "200" }'},
            ),
        )
