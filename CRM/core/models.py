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

class Donation(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='donations')
    value = models.DecimalField(max_digits=19, decimal_places=3)
    date = models.DateField()
    types = (
        ('Type1', "Type1"),
        ('Type2', "Type2"),
        ('Type3', "Type3")
    )
    type = models.CharField(max_length=20, choices=types, default="Type1")


