from django.shortcuts import render

# Create your views here.
from .models import Goleadores, Asistidores, Rojas, amarillas
from django.http import HttpResponse
from LigaFc.forms import GoleadoresForms, AsistidoresForms, RojasForms, amarillasForms 
# Create your views here.


def inicio(request):
    return render (request, "LigaFc/inicio.html")

"""def amarillas(request):
    return render (request, "LigaFc/amarillas.html")"""

def Asistidores(request):
    return render (request, "LigaFc/Asistidores.html")

def Goleadores(request):
    return render (request, "LigaFc/Goleadores.html")

def Rojas(request):
    return render (request, "LigaFc/Rojas.html")



def Goleadores(request):
    if request.method=="POST":
        form=GoleadoresForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            goles=informacion["goles"]
            goleador=Goleadores(nombre=nombre, apellido=apellido, club=club, goles=goles)
            goleador.save()
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=GoleadoresForms()
        return render (request, "LigaFc/Goleadores.html", {"formulario":formulario})

def amarillas(request):
    if request.method=="POST":
        form=amarillasForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            amarillas=informacion["amarillas"]
            amarillas_validas=amarillas(nombre=nombre, apellido=apellido, club=club, amarillas=amarillas)
            amarillas_validas.save()
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=amarillasForms()
        return render (request, "LigaFc/amarillas.html", {"formulario":formulario})


def Asistidores(request):

    if request.method=="POST":
        form=AsistidoresForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            asistencias=informacion["asistencias"]
            Asistencias=Asistidores(nombre=nombre, apellido=apellido, club=club, asistencias=asistencias)
            Asistencias.save()
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=AsistidoresForms()
        return render (request, "LigaFc/Asistencias.html", {"formulario":formulario})


def Rojas(request):
    if request.method=="POST":
        form=RojasForms(request.POST)
       
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            rojas=informacion["rojas"]
            Roja=roja(nombre=nombre, apellido=apellido, club=club, rojas=rojas)
            Roja.save()
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=RojasForms()
        return render (request, "LigaFc/Rojas.html", {"formulario":formulario})



def busquedaclub(request):
    return render(request, "LigaFc/busquedaclub.html")
    

    
def buscar(request):
    if request.GET["club"]:

        nombres=request.GET["club"]
        #traeme de la base, TODOS los jugadores del club
        clubes=club.objects.filter(club=club)
        return render(request, "LigaFc/resultadosBusqueda.html", {"club":"club"})
    else:
        return render(request, "LigaFc/busquedaclub.html", {"mensaje":"Por favor ingresa un club!"})
    
    return HttpResponse(respuesta)