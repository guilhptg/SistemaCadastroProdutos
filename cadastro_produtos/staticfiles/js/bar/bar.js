
// Exemplo: confirmar antes de enviar formulário
document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function(e) {
            if (!confirm("Deseja realmente salvar este produto?")) {
                e.preventDefault();
            }
        });
    }
});


document.addEventListener('DOMContentLoaded', function () {
    // ... (scripts para categoria e estoque que já te passei) ...

    // --- Script para Modal de Edição de PRODUTO ---
    const editProdutoModal = document.getElementById('editProdutoModal');
    if (editProdutoModal) {
        editProdutoModal.addEventListener('show.bs.modal', function (event) {
            const button = event.relatedTarget; // Botão que acionou o modal

            // Pega a URL do atributo data-url
            const url = button.getAttribute('data-url');
            
            // Pega os dados dos atributos data-*
            const nome = button.getAttribute('data-nome');
            const categoria = button.getAttribute('data-categoria');
            const preco_venda = button.getAttribute('data-preco_venda').replace(',', '.');
            const unidade_medida = button.getAttribute('data-unidade_medida');
            const estoque_atual = button.getAttribute('data-estoque_atual').replace(',', '.');
            const estoque_minimo = button.getAttribute('data-estoque_minimo').replace(',', '.');
            const estoque_maximo = button.getAttribute('data-estoque_maximo').replace(',', '.');
            const ativo = button.getAttribute('data-ativo') === 'true';

            // Seleciona o formulário e os campos do modal
            const modalForm = editProdutoModal.querySelector('#editProdutoForm');
            const modalLabel = editProdutoModal.querySelector('#editProdutoModalLabel');
            
            // Define os valores dos campos
            modalForm.action = url;
            modalLabel.textContent = 'Editar Produto: ' + nome;
            modalForm.querySelector('#edit-produto-nome').value = nome;
            modalForm.querySelector('#edit-produto-categoria').value = categoria;
            modalForm.querySelector('#edit-produto-preco_venda').value = preco_venda;
            modalForm.querySelector('#edit-produto-unidade_medida').value = unidade_medida;
            modalForm.querySelector('#edit-produto-estoque_atual').value = estoque_atual;
            modalForm.querySelector('#edit-produto-estoque_minimo').value = estoque_minimo;
            modalForm.querySelector('#edit-produto-estoque_maximo').value = estoque_maximo;
            modalForm.querySelector('#edit-produto-ativo').checked = ativo;
        });
    }
});