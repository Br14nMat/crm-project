from django.forms import ModelForm
from .models import Sponsor

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'