from django.shortcuts import render

# Create your views here.
from .models import Goleadores as GLS, Asistencias as ASIST, Rojas as RED, Amarillas as YELLOW
from django.http import HttpResponse
from LigaFc.forms import AmarillasForms, AsistenciasForms, GoleadoresForms, AsistenciasForms, RojasForms
# Create your views here.


def Inicio(request):
    return render (request, "LigaFc/inicio.html")

"""def amarillas(request):
    return render (request, "LigaFc/amarillas.html")"""

"""def Asistidores(request):
    return render (request, "LigaFc/Asistidores.html")"""

"""def Goleadores(request):
    return render (request, "LigaFc/Goleadores.html")

def Rojas(request):
    return render (request, "LigaFc/Rojas.html")"""



def Goleadores(request):
    if request.method=="POST":
        form=GoleadoresForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            club=form.cleaned_data["club"]
            goles=form.cleaned_data["goles"]
            #goleador=GLS(nombre=nombre, apellido=apellido, club=club, goles=goles)
            form.save()
            print(form)
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=GoleadoresForms()
        return render (request, "LigaFc/Goleadores.html", {"formulario":formulario})

def Amarillas(request):
    if request.method=="POST":
        form=AmarillasForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            club=form.cleaned_data["club"]
            amarillas=form.cleaned_data["amarillas"]
            #amonestado=YELLOW(nombre=nombre, apellido=apellido, club=club, amarillas=amarillas)
            form.save()
            print(form)
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=AmarillasForms()
        return render (request, "LigaFc/Amarillas.html", {"formulario":formulario})


def Asistencias(request):
    if request.method=="POST":
        form=AsistenciasForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            club=form.cleaned_data["club"]
            asistencias=form.cleaned_data["asistencias"]
            #asistidor=ASIST(nombre=nombre, apellido=apellido, club=club, asistencias=asistencias)
            form.save()
            print(form)
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=AsistenciasForms()
        return render (request, "LigaFc/Asistencias.html", {"formulario":formulario})


def Rojas(request):
    if request.method=="POST":
        form=RojasForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            club=form.cleaned_data["club"]
            rojas=form.cleaned_data["rojas"]
            #Roja=RED(nombre=nombre, apellido=apellido, club=club, rojas=rojas)
            form.save()
            print(form)
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=RojasForms()
        return render (request, "LigaFc/Rojas.html", {"formulario":formulario})



def BusquedaGoleadores(request):
    return render(request, "LigaFc/BusquedaGoleadores.html")
    

    
def Buscar(request):
    if request.GET["Goleadores"]:

        nombres=request.GET["goleadores"]
        #traeme de la base, TODOS los goleadores
        Goleadores=GLS.objects.all(Goleadores=Goleadores)
        return render(request, "LigaFc/resultadosBusqueda.html", {"club":"club"})
    else:
        return render(request, "LigaFc/BusquedaGoleadores.html", {"mensaje":"Por favor ingresa un Goleador"})
    
    return HttpResponse(respuesta)