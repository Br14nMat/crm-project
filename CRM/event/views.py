from django.shortcuts import render, redirect
from .forms import EventForm
# Create your views here.

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