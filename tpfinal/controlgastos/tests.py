from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Categoria, Cuenta
from .serializers import CategoriaSerializer
from rest_framework.renderers import JSONRenderer

class CategoriaTests(APITestCase):
    def test_listar_categorias(self):
        """
        Test de listado de caterogias
        """
        url = '/controlgastos/categorias/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_categoria(self):
        """
        Test de creacion de una categoria
        """
        self.client.post('/controlgastos/cuentas/', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/categorias/'
        response = self.client.post(url, {'nombre': 'Compras','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtener_categoria(self):
        """
        Test de obtencion de una sola categoria
        """
        self.client.post('/controlgastos/cuentas/', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias/', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrarr_categoria(self):
        """
        Test de borrado de una sola categoria
        """
        self.client.post('/controlgastos/cuentas/', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias/', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_410_GONE)
