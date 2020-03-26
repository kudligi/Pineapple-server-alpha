import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType

from .models import Team


class TeamType(DjangoObjectType):
    class Meta:
        model = Team

class Query(graphene.ObjectType):
    teams = graphene.List(TeamType)

    def resolve_teams(self, info, **kwargs):
        return Team.objects.all()

    # def resolve_my_teams(self, info, **kwargs):
        


class createTeam(graphene.Mutation):
    name = graphene.String()
    owner  = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        user = info.context.user or None

        team = Team(
            name = name,
            owner = user,
        )

        team.save()

        return createTeam(
            name = team.name,
            owner = team.owner
        )

class Mutation(graphene.ObjectType):
    create_team = createTeam.Field()