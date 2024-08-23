from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import boto3

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.client import DynamoDBClient

logger = logging.getLogger(__name__)


def init_store() -> None:
    """Initialize table as needed."""
    # TODO: Need a pattern to update endpoint_url dynamically
    dynamodb: DynamoDBClient = boto3.client(
        "dynamodb",
        # endpoint_url="http://127.0.0.1:8000",
        endpoint_url="http://dynamodb-local:8000",
    )

    paginator = dynamodb.get_paginator("list_tables")

    table_names = []
    for page in paginator.paginate():
        for table_name in page.get("TableNames", []):
            table_names.append(table_name)

    print("Tables defined in DynamoDB:")
    print("\t" + "\n\t".join(table_names))
    logger.info("Loaded store.")
