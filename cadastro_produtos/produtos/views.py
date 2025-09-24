from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto, Categoria


def cadastro_produtos(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        categoria_id = request.POST.get("categoria")
        preco_custo = request.POST.get("preco_custo")
        preco_venda = request.POST.get("preco_venda")
        unidade_medida = request.POST.get("unidade_medida")
        estoque_atual = request.POST.get("estoque_atual", 0)
        qnt_volume = request.POST.get("qnt_volume", 0)
        estoque_minimo = request.POST.get("estoque_minimo", 0)
        estoque_maximo = request.POST.get("estoque_maximo", 100)
        ativo = True if request.POST.get("ativo") == "on" else False

        categoria = Categoria.objects.get(id=categoria_id)

        Produto.objects.create(
            nome=nome,
            categoria=categoria,
            preco_custo=preco_custo,
            preco_venda=preco_venda,
            qnt_volume=qnt_volume,
            unidade_medida=unidade_medida,
            estoque_atual=estoque_atual,
            estoque_minimo=estoque_minimo,
            estoque_maximo=estoque_maximo,
            ativo=ativo,
        )

        messages.success(request, f"{nome} cadastrado com sucesso!")
        return redirect("cadastro_produtos")

    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        "produtos": produtos,
        "categorias": categorias,
    }
    return render(request, "cadastro/bar/bar.html", context)


def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        dados = request.POST.dict()
        print(dados)
        produto.nome = request.POST.get("nome")
        produto.categoria_id = request.POST.get("categoria")
        produto.preco_custo = request.POST.get("preco_custo", 0)
        produto.preco_venda = request.POST.get("preco_venda")
        produto.unidade_medida = request.POST.get("unidade_medida")
        produto.qnt_volume = request.POST.get("qnt_volume", 0)
        produto.estoque_atual = request.POST.get("estoque_atual", 0)
        produto.estoque_minimo = request.POST.get("estoque_minimo", 0)
        produto.estoque_maximo = request.POST.get("estoque_maximo", 100)
        produto.ativo = True if request.POST.get("ativo") == "on" else False
        produto.save()
        messages.success(request, f"{produto} atualizado com sucesso!")
        return redirect("cadastro_produtos")

    categorias = Categoria.objects.all()
    context = {
        "produto": produto,
        "categorias": categorias,
    }
    return redirect(cadastro_produtos)


def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    messages.success(request, "Produto excluído com sucesso!")
    return redirect("cadastro_produtos")
