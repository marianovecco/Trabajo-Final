from django.conf.urls import url
from controlgastos import views

urlpatterns = [
    url(r'^categorias$', views.CategoriaList.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)$', views.CategoriaDetail.as_view()),
    url(r'^cuentas$', views.CuentaList.as_view()),
    url(r'^cuentas/(?P<pk>[0-9]+)$', views.CuentaDetail.as_view()),
    url(r'^usuarios$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)$', views.UsuarioDetail.as_view()),
    url(r'^cuentas/(?P<pk>[0-9]+)/usuarios$', views.usuarios_cuenta),
    url(r'^cuentas/(?P<pk>[0-9]+)/categorias$', views.categorias_cuenta),
    url(r'^movimientos$', views.MovimientoList.as_view()),
    url(r'^movimientos/(?P<pk>[0-9]+)$', views.MovimientoDetail.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/movimientos$', views.movimientos_usuario),
    url(r'^categorias/(?P<pk>[0-9]+)/movimientos$', views.movimientos_categoria),
]
