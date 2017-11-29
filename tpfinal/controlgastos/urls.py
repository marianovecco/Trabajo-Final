from django.conf.urls import url
from controlgastos import views

urlpatterns = [
    url(r'^categorias$', views.categoria_list),
    url(r'^categorias/(?P<pk>[0-9]+)$', views.categoria_detail),
    url(r'^cuentas$', views.cuenta_list),
    url(r'^cuentas/(?P<pk>[0-9]+)$', views.cuenta_detail),
    url(r'^usuarios$', views.usuario_list),
    url(r'^usuarios/(?P<pk>[0-9]+)$', views.usuario_detail),
    url(r'^cuentas/(?P<pk>[0-9]+)/usuarios$', views.usuarios_cuenta),
    url(r'^cuentas/(?P<pk>[0-9]+)/categorias$', views.categorias_cuenta),
]
