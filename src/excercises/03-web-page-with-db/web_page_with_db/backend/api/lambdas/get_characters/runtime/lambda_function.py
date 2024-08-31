from typing import Dict
import json
import logging
import os

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

DYNAMODB = boto3.resource("dynamodb")
TABLE_NAME = os.getenv("TABLE_NAME")


def get_all_characters():
    table = DYNAMODB.Table(TABLE_NAME)
    try:
        response = table.scan(
            ProjectionExpression="ID, #nm",
            ExpressionAttributeNames={"#nm": "Name"})
        return response.get("Items", [])
    except ClientError as e:
        logger.error(f"Error fetching all news items: {e.response['Error']['Message']}")
        return None


def get_character_by_id(news_id: int) -> Dict[str, str]:
    table = DYNAMODB.Table(TABLE_NAME)
    try:
        response = table.get_item(Key={"id": news_id})
        return response.get("Item")
    except ClientError as e:
        logger.error(
            f"Error fetching news item by ID: {e.response['Error']['Message']}"
        )
        return None


def lambda_handler(event: Dict[str, str], context: Dict[str, str]) -> Dict[str, str]:
    logger.debug("Event: {}".format(json.dumps(event)))

    response, err = None, None

    if event["resource"] == "/characters":
        response = get_all_characters()
        if response is None:
            err = "Error fetching news items."

    elif event["resource"] == "/news/{id}":
        news_id = event["pathParameters"]["id"]
        response = get_character_by_id(news_id)
        if response is None:
            err = f"News item with ID {news_id} not found."

    else:
        err = "Invalid request made"

    return response_payload(err, response)


def response_payload(err: str, response: Dict[str, str]):
    return {
        "statusCode": "400" if err else "200",
        "body": json.dumps({"error": err}) if err else json.dumps(response),
        "headers": {
            "Content-Type": "application/json",
        },
    }
