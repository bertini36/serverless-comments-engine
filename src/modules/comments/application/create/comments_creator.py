from dataclasses import asdict

from .create_comment_command import CreateCommentCommand
from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository


class CommentsCreator:
    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    def create(self, command: CreateCommentCommand):
        comment = Comment(**asdict(command))
        self.repository.add_comment(comment)
