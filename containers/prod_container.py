from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask

from entrypoints.infrastructure import controllers
from modules.comments.infrastructure.repository.dynamo_comments_repository import (
    DynamoCommentsRepository,
)


class ProdApplicationContainer(containers.DeclarativeContainer):
    app = flask.Application(Flask, __name__)

    comments_repository = providers.Factory(DynamoCommentsRepository)

    get_comments_view = flask.View(
        controllers.get_comments, comments_repository=comments_repository
    )
    add_comment_view = flask.View(
        controllers.add_comment, comments_repository=comments_repository
    )
