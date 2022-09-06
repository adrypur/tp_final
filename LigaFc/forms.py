from django import forms

class GoleadoresForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    club=forms.CharField(max_length=50)
    goles=forms.IntegerField()

    


class AsistenciasForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    club=forms.CharField(max_length=50)
    asistencias=forms.IntegerField()

   

class RojasForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    club=forms.CharField(max_length=50)
    rojas=forms.IntegerField()

    


class AmarillasForms(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    club=forms.CharField(max_length=50)
    amarillas=forms.IntegerField()

    