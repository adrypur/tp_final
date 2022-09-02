
from django.urls import path
from LigaFc.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("Amarillas/", Amarillas, name="Amarillas"),
    path("Asistidores/", Asistidores, name="Asistidores"),
    path("Rojas/", Rojas, name="Rojas"),
    path("Goleadores/", Goleadores, name="Goleadores"),
    path("buscar/", buscar, name="buscar"),
    path("busquedaclub/", busquedaclub, name="busquedaclub"),
    

    
]