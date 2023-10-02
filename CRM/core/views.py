from django.shortcuts import render, redirect
from .forms import SponsorForm
from .forms import EventForm
from .forms import FollowupForm
from .models import Event
from .models import Sponsor
from .models import Followup


def register_sponsor(request):
    form= SponsorForm()
    try:
        if request.method == 'POST':
            print(request.POST)
            form= SponsorForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')
    except ValueError:
        return render(request, 'create_event.html', {
            'form': SponsorForm,
            'error': 'Please provide valid data'
            })
    
    context = {'form':form}
    return render(request, 'register_sponsor.html',context)

def list_sponsors(request):
    sponsors = Sponsor.objects.all()
    if request.method == 'GET':
        return render(request, 'list_sponsors.html',{
            "sponsors":sponsors
        })
    

def create_event(request):

    if request.method == 'POST':
        try:
            form = EventForm(request.POST)
            new_form = form.save(commit = False)
            new_form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_event.html', {
            'form': EventForm,
            'error': 'Please provide valid data'
            })

    return render(request, 'create_event.html', {
        'form': EventForm
    })

def list_event(request):
    events = Event.objects.all()
    return render(request, "list_event.html", {
        "events": events
    })

def delete_event(request, id):
    event = Event.objects.get(id = id)
    event.delete()
    return redirect("/event/all")

def show_event(request, id):    
    event = Event.objects.get(id = id )
    followups = Followup.objects.filter(event_id = id)
    form = FollowupForm()
    try:
        if request.method == 'POST':
            print(request.POST)
            form = FollowupForm(request.POST)
            if form.is_valid():
                fol = form.save(commit=False)
                fol.event_id = event
                fol.save()
            return redirect('home')
    except ValueError:
        return render(request, 'event_info.html', {
            'form': FollowupForm,
            'error': 'Please provide valid data'
            })
    
    return render(request, "event_info.html", {
        "event": event,
        "followups": followups,
        "form": form
    })         

