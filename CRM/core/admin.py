from django.contrib import admin

from .models import Sponsor, Event, Donation, investigation_project, Followup

# Register your models here.
admin.site.register(Sponsor)
admin.site.register(Event)
admin.site.register(Donation)
admin.site.register(investigation_project)
admin.site.register(Followup)
