import os

import pytest

from src.app import create_app
from src.containers.test_container import TestAppContainer


@pytest.fixture
def app():
    container = TestAppContainer()
    app = create_app(container)
    return app


def pytest_unconfigure(config):
    os.remove('src/data/test_comments.json')
