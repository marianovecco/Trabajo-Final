from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from controlgastos.models import Categoria, Cuenta, Usuario
from controlgastos.serializers import CategoriaSerializer, CuentaSerializer, UsuarioSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def categoria_list(request):
    """
    Lista o crea las categorias
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
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    """
    Hacer retrieve, update o delete de una categoria.
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

    elif request.method == 'DELETE':
        categoria.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def cuenta_list(request):
    """
    Lista o crea las cuentas
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
@api_view(['GET', 'PUT', 'DELETE'])
def cuenta_detail(request, pk):
    """
    Hacer retrieve, update o delete de una cuenta.
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

    elif request.method == 'DELETE':
        cuenta.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'POST'])
def usuario_list(request):
    """
    Lista o crea los usuarios
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
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    """
    Hacer retrieve, update o delete de un usuario
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

    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)

def usuarios_cuenta(request,pk):
    """
    Lista o crea los usuarios
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        usuarios = Usuario.objects.filter(cuenta=cuenta.id)
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer.data, safe=False)

def categorias_cuenta(request,pk):
    """
    Lista o crea los usuarios
    """
    try:
        cuenta = Cuenta.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        categorias = Categoria.objects.filter(cuenta=cuenta.id)
        serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(serializer.data, safe=False)
