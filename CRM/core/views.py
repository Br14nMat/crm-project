from django.shortcuts import render, redirect
from .forms import SponsorForm

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
