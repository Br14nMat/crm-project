from django.shortcuts import render, redirect
from .forms import SponsorForm
from .forms import EventForm

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