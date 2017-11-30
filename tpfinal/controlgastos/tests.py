from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from controlgastos.models import Categoria, Cuenta
from controlgastos.serializers import CategoriaSerializer
from rest_framework.renderers import JSONRenderer

class CategoriaTests(APITestCase):
    def test_listar_categorias(self):
        """
        Test de listado de caterogias
        """
        url = '/controlgastos/categorias'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_categoria(self):
        """
        Test de creacion de una categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/categorias'
        response = self.client.post(url, {'nombre': 'Compras','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtener_categoria(self):
        """
        Test de obtencion de una sola categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrar_categoria(self):
        """
        Test de borrado de una sola categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class UsuarioTests(APITestCase):
    def test_listar_usuarios(self):
        """
        Test de listado de usuarios
        """
        url = '/controlgastos/usuarios'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_usuario(self):
        """
        Test de creacion de una usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/usuarios'
        response = self.client.post(url, {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtener_usuario(self):
        """
        Test de obtencion de un solo usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        url = '/controlgastos/usuarios/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrar_usuario(self):
        """
        Test de borrado de un solo usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        url = '/controlgastos/usuarios/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CuentaTests(APITestCase):
    def test_listar_cuentas(self):
        """
        Test de listado de cuentas
        """
        url = '/controlgastos/cuentas'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_cuenta(self):
        """
        Test de creacion de una cuenta
        """
        url = '/controlgastos/cuentas'
        response = self.client.post(url, {'nombre': 'cuenta1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtener_cuenta(self):
        """
        Test de obtencion de una cuenta
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/cuentas/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_borrar_cuenta(self):
        """
        Test de borrado de una cuenta
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/cuentas/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
