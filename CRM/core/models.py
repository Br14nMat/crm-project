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
    initialDonation = models.DecimalField(max_digits=19, decimal_places=3)
    status = "active"
