# Trabajo Final para la materia Programacion Distribuida I
## Granata, Matias; Vecco, Mariano.
[![Build Status](https://travis-ci.org/marianovecco/Trabajo-Final.svg?branch=master)](https://travis-ci.org/marianovecco/Trabajo-Final)
[![Coverage Status](https://coveralls.io/repos/github/marianovecco/Trabajo-Final/badge.svg?branch=master)](https://coveralls.io/github/marianovecco/Trabajo-Final?branch=master)

# Tabla de Contenidos

1. [Introducción](#introducción)
2. [Instalación](#instalación)
	  * [Requisitos y dependencias](#requisitos-y-dependencias)
    * [Pasos para la instalación](#pasos-para-la-instalación)
3. [Documentación](#documentación)
4. [Test](#test)

---

# Introducción

El objetivo de este Trabajo es el desarrollo de una API HTTP para llevar a cabo el control de los gastos diarios de los usuarios, que serán agrupados en cuentas.
Esta API utilizara los siguientes recursos:

* Cuentas
* Usuarios
* Movimientos
* Categorías

Todos los pedidos serán devueltos en formato JSON. La información sobre los recursos y métodos disponibles para cada uno esta disponible en la [documentación](#documentación) del proyecto.

---

# Instalación:
### Requisitos y dependencias
Deberá contar con los siguientes paquetes instalados:
* Python 3.5  `sudo apt-get install python3`
    
* Django 1.11  `pip3 install Django`
    
* Django Rest Framework 3.7.3  `pip3 install djangorestframework`
 
* DRF Docs (para acceder a la [documentación](#documentación)) `pip3 install drfdocs`
    
### Pasos para la instalación
A continuación se detallan los pasos para la instalación:
```
git clone https://github.com/marianovecco/Trabajo-Final.git
cd tpfinal
python3 manage.py runserver
```
---

# Documentación
Para acceder a la pagina que contiene la documentación referente a las URIs disponibles y los metodos que pueden utilizarse debe instalarse DRF Docs utilizando el comando:

    pip3 install drfdocs

Y luego, con el servidor corriendo, es decir usando el comando:

    python3 manage.py runserver

Acceder desde el navegador a la url http://localhost:8000/docs (en caso de no usar el servidor o el puerto por defecto es necesario modificarlo).

Dentro podran encontrar las URIs con sus respectivos metodos, descripcion de su funcion y descripcion de los campos de los recursos utilizados. Ademas, haciendo click en el icono en el extremo derecho de cada URI se podran realizar requests de prueba y ver su correspondiente response.

---

# Test
Para los tests se han utilizado fixtures de forma que los datos de prueba ya son provistos por la API. Para correr los tests se debe utilizar el comando:
```
python3 manage.py test controlgastos
```
