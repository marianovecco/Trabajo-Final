from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from controlgastos.models import Categoria, Cuenta, Usuario, Movimiento
from controlgastos.serializers import CategoriaSerializer, CuentaSerializer, UsuarioSerializer, MovimientoSerializer
from rest_framework.renderers import JSONRenderer
import json

class CategoriaTests(APITestCase):
    fixtures = ['db.json']
    def test_listar_categorias(self):
        """
        Test de listado de caterogias
        """
        url = '/controlgastos/categorias'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'nombre': 'Compras', 'cuenta': 1}])
        self.assertEqual(json.loads(content),[{'id': 1, 'nombre': 'Compras', 'cuenta': 1}])

    def test_crear_categoria(self):
        """
        Test de creacion de una categoria
        """
        url = '/controlgastos/categorias'
        response = self.client.post(url, {'nombre': 'Supermercado','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 2, 'nombre': 'Supermercado', 'cuenta': 1})
        categoria = Categoria.objects.get(id='2')
        serializer = CategoriaSerializer(categoria)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(content),{'id': 2, 'nombre': 'Supermercado', 'cuenta': 1})

    def test_obtener_categoria(self):
        """
        Test de obtencion de una sola categoria
        """
        url = '/controlgastos/categorias/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Compras', 'cuenta': 1})
        categoria = Categoria.objects.get(id='1')
        serializer = CategoriaSerializer(categoria)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(content),{'id': 1, 'nombre': 'Compras', 'cuenta': 1})

    def test_put_categoria(self):
        """
        Test de modificacion de una sola categoria con el metodo put
        """
        url = '/controlgastos/categorias/1'
        response = self.client.put(url, {'nombre': 'Perro','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Perro', 'cuenta': 1})
        categoria = Categoria.objects.get(id='1')
        serializer = CategoriaSerializer(categoria)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(content),{'id': 1, 'nombre': 'Perro', 'cuenta': 1})

    def test_patch_categoria(self):
        """
        Test de modificacion de una sola categoria con el metodo patch
        """
        url = '/controlgastos/categorias/1'
        response = self.client.put(url, {'nombre': 'Gato'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Gato', 'cuenta': 1})
        categoria = Categoria.objects.get(id='1')
        serializer = CategoriaSerializer(categoria)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(content),{'id': 1, 'nombre': 'Gato', 'cuenta': 1})

    def test_borrar_categoria(self):
        """
        Test de borrado de una sola categoria
        """
        url = '/controlgastos/categorias/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Categoria.objects.filter(id='1').exists())

    def test_obtener_movimientos(self):
        """
        Test de obtencion de los movimientos de una categoria
        """
        url = '/controlgastos/categorias/1/movimientos'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'}])
        categoria = Categoria.objects.get(id='1')
        movimientos = Movimiento.objects.filter(categoria=categoria)
        serializer = MovimientoSerializer(movimientos, many=True)
        content = JSONRenderer().render(serializer.data)
        self.assertEqual(json.loads(content),[{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'}])


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
        url = '/controlgastos/categorias/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UsuarioTests(APITestCase):
    fixtures = ['db.json']
    def test_listar_usuarios(self):
        """
        Test de listado de usuarios
        """
        url = '/controlgastos/usuarios'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'user': 'Pepito','password': '1234','email':'hola@123.com', 'cuenta': 1},{'id': 2, 'user': 'Pepon','password': '123478','email':'pepon@123.com', 'cuenta': 1}])

    def test_crear_usuario(self):
        """
        Test de creacion de una usuario
        """
        url = '/controlgastos/usuarios'
        response = self.client.post(url, {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 4, 'user': 'user1','password': 'contraseña','email':'user1@gmail.com', 'cuenta': 1})

    def test_obtener_usuario(self):
        """
        Test de obtencion de un solo usuario
        """
        url = '/controlgastos/usuarios/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, "user": "Pepito", "password": "1234", "email": "hola@123.com", "cuenta": 1})

    def test_put_usuario(self):
        """
        Test de modificacion de un usuario con el metodo put
        """
        url = '/controlgastos/usuarios/1'
        response = self.client.put(url, {'user': 'user1','password': 'contraseña','email':'user1@gmail.com','cuenta':'1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'user': 'user1','password': 'contraseña','email':'user1@gmail.com', 'cuenta': 1})

    def test_patch_usuario(self):
        """
        Test de modificacion de un usuario con el metodo patch
        """
        url = '/controlgastos/usuarios/1'
        response = self.client.patch(url, {'user': 'Mariano'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, "user": "Mariano", "password": "1234", "email": "hola@123.com", "cuenta": 1})


    def test_borrar_usuario_con(self):
        """
        Test de borrado de un solo usuario con movimientos
        """
        url = '/controlgastos/usuarios/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_borrar_usuario_sin(self):
        """
        Test de borrado de un solo usuario sin movimientos
        """
        url = '/controlgastos/usuarios/2'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_obtener_movimientos(self):
        """
        Test de obtencion de los movimientos de un usuario
        """
        url = '/controlgastos/usuarios/1/movimientos'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'}])

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
        url = '/controlgastos/usuarios/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CuentaTests(APITestCase):
    fixtures = ['db.json']
    def test_listar_cuentas(self):
        """
        Test de listado de cuentas
        """
        url = '/controlgastos/cuentas'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'nombre': 'Cuenta1'}])

    def test_crear_cuenta(self):
        """
        Test de creacion de una cuenta
        """
        url = '/controlgastos/cuentas'
        response = self.client.post(url, {'nombre': 'Cuenta2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id': 2, 'nombre': 'Cuenta2'})

    def test_obtener_cuenta(self):
        """
        Test de obtencion de una cuenta
        """
        url = '/controlgastos/cuentas/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Cuenta1'})

    def test_borrar_cuenta(self):
        """
        Test de borrado de una cuenta
        """
        url = '/controlgastos/cuentas/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_obtener_categorias(self):
        """
        Test de obtencion de las caterogias de una cuenta
        """
        url = '/controlgastos/cuentas/1/categorias'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'nombre': 'Compras', 'cuenta': 1}])

    def test_obtener_usuarios(self):
        """
        Test de obtencion de los usuarios de una cuenta
        """
        url = '/controlgastos/cuentas/1/usuarios'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id': 1, 'user': 'Pepito','password': '1234','email':'hola@123.com', 'cuenta': 1},{'id': 2, 'user': 'Pepon','password': '123478','email':'pepon@123.com', 'cuenta': 1}])

    def test_put_cuenta(self):
        """
        Test de modificacion de una cuenta con el metodo put
        """
        url = '/controlgastos/cuentas/1'
        response = self.client.put(url,  {'nombre': 'Cuenta2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Cuenta2'})

    def test_patch_cuenta(self):
        """
        Test de modificacion de una cuenta con el metodo patch
        """
        url = '/controlgastos/cuentas/1'
        response = self.client.patch(url, {'nombre': 'Cuenta3'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'nombre': 'Cuenta3'})

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
        url = '/controlgastos/cuentas/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class MovimientoTests(APITestCase):
    fixtures = ['db.json']
    def test_listar_movimientos(self):
        """
        Test de listado de movimientos
        """
        url = '/controlgastos/movimientos'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),[{'id':1, 'fecha':'2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'}])

    def test_crear_movimiento(self):
        """
        Test de creacion de un movimiento
        """
        url = '/controlgastos/movimientos'
        response = self.client.post(url, {'fecha':'2017-07-12','usuario':'1','monto':'3500','categoria':'1','descripcion':'pepito'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),{'id':2, 'fecha':'2017-07-12','usuario':1,'monto':3500,'categoria':1,'descripcion':'pepito'})

    def test_obtener_movimiento(self):
        """
        Test de obtencion de un solo movimiento
        """
        url = '/controlgastos/movimientos/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':2000,'categoria':1,'descripcion':'pepe'})

    def test_borrar_movimiento(self):
        """
        Test de borrado de un solo movimiento
        """
        url = '/controlgastos/movimientos/1'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_put_movimiento(self):
        """
        Test de modificacion de un movimiento con el metodo put
        """
        url = '/controlgastos/movimientos/1'
        response = self.client.put(url,   {'fecha':'2017-07-12','usuario':'1','monto':'3500','categoria':'1','descripcion':'pepito'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id':1, 'fecha':'2017-07-12','usuario':1,'monto':3500,'categoria':1,'descripcion':'pepito'})

    def test_patch_movimiento(self):
        """
        Test de modificacion de un movimiento con el metodo patch
        """
        url = '/controlgastos/movimientos/1'
        response = self.client.patch(url, {'monto': '5600'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),{'id': 1, 'fecha': '2017-07-12','usuario':1,'monto':5600,'categoria':1,'descripcion':'pepe'})

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
        url = '/controlgastos/movimientos/20'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
