from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask

from entrypoints.infrastructure import controllers
from modules.comments.infrastructure.repository.inmemory_comments_repository import (
    InMemoryCommentsRepository
)


class DevAppContainer(containers.DeclarativeContainer):
    app = flask.Application(Flask, __name__)

    # InMemory repository is used in development to avoid use Dynamo AWS
    comments_repository = providers.Factory(InMemoryCommentsRepository)

    get_comments_view = flask.View(
        controllers.get_comments,
        comments_repository=comments_repository
    )
    add_comment_view = flask.View(
        controllers.add_comment,
        comments_repository=comments_repository
    )
