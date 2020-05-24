from graphene import ObjectType, String, Boolean



class ProfileSchema(ObjectType):
    """
    Profile Schema defining the types and relationship between Fields in your
    API.
    """
    _id = String(required=True)
    username = String(required=True)
    # password = String(required=True)
    name = String()
    email = String()
