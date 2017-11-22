from django.conf.urls import url
from controlgastos import views

urlpatterns = [
    url(r'^categorias/$', views.categoria_list),
    url(r'^categorias/(?P<pk>[0-9]+)/$', views.categoria_detail),
]
