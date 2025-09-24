from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('cadastro/', cadastro_produtos, name='cadastro_produtos'),
]