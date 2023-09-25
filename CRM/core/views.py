from django.shortcuts import render, redirect
from .forms import InvestigationProyectFrom
# Create your views here.

def agregarProyecto(request):
    if request.method == "POST":
        form = InvestigationProyectFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = InvestigationProyectFrom()
    return render(request, 'agregar_proyecto.html', {"form": form})    

        

