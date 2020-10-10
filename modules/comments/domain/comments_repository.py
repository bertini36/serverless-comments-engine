from abc import ABC, abstractmethod
from typing import List

from ..domain.comment import Comment


class CommentsRepository(ABC):

    @abstractmethod
    def get_comments(self, post_slug: str) -> List[Comment] or None:
        pass

    @abstractmethod
    def add_comment(self, comment: Comment):
        pass
