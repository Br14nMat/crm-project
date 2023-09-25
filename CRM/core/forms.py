from django import forms
from .models import InvestigationProyect

class InvestigationProyectFrom(forms.ModelForm):
    class Meta:
        model = InvestigationProyect
        fields = ['name','description','objetivos','start_date','finish_date','nit']