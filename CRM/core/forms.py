from django.forms import ModelForm, widgets

from .models import Sponsor
from .models import Event
from .models import Followup
from .models import Donation
from .models import Product
from .models import investigation_project

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = ['nit', 'name', 'type', 'mail', 'image']

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name','date','type','objective','description']
        widgets = {
            'name': widgets.TextInput(attrs = {'class': 'form-control'}),

            'date': widgets.DateInput(attrs = {
                'type': 'date',
                'class': 'form-control'
                }),

            'type': widgets.Select(attrs = {'class': 'form-control'}),
            'objective': widgets.Textarea(attrs = {
                'class': 'form-control',
                'rows': '3'
                }),
                
            'description': widgets.Textarea(attrs = {
                'class': 'form-control',
                'rows': '3'
                }),
        }

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }
        exclude = ("sponsor",)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("project",)

class FollowupForm(ModelForm):
    class Meta:
        model = Followup
        exclude = ("event_id",)
        widgets = {
            'name': widgets.TextInput(attrs = {'class': 'form-control'}),

            'description': widgets.Textarea(attrs = {
                'class': 'form-control',
                'rows': '2'
                }),

        }
        
class investigation_project_form(ModelForm):
    class Meta:
        model = investigation_project
        fields = ['name','description','objectives','start_date','finish_date','sponsors']
        widgets = {
            'start_date': widgets.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            'finish_date': widgets.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        finish_date = cleaned_data.get('finish_date')

        if start_date and finish_date:
            if finish_date <= start_date:
                self.add_error('finish_date', 'La fecha de finalización debe ser posterior a la fecha de inicio.')

        return cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Modificar la etiqueta del campo sponsors para mostrar el nombre en lugar del NIT
        self.fields['sponsors'].label_from_instance = lambda obj: f"{obj.name} ({obj.nit})"