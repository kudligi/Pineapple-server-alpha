import graphene
from graphene_django import DjangoObjectType

from contests.models import Contest


class ContestType(DjangoObjectType):
    class Meta:
        model = Contest

class Query(graphene.ObjectType):
    contests = graphene.List(ContestType)

    def resolve_contests(self, info, **kwargs):
        return Contest.objects.all() 

