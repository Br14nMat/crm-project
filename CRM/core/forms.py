
from django.forms import ModelForm, widgets
from .models import Sponsor
from .models import Event
from .models import Donation



class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }

        fields = '__all__'

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }
        fields = ['value','date','type']

