"""
URL configuration for crm_module project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.signin, name = 'login'),
    path('home/', auth_views.home, name = 'home'),
    path('signup/', auth_views.signup, name = 'signup'),
    path('signin/', auth_views.signin, name = 'signin'),
    path('signout/', auth_views.signout, name = 'signout'),
    path("project/add", core_views.add_project, name='add_project'),
    path('sponsor/register', core_views.register_sponsor, name = 'register_sponsor'),
    path('sponsor/edit', core_views.edit_sponsor, name = 'edit_sponsor'),
    path('sponsor/all', core_views.list_sponsors, name = 'list_sponsors'),
    path('event/register', core_views.create_event, name = 'create event'),
    path('event/all', core_views.list_event, name = 'list event'),
    path('event/delete/<int:id>', core_views.delete_event, name = 'delete event'),
    path('event/info/<int:id>', core_views.show_event, name = 'show event information'),
    path('event/info/<int:eventId>/remove_sponsor/<int:sponsorId>', core_views.remove_sponsor, name = 'show event information'),
    path('project/product/add/<int:id>', core_views.add_product, name = 'add_product'),
    path('sponsor/donation/add', core_views.add_donation, name = 'add_donation'),
    path('event/info/followup/delete/<int:eventId>/<int:followupId>', core_views.delete_followup, name = 'show event information'),
    path('project/product/all/<int:id>', core_views.list_product, name='list_product'),
    path('project/product/edit', core_views.edit_product, name='edit_product'),
    path('project/product/delete', core_views.delete_product, name='delete_product'),
    path('sponsor/report/<int:id>', core_views.sponsor_report, name = 'sponsor report'),
    path('sponsor/report', core_views.general_report, name = 'general report'),
    path('project/delete/<int:id>', core_views.delete_project, name="delete_project"),
    path('project/all', core_views.project_list, name= 'project_list'),
    path('project/edit/<int:id>', core_views.edit_project, name= 'edit_project'),
    path('event/calendar', core_views.calendar ,name= 'show_calendar'),
    path('event/calendar/events', core_views.list_event_day ,name= 'show_events_calendar'),
    path('event/info/<int:id>/sponsors/<str:sponsor_name>', core_views.get_sponsors_by_name_event, name = 'show event sponsors'),
    path('project/edit/<int:id>/sponsors/<str:sponsor_name>', core_views.get_sponsors_by_name_project, name= 'show project sponsors')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
