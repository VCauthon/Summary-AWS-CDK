<table align="center">
  <tr>
    <td>
      <a href="./06-deploying-cycle.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Deploying cycle">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="./07-testing-infrastructure.md">
        <img src="../static/icons/arrow_right.png" alt="Right">
      </a>
    </td>
  </tr>
</table>

---

# TESTING INFRASTRUCTURE

- [Introduction](#introduction)
- [Example Tests](#example-tests)

---

## Introduction

Testing your AWS CDK infrastructure is a crucial step in ensuring that the resources you define behave as expected before deploying them to AWS. By writing tests, you can validate the structure of your stacks, the configuration of your resources, and their interactions. The AWS CDK provides a powerful `assertions` module that allows you to create unit tests for your infrastructure.

---

## Example Tests

Here are some examples of how to test your AWS CDK infrastructure ([and here the examples in code](../excercises/01-simple-api-lambda-dynamodb/tests/unit/test_api_lambda_dynamodb_stack.py)):

<table border="1" cellpadding="10">
  <tr>
    <th>Purpose</th>
    <th>Code Example</th>
    <th>Explanation</th>
  </tr>
  
  <!-- Testing DynamoDB Table -->
  <tr>
    <td>Test DynamoDB Table Exists</td>
    <td>
      <pre><code>
import aws_cdk as core
import aws_cdk.assertions as assertions

from api_lambda_dynamodb.components import ApiLambdaDynamodbStack

def test_dynamodb_table_exists():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that the DynamoDB table exists
    template.resource_count_is("AWS::DynamoDB::Table", 1)
      </code></pre>
    </td>
    <td>Verifies that exactly one DynamoDB table is defined in the stack.</td>
  </tr>

  <!-- Testing Lambda Functions -->
  <tr>
    <td>Test Lambda Functions Exist</td>
    <td>
      <pre><code>
import aws_cdk as core
import aws_cdk.assertions as assertions

from api_lambda_dynamodb.components import ApiLambdaDynamodbStack

def test_lambda_functions_exist():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that there are exactly 2 Lambda functions
    template.resource_count_is("AWS::Lambda::Function", 2)
      </code></pre>
    </td>
    <td>Ensures that two Lambda functions are defined in the stack.</td>
  </tr>

  <!-- Testing API Gateway -->
  <tr>
    <td>Test API Gateway Exists</td>
    <td>
      <pre><code>
import aws_cdk as core
import aws_cdk.assertions as assertions

from api_lambda_dynamodb.components import ApiLambdaDynamodbStack

def test_api_gateway_exists():
    app = core.App()
    stack = ApiLambdaDynamodbStack(app, "api-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

    # Check that the API Gateway RestApi exists
    template.resource_count_is("AWS::ApiGateway::RestApi", 1)
      </code></pre>
    </td>
    <td>Verifies the presence of an API Gateway resource in the stack.</td>
  </tr>
</table>

These examples demonstrate basic tests for ensuring that essential resources like DynamoDB tables, Lambda functions, and API Gateways are correctly defined in your CDK stacks. By running these tests, you can catch errors early in the development process, before deploying your infrastructure to AWS.

---

<table align="center">
  <tr>
    <td>
      <a href="./06-deploying-cycle.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Deploying cycle">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="./07-testing-infrastructure.md">
        <img src="../static/icons/arrow_right.png" alt="Right">
      </a>
    </td>
  </tr>
</table>
