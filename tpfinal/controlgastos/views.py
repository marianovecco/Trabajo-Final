from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from controlgastos.models import Categoria, Cuenta, Usuario, Movimiento
from controlgastos.serializers import CategoriaSerializer, CuentaSerializer, UsuarioSerializer, MovimientoSerializer
from rest_framework import generics

@csrf_exempt
@api_view(['GET', 'POST'])
def categoria_list(request):
    """
    Listado y creacion de las categorias
    """
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT','PATCH','DELETE'])
def categoria_detail(request, pk):
    """
    Obtencion, modificacion y eliminacion de una categoria
    """
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = CategoriaSerializer(categoria,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        categoria.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def cuenta_list(request):
    """
    Listado y creacion de las cuentas
    """
    if request.method == 'GET':
        cuentas = Cuenta.objects.all()
        serializer = CuentaSerializer(cuentas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CuentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT','PATCH','DELETE'])
def cuenta_detail(request, pk):
    """
    Obtencion, modificacion y eliminacion de una cuenta
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Cuenta.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CuentaSerializer(cuenta)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CuentaSerializer(cuenta, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = CuentaSerializer(cuenta,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cuenta.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def usuario_list(request):
    """
    Listado y creacion de los usuarios
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT','PATCH','DELETE'])
def usuario_detail(request, pk):
    """
    Obtencion, modificacion y eliminacion de un usuario
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)

@api_view(['GET'])
def usuarios_cuenta(request,pk):
    """
    Lista los usuarios de una cuenta
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Usuario.DoesNotExist:
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
    except Usuario.DoesNotExist:
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
