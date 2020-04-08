from sanic import Blueprint
from sanic_graphql import GraphQLView
from resolvers import schema_test


bp = Blueprint('graph', url_prefix='/graph')


bp.add_route(GraphQLView.as_view(schema=schema_test, graphiql=True), '/graphql')
bp.add_route(GraphQLView.as_view(schema=schema_test, batch=True), '/graphql/batch')

