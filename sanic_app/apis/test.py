from sanic.response import json
from sanic import Blueprint
from sanic.views import HTTPMethodView

bp = Blueprint('test', url_prefix="/test")

class AsTest(HTTPMethodView):
    async def get(self, request):
        return json({"msg":"i am the get method"})

bp.add_route(AsTest.as_view(),'/')





