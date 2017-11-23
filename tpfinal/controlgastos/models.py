from django.db import models


class Cuenta(models.Model):
    nombre = models.CharField(max_length=200)


class Usuario(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE) #Verificar relaciones y si hay que usar cascadeo

'''
class Movimiento(models.Model):
    #Verificar relaciones con Usuario y Categoria
    fecha = models.DateTimeField('fecha')
    usuario = models.ForeignKey(Usuario)
    monto = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria)
    descripcion = models.CharField(max=500)
'''

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default="")


#Todavia no hice las migraciones hasta verificar bien las cosas que estan marcadas

#INSTALLED APPS
