from django.shortcuts import render, redirect
from .forms import SponsorForm
from .forms import EventForm
from .forms import DonationForm
from .forms import FollowupForm
from .models import Event
from .models import Sponsor
from .models import Followup
from .forms import investigation_project_form

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

def edit_sponsor(request):
    nit = request.session.get('selectedNIT', -1)
    sponsor=Sponsor.objects.get(nit=nit)
    form = SponsorForm(instance=sponsor)
    if request.method=='POST':
        if request.POST.get('edit'):
            form = SponsorForm(request.POST,instance=sponsor)
            edited_sponsor = form.save(commit=False)
            edited_sponsor.save()
            del request.session['selectedNIT']
            return redirect('list_sponsors')
        elif request.POST.get('change_status'):
            if sponsor.status=='activo':
                sponsor.status='inactivo'
            elif sponsor.status=='inactivo':
                sponsor.status='activo'
            sponsor.save()
            context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
            return render(request, 'edit_sponsor.html', context)

    else:
        context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
        return render(request, 'edit_sponsor.html', context)
    
def add_donation(request):
    nit = request.session.get('selectedNIT', -1)
    sponsor=Sponsor.objects.get(nit=nit)
    form= DonationForm()
    print(sponsor) 
    if request.method == 'POST': 
        try: 
            form = DonationForm(request.POST)
            if form.is_valid():
                donation = form.save(commit=False)
                donation.sponsor = sponsor
                donation.save()
                del request.session['selectedNIT']
                return redirect('home')
        except ValueError:
            print("Please provide valid data")
            context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
            return render(request, 'add_donation.html', context)
    else:
        context = {'form': form, 'sponsor': sponsor,'error': 'Please provide valid data'}
        return render(request, 'add_donation.html', context)

def list_sponsors(request):
    sponsors = Sponsor.objects.all()
    if request.method == 'GET':
        return render(request, 'list_sponsors.html',{
            "sponsors":sponsors
        })
    if request.method == 'POST':

        if request.POST.get('new_donation'):
            nit = request.POST.get('new_donation', None)
            request.session['selectedNIT']=nit
            return redirect('add_donation')

        if request.POST.get('nit'):
            nit = request.POST.get('nit', None)
            request.session['selectedNIT']=nit
            return redirect('edit_sponsor')
    

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
    event = Event.objects.get(id = id)
    followups = Followup.objects.filter(event_id = id)
    form = FollowupForm()
    usable_sponsors=[]
    for sponsor in Sponsor.objects.all():
        if not event.sponsors.filter(nit=sponsor.nit).exists():
            usable_sponsors.append(sponsor)
    try:
        if request.method == 'POST':
            if request.POST.get('followup'):
                print(request.POST)
                form = FollowupForm(request.POST)
                if form.is_valid():
                    fol = form.save(commit=False)
                    fol.event_id = event
                    fol.save()
                return redirect("/event/info/"+str(id))
            if request.POST.get('link_sponsor'):
                selected_nit= request.POST.get('nit', None)
                sponsor = Sponsor.objects.get(nit=selected_nit)
                event.sponsors.add(sponsor)
                sponsor.events.add(event)
                return redirect("/event/info/"+str(id))
    except ValueError:
        return render(request, 'event_info.html', {
            'form': FollowupForm,
            'error': 'Please provide valid data'
            })
    
    return render(request, "event_info.html", {
        "event": event,
        "followups": followups,
        "form": form,
        "sponsors" : usable_sponsors
    })

def delete_followup(request, eventId, followupId):
    followup = Followup.objects.get(id = followupId)
    followup.delete()
    return redirect("/event/info/"+str(eventId))
  
 

def add_project(request):
    if request.method == "POST":
        form = investigation_project_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = investigation_project_form()
    return render(request, 'add_project.html', {"form": form})    


