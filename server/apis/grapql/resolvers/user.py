from graphene import ObjectType, Schema, String 





class Query(ObjectType):
    hello = String(description="")

    def resolve_hello(self, info):
        return "World"


user_schema = Schema(query=Query)