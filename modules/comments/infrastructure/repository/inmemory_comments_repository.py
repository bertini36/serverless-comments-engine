import json
import os.path
from collections import defaultdict
from typing import List

from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository


class InMemoryCommentsRepository(CommentsRepository):
    COMMENTS_PATH = 'data/comments.json'

    def __init__(self):
        self.data = defaultdict(list)
        if os.path.exists(self.COMMENTS_PATH):
            self.data = defaultdict(list, self._read_comments_json())

    def get_comments(self, post_slug: str) -> List[Comment] or None:
        return self.data[post_slug]

    def add_comment(self, comment: Comment):
        self.data[comment.post_slug].append(comment)
        self._write_comments_json()

    def _read_comments_json(self) -> dict:
        serialized_data = json.load(open(self.COMMENTS_PATH, 'r'))
        data = {
            post_slug: [
                Comment(**comment_kwargs) for comment_kwargs in raw_comments
            ]
            for post_slug, raw_comments in serialized_data.items()
        }
        return data

    def _write_comments_json(self):
        serialized_data = {
            post_slug: [comment.serialize() for comment in comments]
            for post_slug, comments in self.data.items()
        }
        json.dump(serialized_data, open(self.COMMENTS_PATH, 'w'))
