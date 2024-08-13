#!/usr/bin/env python3
import os

import aws_cdk as cdk

from api_lambda_dynamodb.components import ApiLambdaDynamodbStack


app = cdk.App()
ApiLambdaDynamodbStack(app, "ApiLambdaDynamodbStack")
app.synth()
