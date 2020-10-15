import os

import sentry_sdk
from dependency_injector import containers
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration

from .containers.dev_container import DevAppContainer

env = os.environ.get('FLASK_ENV')
sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    environment=env,
)


def get_container(env: str) -> containers.DeclarativeContainer:
    container = DevAppContainer()
    if env == 'production':
        from src.containers import ProdApplicationContainer
        container = ProdApplicationContainer()
    return container


def create_app(container):
    app = container.app()
    app.container = container
    app.debug = True
    app.add_url_rule(
        '/comments/<string:post_slug>',
        view_func=container.get_comments_view.as_view(),
        methods=('GET',),
    )
    app.add_url_rule(
        '/comments/<string:post_slug>',
        view_func=container.add_comment_view.as_view(),
        methods=('POST', 'OPTIONS'),
    )
    return app


container = get_container(env)
app = create_app(container)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
