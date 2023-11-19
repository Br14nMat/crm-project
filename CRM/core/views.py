from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import SponsorForm
from .forms import EventForm
from .forms import DonationForm
from .forms import ProductForm
from .forms import FollowupForm
from .forms import investigation_project_form
from .models import Event
from .models import Sponsor
from .models import Followup
from .models import investigation_project
from .models import Product

def register_sponsor(request):
    form= SponsorForm()
    try:
        if request.method == 'POST':
            print(request.POST)
            form= SponsorForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('list_sponsors')
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
                return redirect('list_sponsors')
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
            return redirect('list event')
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
    
    referer = request.META.get('HTTP_REFERER', None)
    print(referer)

    if referer:
        if 'event/all' in referer:
            return redirect("/event/all")
        elif 'event/calendar' in referer:
            return redirect("/event/calendar")


def show_event(request, id):    
    event = Event.objects.get(id = id)
    followups = Followup.objects.filter(event_id = id)
    form = FollowupForm()
    usable_sponsors=[]
    used_sponsors=[]
    for sponsor in Sponsor.objects.all():
        if event.sponsors.filter(nit=sponsor.nit).exists():
            used_sponsors.append(sponsor)
        else: usable_sponsors.append(sponsor)
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
                selected_nit= request.POST.get('link_sponsor', None)
                sponsor = Sponsor.objects.get(nit=selected_nit)
                event.sponsors.add(sponsor)
                sponsor.events.add(event)
                return redirect("/event/info/"+str(id))
            if request.POST.get('filter_sponsors'):
                sponsor_name = request.POST.get('sponsor_name', '')
                sponsors=Sponsor.objects.filter(name__istartswith=sponsor_name)
                return render(request, "event_info.html", {
                    "event": event,
                    "followups": followups,
                    "form": form,
                    "sponsors" : sponsors,
                    "event_sponsors" : used_sponsors})
            
    except ValueError:
        return render(request, 'event_info.html', {
            'form': FollowupForm,
            'error': 'Please provide valid data'
            })
    
    return render(request, "event_info.html", {
        "event": event,
        "followups": followups,
        "form": form,
        "sponsors" : usable_sponsors,
        "event_sponsors" : used_sponsors
    })

def add_product(request, id):
    #id = request.session.get('selectedID', -1)
    project = investigation_project.objects.get(id=id)
    form= ProductForm()
    if request.method == 'POST': 
        try: 
            form = ProductForm(request.POST)
            if form.is_valid():
                product = form.save(commit=False)
                product.project = project
                product.save()
                #del request.session['selectedID']
                return redirect('list_product',id)
        except ValueError:
            print("Please provide valid data")
            context = {'form': form, 'project': project,'error': 'Please provide valid data'}
            return render(request, 'add_product.html', context)
    else:
        context = {'form': form, 'project': project,'error': 'Please provide valid data'}
    return render(request, 'add_product.html', context)

def delete_followup(request, eventId, followupId):
    followup = Followup.objects.get(id = followupId)
    followup.delete()
    return redirect("/event/info/"+str(eventId))

def remove_sponsor(request, eventId, sponsorId):
    event = Event.objects.get(id = eventId)
    sponsor = Sponsor.objects.get(id = sponsorId)
    event.sponsors.remove(sponsor)
    sponsor.events.remove(event)
    return redirect("/event/info/"+str(eventId))

def add_project(request):
    if request.method == "POST":
        form = investigation_project_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = investigation_project_form()
    return render(request, 'add_project.html', {"form": form})    

def list_product(request,id):
    project = investigation_project.objects.get(id=id)
    products = Product.objects.filter(project=project)
    used_sponsors=[]
    usable_sponsors=[]
    for sponsor in Sponsor.objects.all():
        if project.sponsors.filter(nit=sponsor.nit).exists():
            used_sponsors.append(sponsor)
        else: usable_sponsors.append(sponsor)
    if request.method == 'GET':
        return render(request, "list_products.html", {
            "products": products,
            "project" : project,
            "project_sponsors" : used_sponsors
        })
    if request.method == 'POST':
        if request.POST.get('delete_product'):
            id_product = request.POST.get('delete_product', None)
            request.session['selectedID']=id_product
            return redirect('delete_product')
        if request.POST.get('edit_product'):
            id_product = request.POST.get('edit_product', None)
            request.session['selectedID']=id_product
            return redirect('edit_product')

