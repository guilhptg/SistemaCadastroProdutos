from django.shortcuts import render, redirect
from django.contrib import messages
from produtos.models import Produto, Categoria

def cadastro_produtos(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.select_related("categoria").all()

    if request.method == "POST":
        nome = request.POST.get("nome")
        categoria_id = request.POST.get("categoria")
        preco_venda = request.POST.get("preco_venda")
        unidade_medida = request.POST.get("unidade_medida")
        estoque_atual = request.POST.get("estoque_atual")
        estoque_minimo = request.POST.get("estoque_minimo")
        estoque_maximo = request.POST.get("estoque_maximo")
        ativo = request.POST.get("ativo") == "on"

        if not nome or not categoria_id or not preco_venda:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            
        else:
            try:
                categoria = Categoria.objects.get(id=categoria_id)
                produto = Produto.objects.create(
                    nome=nome,
                    categoria=categoria,
                    preco_venda=preco_venda,
                    unidade_medida=unidade_medida,
                    estoque_atual=estoque_atual or 0,
                    estoque_minimo=estoque_minimo or 0,
                    estoque_maximo=estoque_maximo or 100,
                    ativo=ativo
                )
                messages.success(request, f"Produto '{produto.nome}' cadastrado com sucesso!")
                return redirect("cadastro_produtos")
            except Categoria.DoesNotExist:
                messages.error(request, "Categoria inválida.")

    context = {
        "categorias": categorias,
        "produtos": produtos,
    }
    return render(request, "cadastro/bar/cadastro_produtos.html", context)
