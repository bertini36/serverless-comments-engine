import os

import sentry_sdk
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration

from containers.dev_container import DevAppContainer

env = os.environ.get('FLASK_ENV')

container = DevAppContainer()

if env == 'production':
    from containers.prod_container import ProdApplicationContainer
    container = ProdApplicationContainer()

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    environment=env,
)

app = container.app()
app.container = container
app.debug = True

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.add_url_rule(
    '/comments/<string:post_slug>',
    view_func=container.get_comments_view.as_view(),
    methods=('GET',)
)
app.add_url_rule(
    '/comments/<string:post_slug>',
    view_func=container.add_comment_view.as_view(),
    methods=('POST', 'OPTIONS')
)
