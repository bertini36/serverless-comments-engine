import os
from typing import List

import boto3
from botocore.exceptions import ClientError

from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository
from ...domain.exceptions import DatabaseError


class DynamoCommentsRepository(CommentsRepository):
    REGION_NAME = 'eu-west-1'

    def __init__(self):
        self.client = boto3.resource('dynamodb', region_name=self.REGION_NAME)
        self.table = self.client.Table(os.environ['COMMENTS_TABLE'])

    def get_comments(self, post_slug: str) -> List[Comment] or None:
        try:
            response = self.table.get_item(Key={'postSlug': post_slug})
            comment_dicts = response['Item']['comments'] if 'Item' in response else []
            comments = [Comment(**comment_dict) for comment_dict in comment_dicts]
            return comments
        except ClientError:
            raise DatabaseError('Database error')

    def add_comment(self, comment: Comment):
        try:
            previous_comments = self.get_comments(comment.post_slug) or []
            post_data = {
                'postSlug': comment.post_slug,
                'comments': [comment.serialize() for comment in previous_comments]
            }
            post_data['comments'].append(comment.serialize())
            self.table.put_item(Item=post_data)
        except ClientError:
            raise DatabaseError('Database error')
