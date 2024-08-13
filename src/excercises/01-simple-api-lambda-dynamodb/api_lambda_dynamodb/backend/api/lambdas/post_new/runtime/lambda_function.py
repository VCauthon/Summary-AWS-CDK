from typing import Dict
import json
import logging
import os

import uuid

import boto3


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

DYNAMODB = boto3.resource("dynamodb")
TABLE_NAME = os.getenv("TABLE_NAME")


def add_item_to_table(item: Dict[str, str]):
    table = DYNAMODB.Table(TABLE_NAME)
    response = table.put_item(Item={"id": str(uuid.uuid4())} | item)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return True
    return False


def parse_received_content(payload: str) -> Dict[str, str]:
    try:
        return json.loads(payload)
    except json.JSONDecodeError as err:
        return err


def response_payload(err: str, response: Dict[str, str]):
    return {
        "statusCode": "400" if err else "200",
        "body": err if err else json.dumps(response),
        "headers": {
            "Content-Type": "application/json",
        },
    }


def lambda_handler(event: Dict[str, str], context: Dict[str, str]) -> Dict[str, str]:
    logger.debug("Event: {}".format(json.dumps(event)))

    payload = event.get("body", None)
    if not payload:
        return response_payload("Body not found", None)

    payload = parse_received_content(payload)
    if not isinstance(payload, dict):
        return response_payload(payload, None)

    if "id" in payload:
        return response_payload("ID is a reserved value")

    if not add_item_to_table(payload):
        return response_payload("Error to add item to the table", None)

    return response_payload(None, {"Response": "New added into the BD"})
