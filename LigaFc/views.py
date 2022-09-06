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
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            goles=informacion["goles"]
            goleador=GLS(nombre=nombre, apellido=apellido, club=club, goles=goles)
            goleador.save()
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
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            amarillas=informacion["amarillas"]
            amonestado=YELLOW(nombre=nombre, apellido=apellido, club=club, amarillas=amarillas)
            amonestado.save()
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
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            asistencias=informacion["asistencias"]
            asistidor=ASIST(nombre=nombre, apellido=apellido, club=club, asistencias=asistencias)
            asistidor.save()
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
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            club=informacion["club"]
            rojas=informacion["rojas"]
            Roja=RED(nombre=nombre, apellido=apellido, club=club, rojas=rojas)
            Roja.save()
            return render (request, "LigaFc/inicio.html")

    else:
        formulario=RojasForms()
        return render (request, "LigaFc/Rojas.html", {"formulario":formulario})



def Busquedaclub(request):
    return render(request, "LigaFc/busquedaclub.html")
    

    
def Buscar(request):
    if request.GET["club"]:

        nombres=request.GET["club"]
        #traeme de la base, TODOS los jugadores del club
        clubes=club.objects.filter(club=club)
        return render(request, "LigaFc/resultadosBusqueda.html", {"club":"club"})
    else:
        return render(request, "LigaFc/busquedaclub.html", {"mensaje":"Por favor ingresa un club!"})
    
    return HttpResponse(respuesta)