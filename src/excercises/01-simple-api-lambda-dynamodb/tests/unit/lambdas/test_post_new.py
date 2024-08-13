import pytest
import os
import json
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from api_lambda_dynamodb.backend.api.lambdas.post_new.runtime.lambda_function import lambda_handler, add_item_to_table, parse_received_content, response_payload


@pytest.fixture
def mock_dynamodb_table():
    with patch("api_lambda_dynamodb.backend.api.lambdas.post_new.runtime.lambda_function.DYNAMODB") as mock_dynamodb, \
         patch("api_lambda_dynamodb.backend.api.lambdas.post_new.runtime.lambda_function.TABLE_NAME", "mock_table_name"):
        mock_table = MagicMock()
        mock_dynamodb.Table.return_value = mock_table
        yield mock_table


def test_add_item_to_table_success(mock_dynamodb_table):
    mock_dynamodb_table.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

    item = {"name": "Test News"}
    result = add_item_to_table(item)

    assert result is True
    mock_dynamodb_table.put_item.assert_called_once()


def test_add_item_to_table_failure(mock_dynamodb_table):
    mock_dynamodb_table.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 500}}

    item = {"name": "Test News"}
    result = add_item_to_table(item)

    assert result is False
    mock_dynamodb_table.put_item.assert_called_once()


def test_parse_received_content_valid_json():
    payload = '{"name": "Test News"}'
    result = parse_received_content(payload)
    assert result == {"name": "Test News"}


def test_parse_received_content_invalid_json():
    payload = '{"name": "Test News"'  # Invalid JSON
    result = parse_received_content(payload)
    assert isinstance(result, json.JSONDecodeError)


def test_response_payload_success():
    response = {"Response": "New added into the BD"}
    result = response_payload(None, response)
    assert result["statusCode"] == "200"
    assert result["body"] == json.dumps(response)


def test_response_payload_error():
    result = response_payload("Error occurred", None)
    assert result["statusCode"] == "400"
    assert result["body"] == "Error occurred"


def test_lambda_handler_no_body(mock_dynamodb_table):
    event = {"body": None}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == "400"
    assert "Body not found" in response["body"]


def test_lambda_handler_success(mock_dynamodb_table):
    mock_dynamodb_table.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 200}}

    event = {"body": '{"name": "Test News"}'}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == "200"
    assert "New added into the BD" in response["body"]
    mock_dynamodb_table.put_item.assert_called_once()


def test_lambda_handler_put_item_failure(mock_dynamodb_table):
    mock_dynamodb_table.put_item.return_value = {"ResponseMetadata": {"HTTPStatusCode": 500}}

    event = {"body": '{"name": "Test News"}'}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == "400"
    assert "Error to add item to the table" in response["body"]
    mock_dynamodb_table.put_item.assert_called_once()
