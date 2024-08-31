from aws_cdk import (
    aws_apigateway as apigateway,
)
from constructs import Construct

from web_page_with_db.backend.api.lambdas.get_characters.infrastructure import LambdaGetCharacters


class ApiGetWayNews(Construct):
    def __init__(self, scope: Construct, id: str, table_name: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.lambda_get_new = LambdaGetCharacters(self, "LambdaGetCharacters", table_name)
        api = apigateway.RestApi(
            self,
            "CharactersApi",
            rest_api_name="CharactersApi",
            description="Returns the existing wheel of the time characters",
        )

        # Endpoints to list and query news
        news_resource = api.root.add_resource("characters")
        news_resource_by_id = news_resource.add_resource("{id}")
        for endpoint in [news_resource, news_resource_by_id]:
            endpoint.add_method(
                http_method="GET",
                integration=apigateway.LambdaIntegration(
                    self.lambda_get_new.lambda_function,
                    request_templates={"application/json": '{ "statusCode": "200" }'},
                ),
            )
