from sanic import Sanic
from sanic.response import json
from apis import test
from apis import graph


def create_app(config):

    app = Sanic()
    app.config.from_pyfile(config)
    app.blueprint(test.bp)
    app.blueprint(graph.bp)
    
    return app
