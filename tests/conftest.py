import os

import pytest

from src.app import create_app
from src.containers.test_container import TestAppContainer

IN_MEMORY_COMMENTS_PATH = 'src/data/test_comments.json'


@pytest.fixture
def app():
    container = TestAppContainer()
    app = create_app(container)
    return app


def pytest_unconfigure(config):
    if os.path.exists(IN_MEMORY_COMMENTS_PATH):
        os.remove(IN_MEMORY_COMMENTS_PATH)
