from django.shortcuts import render, redirect
from .forms import SponsorForm
from .forms import EventForm
from .forms import DonationForm
from .models import Event
from .models import Sponsor


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
    return render(request, "event_info.html", {
        "event": event
    })

def add_donation(request, nit):
    sponsor = Sponsor.objects.get(nit=nit)
    form= DonationForm()
    print(sponsor)
    if request.method == 'POST': 
        try: 
                form = DonationForm(request.POST)
                donation = form.save(commit=False)
                donation.sponsor = sponsor
                donation.save()
                print(sponsor)
                return redirect('home')
        except ValueError:
            print("Please provide valid data")
            context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
            return render(request, 'add_donation.html', context)
    
    context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
    return render(request, 'add_donation.html', context)


