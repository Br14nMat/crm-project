from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateTimeField()
    objective = models.TextField(blank = True)
    description = models.TextField(blank = True)