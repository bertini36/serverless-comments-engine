from datetime import datetime
from typing import List

from .exceptions import InvalidDataError


class Comment:

    def __init__(
        self,
        post_slug: str,
        name: str,
        email: str,
        text: str,
        date: str = None
    ):
        self.post_slug = post_slug
        self.name = name
        self.email = email
        self.text = text
        self.date = date if date else str(datetime.now())
        self.validate()

    def validate(self):
        if self.name == '':
            raise InvalidDataError('Name is required')
        if self.email == '':
            raise InvalidDataError('Email is required')
        if '@' not in self.email:
            raise InvalidDataError('Specify a correct email')
        if self.text == '':
            raise InvalidDataError('Text is required')

    def serialize(self):
        return {
            'post_slug': self.post_slug,
            'name': self.name,
            'email': self.email,
            'text': self.text,
            'date': self.date
        }

    @classmethod
    def sort(cls, comments: List['Comment']) -> List['Comment']:
        return list(sorted(
            comments,
            key=lambda comment: datetime.strptime(
                comment.date,
                '%Y-%m-%d %H:%M:%S.%f'
            )
        ))
