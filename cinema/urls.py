from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$' , views.lista_post),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalhes_post),
]
