from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from controlgastos.models import Categoria, Cuenta
from controlgastos.serializers import CategoriaSerializer
from rest_framework.renderers import JSONRenderer
import json

class CategoriaTests(APITestCase):
    def test_listar_categorias(self):
        """
        Test de listado de caterogias
        """
        url = '/controlgastos/categorias'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[]) #Por ahora dejemoslo asi, despues veo si usamos fixtures y hay que cambiarlo


    def test_crear_categoria(self):
        """
        Test de creacion de una categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/categorias'
        response = self.client.post(url, {'nombre': 'Compras','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Compras', 'cuenta': 1})

    def test_obtener_categoria(self):
        """
        Test de obtencion de una sola categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Compras', 'cuenta': 1})

    def test_borrar_categoria(self):
        """
        Test de borrado de una sola categoria
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bad_request(self):
        """
        Testea cuando un request no se hace correctamente, en este caso no se le pasan parametros al post
        """
        url = '/controlgastos/categorias'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found(self):
        """
        Testea cuando se pide una categoria que no existe
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/categorias/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UsuarioTests(APITestCase):
    def test_listar_usuarios(self):
        """
        Test de listado de usuarios
        """
        url = '/controlgastos/usuarios'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[])

    def test_crear_usuario(self):
        """
        Test de creacion de una usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/usuarios'
        response = self.client.post(url, {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 1, 'user': 'user1','password': 'contraseña','email':'user1@gmail.com', 'cuenta': 1})

    def test_obtener_usuario(self):
        """
        Test de obtencion de un solo usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        url = '/controlgastos/usuarios/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'user': 'user1','password': 'contraseña','email':'user1@gmail.com', 'cuenta': 1})

    def test_borrar_usuario(self):
        """
        Test de borrado de un solo usuario
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        url = '/controlgastos/usuarios/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bad_request(self):
        """
        Testea cuando un request no se hace correctamente, en este caso no se le pasan parametros al post
        """
        url = '/controlgastos/usuarios'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found(self):
        """
        Testea cuando se pide un usuario que no existe
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        url = '/controlgastos/usuarios/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CuentaTests(APITestCase):
    def test_listar_cuentas(self):
        """
        Test de listado de cuentas
        """
        url = '/controlgastos/cuentas'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[])

    def test_crear_cuenta(self):
        """
        Test de creacion de una cuenta
        """
        url = '/controlgastos/cuentas'
        response = self.client.post(url, {'nombre': 'cuenta1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'cuenta1'})

    def test_obtener_cuenta(self):
        """
        Test de obtencion de una cuenta
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/cuentas/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'cuenta1'})


    def test_borrar_cuenta(self):
        """
        Test de borrado de una cuenta
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/cuentas/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bad_request(self):
        """
        Testea cuando un request no se hace correctamente, en este caso no se le pasan parametros al post
        """
        url = '/controlgastos/cuentas'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_not_found(self):
        """
        Testea cuando se pide una cuenta que no existe
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        url = '/controlgastos/cuentas/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)




class MovimientoTests(APITestCase):
    def test_listar_movimientos(self):
        """
        Test de listado de movimientos
        """
        url = '/controlgastos/movimientos'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[])

    def test_crear_movimiento(self):
        """
        Test de creacion de un movimiento
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/movimientos'
        response = self.client.post(url, {'fecha':'2017-07-12','usuario':'1','monto':'2000','categoria':'1','descripcion':'pepe'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id':1, 'fecha':'2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'})

    def test_obtener_movimiento(self):
        """
        Test de obtencion de un solo movimiento
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/movimientos', {'fecha':'2017-07-12','usuario':'1','monto':'2000','categoria':'1','descripcion':'pepe'}, format='json')
        url = '/controlgastos/movimientos/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'})

    def test_borrar_movimiento(self):
        """
        Test de borrado de un solo movimiento
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('/controlgastos/usuarios', {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/movimientos', {'fecha':'2017-07-12','usuario':'1','monto':'2000','categoria':'1','descripcion':'pepe'}, format='json')
        url = '/controlgastos/movimientos/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_bad_request(self):
        """
        Testea cuando un request no se hace correctamente, en este caso no se le pasan parametros al post
        """
        url = '/controlgastos/movimientos'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found(self):
        """
        Testea cuando se pide un movimiento que no existe
        """
        self.client.post('/controlgastos/cuentas', {'nombre': 'cuenta1'}, format='json')
        self.client.post('controlgastos/usuarios',{'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.client.post('/controlgastos/categorias', {'nombre': 'Compras','cuenta':'1'}, format='json')
        url = '/controlgastos/movimientos/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
