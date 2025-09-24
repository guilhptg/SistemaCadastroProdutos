
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