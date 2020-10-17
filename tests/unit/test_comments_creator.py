import pytest

from src.modules.comments.application.create.comments_creator import (
    CommentsCreator,
)
from src.modules.comments.application.create.create_comment_command import (
    CreateCommentCommand
)
from src.modules.comments.domain.exceptions import InvalidDataError
from src.modules.comments.infrastructure.repository.inmemory_comments_repository import (  # noqa
    InMemoryCommentsRepository,
)
from ..conftest import IN_MEMORY_COMMENTS_PATH

repository = InMemoryCommentsRepository(IN_MEMORY_COMMENTS_PATH)


def test_create_comment():
    command = CreateCommentCommand(
        post_slug='dummy',
        name='John Doe',
        email='john@doe.com',
        text='Ouh mama',
    )
    CommentsCreator(repository).create(command)


def test_create_comment_with_validation_error():
    command = CreateCommentCommand(
        post_slug='dummy', name='', email='john@doe.com', text='Ouh mama'
    )

    with pytest.raises(InvalidDataError):
        CommentsCreator(repository).create(command)
