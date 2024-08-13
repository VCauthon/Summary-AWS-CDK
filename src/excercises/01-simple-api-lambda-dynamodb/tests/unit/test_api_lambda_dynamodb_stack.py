import aws_cdk as core
import aws_cdk.assertions as assertions

from api_lambda_dynamodb.components import ApiLambdaDynamodbStack


def test_dynamodb_table_exists():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that the DynamoDB table exists
    template.resource_count_is("AWS::DynamoDB::Table", 1)


def test_lambda_functions_exist():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that there are exactly 2 Lambda functions
    template.resource_count_is("AWS::Lambda::Function", 2)


def test_api_gateway_exists():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that the API Gateway RestApi exists
    template.resource_count_is("AWS::ApiGateway::RestApi", 1)
