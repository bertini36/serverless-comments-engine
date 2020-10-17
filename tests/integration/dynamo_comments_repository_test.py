import os

import boto3
from structlog import get_logger

from src.modules.comments.domain.comment import Comment
from src.modules.comments.infrastructure.repository.dynamo_comments_repository import (  # noqa
    DynamoCommentsRepository,
)

logger = get_logger()


def create_comments_table():
    client = boto3.resource(
        'dynamodb',
        region_name=os.environ.get('REGION_NAME'),
        endpoint_url=os.environ.get('DYNAMODB_ENDPOINT_URL'),
    )
    table_name = os.environ.get('COMMENTS_TABLE')
    table = client.Table(table_name)
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': 'postSlug', 'KeyType': 'HASH'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': 'postSlug', 'AttributeType': 'S'},
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10,
        },
    }
    try:
        table = client.create_table(**params)
        table.wait_until_exists()
        logger.info('dynamo-table-created', table_name=table_name)
    except client.exceptions.ResourceInUseException:
        pass
    return table


create_comments_table()


def test_add_comment():
    comment = Comment(
        post_slug='dummy',
        name='John Doe',
        email='john@doe.com',
        text='Ouh mama',
    )
    DynamoCommentsRepository().add_comment(comment)


def test_get_comments():
    comments = DynamoCommentsRepository().get_comments('dummy')
    assert type(comments) is list
