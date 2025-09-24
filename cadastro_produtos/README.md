# Sistema de Gestão de Produtos - Django

> Um sistema web completo para cadastro e administração de produtos, desenvolvido com Django. Ideal para pequenas empresas, bares ou restaurantes que precisam de um controle de estoque e catálogo de produtos eficiente e intuitivo.

Este projeto foi criado como parte de um estudo prático sobre o desenvolvimento de aplicações web escaláveis e bem organizadas com o framework Django, aplicando conceitos de CRUD (Create, Read, Update, Delete) em um ambiente interativo e responsivo. Para a matéria de **Técnicas de Desenvolvimento de Algoritimos do CTS em Análise e Desenvolviento de Sistemas**

![Screenshot da Aplicação](/images/cadastro.png)
_**Nota:** Faça o upload da sua imagem para o repositório e substitua `path/to/your/screenshot.png` pelo caminho correto._

---

## ✨ Funcionalidades Principais

* **✅ Gestão de Produtos:**
    * Cadastro de novos produtos com nome, categoria, preço, unidade de medida e níveis de estoque.
    * Edição de informações de produtos existentes.
    * Exclusão de produtos.
* **✅ Gestão de Categorias:**
    * Criação, edição e exclusão de categorias para organizar os produtos.
    * Validação para impedir a exclusão de categorias que possuem produtos associados.
* **✅ Controle de Estoque:**
    * Visualização rápida do estoque atual e mínimo de todos os produtos.
    * Interface com destaque visual (cores) para produtos com estoque baixo ou esgotado.
* **✅ Interface Moderna e Interativa:**
    * Uso de **modais** para operações de cadastro e edição, evitando a necessidade de recarregar a página.
    * Navegação organizada em abas para separar as seções de Produtos, Categorias e Estoque.
    * Feedback ao usuário com mensagens de sucesso e erro após cada operação.

---

## 🚀 Tecnologias Utilizadas

Este projeto foi construído com as seguintes tecnologias:

* **Backend:**
    * ![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
    * ![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
* **Frontend:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
    * ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
* **Banco de Dados:**
    * ![SQLite3](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white) (Padrão de desenvolvimento)

---

## 🛠️ Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar a aplicação no seu ambiente de desenvolvimento.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.11+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    # Para Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Para Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    *Primeiro, crie o arquivo `requirements.txt` se ele não existir, com o ambiente virtual ativado:*
    ```bash
    pip freeze > requirements.txt
    ```
    *Depois, instale as dependências (ou se você já tiver o arquivo):*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um superusuário para acessar o Admin (Opcional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Execute o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Acesse a aplicação no seu navegador em `http://127.0.0.1:8000/`.

---

## 📈 Possíveis Melhorias Futuras

Este projeto tem um grande potencial de expansão. Algumas ideias para futuras implementações:

* [ ] **Sistema de Autenticação:** Criar um sistema de login/logout para que apenas usuários autorizados possam gerenciar os produtos.
* [ ] **Dashboard de Análise:** Implementar um painel com gráficos mostrando produtos mais vendidos, níveis de estoque gerais, etc.
* [ ] **API REST:** Desenvolver uma API com Django REST Framework para permitir a integração com outras aplicações.
* [ ] **Testes Automatizados:** Escrever testes unitários e de integração para garantir a estabilidade do código.
* [ ] **Containerização:** Criar uma configuração com Docker para facilitar o deploy da aplicação.

---

## ✒️ Autor

Projeto desenvolvido por **[Seu Nome Completo]**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/seu-usuario/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/seu-usuario)