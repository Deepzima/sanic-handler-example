from time import time
from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.exceptions import SanicException
from server.config import logger as l
# from sanic_app.config import logger as l


bp = Blueprint('default', url_prefix="/sys")
base_bp = Blueprint('base', url_prefix="/")


@base_bp.exception(SanicException)
def page_not_found(request, error):
    # print(request.headers)
    # print(error)
    l.error(error)
    return json(
        status=404,
        body={"msg":"Route not available"}
    )



class Ping(HTTPMethodView):
    async def get(self, request):
        return json(
            body={"msg":"Yes, we've a Ping-Pong"}
            )
    async def post(self, request):
        return json(
            body={"msg": "pong at ep {}".format(time())}
            )

bp.add_route(Ping.as_view(),'/')





