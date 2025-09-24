from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qnt_volume = models.IntegerField(default=0)
    
    unidade_medida = models.CharField(
        max_length=20,
        choices=[
            ("UN", "Unidade"),
            ("ML", "Mililitro"),
            ("L", "Litro"),
            ("CX", "Caixa"),
        ],
        default="UN"
    )
    
    estoque_atual = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=0)
    estoque_maximo = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('nome', 'categoria')
        ordering = ['nome'] 
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        
    def __str__(self):
        return f"{self.nome} - {self.categoria.nome}"