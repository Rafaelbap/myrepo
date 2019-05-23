""" Neste arquivo está sendo importadas do Django a função urls  e todas as views do aplicativo blog    """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),# padrão para de url. toda vez que entrar na página principal irá aparecer o conteudo de post_list. Nesta linha o Django diz que views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://192.168.56.101:8000 /'."
]
