from sanic import Blueprint
from sanic_graphql import GraphQLView
from server.resolvers import schema_test
from server.resolvers.user.user import user_schema


bp = Blueprint('graph', url_prefix='/graph')


bp.add_route(GraphQLView.as_view(schema=schema_test, graphiql=True), '/graphql/test')
bp.add_route(GraphQLView.as_view(schema=schema_test, batch=True), '/graphql/test/batch')

bp.add_route(GraphQLView.as_view(schema=schema_test, graphiql=True), '/graphql/user')
bp.add_route(GraphQLView.as_view(schema=schema_test, batch=True), '/graphql/user/batch')

