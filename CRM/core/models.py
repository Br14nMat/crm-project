from django.db import models

# Create your models here.
class InvestigationProyect(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    description = models.TextField()
    objetivos = models.TextField()
    start_date= models.DateField()
    finish_date= models.DateField()
    nit= models.IntegerField()

    def __str__(self):
        return self.name