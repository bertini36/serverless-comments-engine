from dataclasses import asdict
from typing import List

from .search_comments_query import SearchCommentsQuery
from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository


class CommentsSearcher:
    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    def search(self, query: SearchCommentsQuery) -> List[Comment]:
        comments = self.repository.get_comments(**asdict(query))
        comments = Comment.sort(comments)
        return comments
