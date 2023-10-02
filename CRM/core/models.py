from django.db import models
# Create your models here.

class Sponsor(models.Model):
    nit = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    types=(
        ('natural', "NATURAL"),
        ('juridica', "JURIDICA")
    )
    type = models.CharField(max_length=10,choices=types,default="natural")
    mail = models.EmailField(max_length=200)
    initial_donation = models.DecimalField(max_digits=19, decimal_places=3)
    status = "active"


class Event(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField()
    types=(
        ('Florecimiento', "FLORECIMIENTO"),
        ('Organizacional', "ORGANIZACIONAL")
    )
    type = models.CharField(max_length = 20, choices = types, default = "florecimiento")
    objective = models.TextField(blank = True)
    description = models.TextField(blank = True)

class Followup(models.Model):
    name = models.CharField(max_length = 50, null=False)
    description = models.TextField(blank = True)
    event_id = models.ForeignKey(Event, on_delete = models.CASCADE)