def edit_product(request):
    id_product = request.session.get('selectedID', -1)
    product = Product.objects.get(id = id_product)
    id_project = product.project.id
    form = ProductForm(instance=product)
    
    if request.method=='POST':
        if request.POST.get('edit'):
            form = ProductForm(request.POST,instance=product)
            edited_product = form.save(commit=False)
            edited_product.save()
            del request.session['selectedID']
            return redirect('list_product', id_project)
    return render(request, 'edit_product.html', {"form":form, "product":product})

def delete_product(request):
    id_product = request.session.get('selectedID', -1)
    product = Product.objects.get(id = id_product)
    id_project = product.project.id
    product.delete()
    del request.session['selectedID']
    return redirect('list_product', id_project)

def sponsor_report(request, id):
    sponsor = Sponsor.objects.get(id = id)
    donations = sponsor.donations.all()
    projects = sponsor.projects.all()

    num_donations = sponsor.donations.count()
    num_projects = sponsor.projects.count()
    
    total_donated = sum(donation.value for donation in donations)

    return render(request, "sponsor_report.html", {
        "sponsor": sponsor,
        "donations": donations,
        "projects": projects,
        "num_donations": num_donations,
        "num_projects": num_projects,
        "total_donated": total_donated
    })

def general_report(request):
    sponsors = Sponsor.objects.all()
    total_donations = 0
    total_projects = 0
    total_donated = 0

    sponsor_donations = []
    sponsor_projects = []

    for sponsor in sponsors:
        donations = sponsor.donations.all()
        total_donations += sponsor.donations.count()
        total_projects += sponsor.projects.count()
        total_donated += sum(donation.value for donation in donations)
        sponsor_donations.append((sponsor, total_donated))
        sponsor_projects.append((sponsor, total_projects))

    ordered_by_donations = sorted(sponsor_donations, key=lambda x: x[1], reverse=True)
    ordered_by_projects = sorted(sponsor_projects, key=lambda x: x[1], reverse=True)

    return render(request, "general_report.html", {
        "total_donations": total_donations,
        "total_projects": total_projects,
        "total_donated": total_donated,
        "ordered_by_donations": ordered_by_donations,
        "ordered_by_projects": ordered_by_projects
    })

def delete_project(request, id):
    project= get_object_or_404(investigation_project, id=id)

    if request.method=='POST':
        project.delete()
        return redirect('project_list')
    
    return  render(request, 'delete_project.html', {'project': project})

def project_list(request):
    project= investigation_project.objects.all()
    return render(request, 'project_list.html', {'project':project})

def edit_project(request, id):
    if(request.session.get('project_id',-1)==-1):
        request.session['project_id']=id
    else:
        new_id=request.session.get('project_id',-1)
        if(id!=new_id):
            id=new_id
    project = get_object_or_404(investigation_project, id=id)
    form = investigation_project_form(instance=project) 
    usable_sponsors=[]
    used_sponsors=[]
    for sponsor in Sponsor.objects.all():
        if project.sponsors.filter(nit=sponsor.nit).exists():
            used_sponsors.append(sponsor)
        else: usable_sponsors.append(sponsor)

    if request.method=='POST':
        if request.POST.get('link_sponsor'):
                selected_nit= request.POST.get('link_sponsor', None)
                sponsor = Sponsor.objects.get(nit=selected_nit)
                project.sponsors.add(sponsor)
                sponsor.projects.add(project)
                for s in usable_sponsors:
                    if (s==sponsor):
                        used_sponsors.append(sponsor)
                        usable_sponsors.remove(sponsor)
                return render(request, 'edit_project.html', {'form':form, 'project':project, "sponsors" : usable_sponsors,"project_sponsors" : used_sponsors})
        else:
            form = investigation_project_form(request.POST, instance=project)
            if form.is_valid():
                form.save()
                del request.session['project_id']
                return redirect("project_list")
        
    return render(request, 'edit_project.html', {'form':form, 'project':project, "sponsors" : usable_sponsors,"project_sponsors" : used_sponsors})

def calendar(request):
    return render(request, "calendar.html")
    
from django.http import JsonResponse

def list_event_day(request):
    print(request.session.get('given_date', -1))
    #events = Event.objects.filter(date=given_date)
    events = Event.objects.all()
    if request.method == 'GET':
        data = [{"id": event.id,"name": event.name, "date": event.date,"description": event.description,"type":event.type} for event in events]
        return JsonResponse(data, safe=False)
    