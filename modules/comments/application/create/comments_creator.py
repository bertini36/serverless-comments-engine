from ...domain.comment import Comment
from ...domain.comments_repository import CommentsRepository


class CommentsCreator:

    def __init__(self, repository: CommentsRepository):
        self.repository = repository

    def create(self, post_slug: str, name: str, email: str, text: str):
        comment = Comment(
            post_slug=post_slug,
            name=name,
            email=email,
            text=text
        )
        self.repository.add_comment(comment)
