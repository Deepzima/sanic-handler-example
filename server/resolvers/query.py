from graphene import ObjectType, Schema, String 





class Query(ObjectType):
    hello = String(description="Hello Zima?")

    def resolve_hello(self, info):
        return "World"


schema_test = Schema(query=Query)
