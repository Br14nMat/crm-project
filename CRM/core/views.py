from django.shortcuts import render, redirect
from .forms import InvestigationProyectForm
# Create your views here.

def agregarProyecto(request):
    if request.method == "POST":
        form = InvestigationProyectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = InvestigationProyectForm()
    return render(request, 'agregar_proyecto.html', {"form": form})    

        

