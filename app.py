import os

from flask_cors import CORS

env = os.environ.get('FLASK_ENV')

if env == 'development':
    from containers.dev_container import DevAppContainer
    container = DevAppContainer()

else:
    from containers.prod_container import ProdApplicationContainer
    container = ProdApplicationContainer()


app = container.app()
app.container = container

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
    methods=('POST',)
)
