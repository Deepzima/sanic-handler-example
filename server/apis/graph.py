from sanic import Blueprint
from sanic_graphql import GraphQLView
# from server.resolvers import schema_test
# from server.resolvers.user.user import user_schema

from server.apis.grapql.resolvers.user import user_schema


bp = Blueprint('graph', url_prefix='/graph')


bp.add_route(GraphQLView.as_view(schema=user_schema, graphiql=True), '/graphql/user')
bp.add_route(GraphQLView.as_view(schema=user_schema, batch=True), '/graphql/user/batch')

