from rest_framework import serializers
from .models import Categoria, Cuenta, Usuario, Movimiento

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre','cuenta')

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('id', 'nombre')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'user','password','email','cuenta')

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = ('id', 'fecha','usuario','monto','categoria','descripcion')
