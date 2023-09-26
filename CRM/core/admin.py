from django.contrib import admin

from .models import Sponsor, Event

# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Event)

