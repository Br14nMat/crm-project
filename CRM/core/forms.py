from django.forms import ModelForm, widgets
from .models import investigation_project

class investigation_project_form(ModelForm):
    class Meta:
        model = investigation_project
        fields = ['name','description','objectives','start_date','finish_date','nit']