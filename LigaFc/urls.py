
from django.urls import path
from LigaFc.views import *

urlpatterns = [
    path("", Inicio, name="inicio"),
    path("amarillas/", Amarillas, name="amarillas"),
    path("Asistencias/", Asistencias, name="Asistencias"),
    path("Rojas/", Rojas, name="Rojas"),
    path("Goleadores/", Goleadores, name="Goleadores"),
    path("buscar/", Buscar, name="buscar"),
    path("busquedaclub/", Busquedaclub, name="busquedaclub"),
    

    
]