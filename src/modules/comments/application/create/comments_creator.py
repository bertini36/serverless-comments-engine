from dataclasses import asdict

from .create_command import CreateCommand
from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository


class CommentsCreator:
    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    def create(self, command: CreateCommand):
        comment = Comment(**asdict(command))
        self.repository.add_comment(comment)
