from django.forms import ModelForm, widgets

from .models import Sponsor
from .models import Event
from .models import Followup
from .models import Donation
from .models import investigation_project

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'

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

        fields = ['value','date','type']

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
        fields = ['name','description','objectives','start_date','finish_date','nit']
