import graphene
import graphql_jwt
import stocks.schema
import users.schema
import contests.schema
import teams.schema

class Query(teams.schema.Query, contests.schema.Query ,stocks.schema.Query, users.schema.Query):
    pass

class Mutation(teams.schema.Mutation, users.schema.Mutation):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

