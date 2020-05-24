import uuid
from graphene import ObjectType, Schema, String, Field

from server.apis.grapql.schemas.user import ProfileSchema





class Query(ObjectType):
    register = Field(ProfileSchema,
                     email=String(),
                     password=String(),
                     username=String(),
                     name=String())

    def resolve_register(self, info, email, password, username, name):
        print(email, password, username, name)

        generated_uuid = str(uuid.uuid1())
        profile_payload = {
            "_id": generated_uuid,
            "email": email.lower(),
            "password": password,
            "username": username,
            "name": name,
        }
        return profile_payload 


user_schema = Schema(query=Query, types=[ProfileSchema])