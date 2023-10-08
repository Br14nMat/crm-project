from django.forms import ModelForm, widgets
from .models import InvestigationProyect

class InvestigationProyectForm(ModelForm):
    class Meta:
        model = InvestigationProyect
        fields = ['name','description','objetivos','start_date','finish_date','nit']