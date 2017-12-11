from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from controlgastos.models import Categoria, Cuenta, Usuario, Movimiento
from controlgastos.serializers import CategoriaSerializer, CuentaSerializer, UsuarioSerializer, MovimientoSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Recurso Cuenta utilizando class based views
class CuentaList(generics.ListCreateAPIView):
    """
    Listado y creacion de cuenta
    """
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer


class CuentaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtencion, modificacion y eliminacion de una cuenta
    """
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

#Recurso Usuario utilizando class based views
class UsuarioList(generics.ListCreateAPIView):
    """
    Listado y creacion de usuarios
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(APIView):
    """
    Obtencion, modificacion y eliminacion de un usuario
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        if Movimiento.objects.filter(usuario=usuario):
            usuario.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            usuario.hard_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

#Recurso Categoria utilizando class based views
class CategoriaList(generics.ListCreateAPIView):
    """
    Listado y creacion de cateogorias
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtencion, modificacion y eliminacion de una categoria
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def usuarios_cuenta(request,pk):
    """
    Lista los usuarios de una cuenta
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Cuenta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        usuarios = Usuario.objects.filter(cuenta=cuenta.id)
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def categorias_cuenta(request,pk):
    """
    Lista las categorias de una cuenta
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Cuenta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        categorias = Categoria.objects.filter(cuenta=cuenta.id)
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)

#Recurso Movimiento utilizando class based views
class MovimientoList(generics.ListCreateAPIView):
    """
    Listado y creacion de movimientos
    """
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class MovimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Obtencion, modificacion y eliminacion de un movimiento
    """
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

@api_view(['GET'])
def movimientos_usuario(request,pk):
    """
    Lista los movimientos de un usuario
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        movimientos = Movimiento.objects.filter(usuario=usuario.id)
        serializer = MovimientoSerializer(movimientos, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def movimientos_categoria(request,pk):
    """
    Lista los movimientos de una categoria
    """
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        movimientos = Movimiento.objects.filter(categoria=categoria.id)
        serializer = MovimientoSerializer(movimientos, many=True)
        return JsonResponse(serializer.data, safe=False)
