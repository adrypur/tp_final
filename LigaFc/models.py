from django.db import models


# Create your models here.

class Goleadores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    goles=models.IntegerField()

    def __str__(self):
        return self.nombre+""+str(self.club)


class Asistidores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    asistencias=models.IntegerField()

    def __str__(self):
        return self.nombre+""+str(self.club)


class Rojas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    rojas=models.IntegerField()

    def __str__(self):
        return self.nombre+""+str(self.club)


class Amarillas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    amarillas=models.IntegerField()

    def __str__(self):
        return self.nombre+""+str(self.club)    
