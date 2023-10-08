from django.shortcuts import render, redirect
from .forms import investigation_project_form
# Create your views here.

def add_project(request):
    if request.method == "POST":
        form = investigation_project_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = investigation_project_form()
    return render(request, 'add_project.html', {"form": form})    

        

