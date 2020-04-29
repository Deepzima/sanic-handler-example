from sanic import Sanic
from sanic.response import json
from server.apis import default
from server.apis import graph


def create_app(env=None):
    from server.config import config_by_name

    app = Sanic("sanic-hoe")
    app.config.from_object(config_by_name[env or "dev"])
    app.blueprint(default.base_bp)
    app.blueprint(default.bp)
    app.blueprint(graph.bp)
    
    return app
