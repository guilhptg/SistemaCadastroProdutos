from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "nome", "categoria", "preco_venda", "unidade_medida",
            "estoque_atual", "estoque_minimo", "estoque_maximo", "ativo"
        ]