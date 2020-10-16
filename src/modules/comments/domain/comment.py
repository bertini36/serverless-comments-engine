from datetime import datetime
from operator import attrgetter
from typing import List, Union

from .exceptions import InvalidDataError


class Comment:
    def __init__(
        self, post_slug: str,
        name: str,
        email: str,
        text: str,
        date: Union[datetime, str] = None
    ):
        self.post_slug = post_slug
        self.name = name
        self.email = email
        self.text = text
        self.date = self.get_date(date)

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
            'date': str(self.date),
        }

    @classmethod
    def sort(cls, comments: List['Comment']) -> List['Comment']:
        return list(sorted(comments, key=attrgetter('date')))

    @staticmethod
    def get_date(date: Union[datetime, str] = None):
        if not date:
            return datetime.now()
        elif isinstance(date, str):
            return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        return date
