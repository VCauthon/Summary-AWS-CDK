import pytest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from api_lambda_dynamodb.backend.api.lambdas.get_new.runtime.lambda_function import lambda_handler, get_all_news, get_news_by_id


@pytest.fixture
def mock_dynamodb_table():
    with patch("api_lambda_dynamodb.backend.api.lambdas.get_new.runtime.lambda_function.DYNAMODB") as mock_dynamodb, \
         patch("api_lambda_dynamodb.backend.api.lambdas.get_new.runtime.lambda_function.TABLE_NAME", "mock_table_name"):
        mock_table = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        yield mock_table 


def test_get_all_news(mock_dynamodb_table):
    mock_dynamodb_table.scan.return_value = {
        "Items": [{"id": "1", "title": "News 1"}, {"id": "2", "title": "News 2"}]
    }

    result = get_all_news()
    assert result == [{"id": "1", "title": "News 1"}, {"id": "2", "title": "News 2"}]


def test_get_news_by_id(mock_dynamodb_table):
    mock_dynamodb_table.get_item.return_value = {"Item": [{"id": "1", "title": "News 1"}]}

    result = get_news_by_id(1)
    assert result == [{"id": "1", "title": "News 1"}]


def test_lambda_handler_all_news(mock_dynamodb_table):
    mock_dynamodb_table.scan.return_value = {
        "Items": [{"id": "1", "title": "News 1"}, {"id": "2", "title": "News 2"}]
    }
    event = {"resource": "/news", "pathParameters": {}}
    response = lambda_handler(event, {})
    assert response["statusCode"] == "200"
    assert "News 1" in response["body"]


def test_lambda_handler_news_by_id(mock_dynamodb_table):
    mock_dynamodb_table.get_item.return_value = {"Item": [{"id": "1", "title": "News 1"}]}
    event = {"resource": "/news/{id}", "pathParameters": {"id": "1"}}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == "200"
    assert "News 1" in response["body"]


@patch("api_lambda_dynamodb.backend.api.lambdas.get_new.runtime.lambda_function.boto3")
def test_lambda_handler_invalid_resource(boto3_mock):
    event = {"resource": "/invalid", "pathParameters": {}}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == "400"
    assert "Invalid request made" in response["body"]
