from django.urls import path
from .views  import *

urlpatterns = [
    path("", cadastro_produtos, name="cadastro_produtos"),
    path("editar/<int:pk>/", editar_produto, name="editar_produto"),
    path("excluir/<int:pk>/", excluir_produto, name="excluir_produto"),
]
