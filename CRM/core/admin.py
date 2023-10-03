from django.contrib import admin

from .models import Sponsor, Event, Donation

# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Event)
admin.site.register(Donation)
