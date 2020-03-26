from django.db import models
from django.contrib.auth.models import User
from contests.models import Contest
from stocks.models import Stock

# Create your models here.
class Team(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.PROTECT, blank=True, null=True)
    stocks = models.ManyToManyField(Stock)
