from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.TextField()
    ticker = models.TextField()
    industry = models.TextField(default='IT')
    isin_code = models.TextField(default='3421432XXX')