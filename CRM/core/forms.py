from django.forms import ModelForm, widgets
from .models import Sponsor
from .models import Event
from .models import Donation
from .models import Product

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
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

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['description','type']

