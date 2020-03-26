from django.db import models

# Create your models here.
class Contest(models.Model):
    name = models.TextField()
    start_time = models.DateTimeField(auto_now=True, blank=True)
    capacity = models.IntegerField(default=10)
    tickets_remaining = models.IntegerField(default=10)

