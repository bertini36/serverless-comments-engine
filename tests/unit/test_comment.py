from datetime import timedelta

import pytest

from src.modules.comments.domain.comment import Comment
from src.modules.comments.domain.exceptions import InvalidDataError


def test_name_is_not_empty_validation():
    with pytest.raises(InvalidDataError) as e:
        Comment(
            post_slug='dummy',
            name='',
            email='john@doe.com',
            text='Ouh mama'
        )

    assert str(e.value) == 'Name is required'


def test_email_is_not_empty_validation():
    with pytest.raises(InvalidDataError) as e:
        Comment(
            post_slug='dummy',
            name='John',
            email='',
            text='Ouh mama'
        )

    assert str(e.value) == 'Email is required'


def test_email_is_not_an_email_validation():
    with pytest.raises(InvalidDataError) as e:
        Comment(
            post_slug='dummy',
            name='John',
            email='john',
            text='Ouh mama'
        )

    assert str(e.value) == 'Specify a correct email'


def test_text_is_not_empty_validation():
    with pytest.raises(InvalidDataError) as e:
        Comment(
            post_slug='dummy',
            name='John',
            email='john@doe.com',
            text=''
        )

    assert str(e.value) == 'Text is required'


def test_comment_seralization():
    comment = Comment(
        post_slug='dummy',
        name='John',
        email='john@doe.com',
        text='Ouh mama'
    )

    serialized_comment = comment.serialize()

    assert type(serialized_comment) is dict


def test_comments_sort():
    comment_1 = Comment(
        post_slug='dummy1',
        name='John',
        email='john@doe.com',
        text='Ouh mama'
    )
    comment_2 = Comment(
        post_slug='dummy2',
        name='John',
        email='john@doe.com',
        text='Ouh mama'
    )
    comment_2.date -= timedelta(days=1)
    comments = [comment_1, comment_2]

    ordered_comments = Comment.sort(comments)

    assert ordered_comments[0].post_slug == 'dummy2'
