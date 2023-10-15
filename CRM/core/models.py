from django.db import models

# Create your models here.

class Sponsor(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    types=(
        ('natural', "NATURAL"),
        ('juridica', "JURIDICA")
    )
    type = models.CharField(max_length=10,choices=types,default="natural")
    mail = models.EmailField(max_length=200)
    initial_donation = models.DecimalField(max_digits=19, decimal_places=3)
    status = "active"

    def __str__(self): 
        return str(self.nit)

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
    sponsors = models.ManyToManyField(Sponsor, related_name='events')    

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

class Product(models.Model):
    #project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank = True)
    types = (
        ('Type1', "Type1"),
        ('Type2', "Type2"),
        ('Type3', "Type3")
    )
    type = models.CharField(max_length=20, choices=types, default="Type1")

class Followup(models.Model):
    name = models.CharField(max_length = 50, null=False)
    description = models.TextField(blank = True)
    event_id = models.ForeignKey(Event, on_delete = models.CASCADE)

class investigation_project(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    description = models.TextField()
    objectives = models.TextField()
    start_date= models.DateField()
    finish_date= models.DateField()
    nit= models.IntegerField()

    def __str__(self):
        return self.name
