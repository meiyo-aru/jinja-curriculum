# Jinja Curriculum Render

Um serviço web de Renderização no Lado do Servidor (SSR) construído com **Python** e **Jinja2** para gerar currículos dinâmicos, estilizados com **SCSS**, e alimentado por uma **API RESTful** dedicada. Este projeto visa demonstrar a criação de conteúdo HTML rico e dinâmico, combinando a lógica de backend com a apresentação de frontend pré-renderizada.

-----

## Sobre o Projeto

O **Jinja Curriculum Render** é uma aplicação que pega dados de currículos de uma API RESTful (separada) e os injeta em templates Jinja2. O resultado é um HTML completo, com estilos aplicados via SCSS, que é enviado diretamente para o navegador do cliente. Isso garante uma experiência de usuário rápida, melhor SEO e um controle preciso sobre o design de cada currículo.

### Tecnologias Utilizadas

  * **Python**: Linguagem de programação principal para a lógica de backend e SSR.
  * **Jinja2**: Poderoso motor de templates para Python, permitindo a criação de HTML dinâmico com facilidade.
  * **SCSS (Sass)**: Linguagem de pré-processamento CSS, utilizada para escrever estilos modulares, reutilizáveis e fáceis de manter.
  * **API RESTful (Externa)**: O projeto espera se comunicar com uma API externa que fornece os dados estruturados dos currículos. Esta API é essencial para o funcionamento do gerador.

-----

## Funcionalidades

  * **Renderização Dinâmica de Currículos**: Gera currículos únicos para cada usuário com base nos dados recebidos da API.
  * **Estilização Profissional com SCSS**: Utiliza um sistema de design robusto baseado em SCSS para garantir um visual coeso e personalizável.
  * **SSR (Server-Side Rendering)**: Melhora o desempenho inicial, SEO e a acessibilidade, pois o conteúdo HTML já chega pronto para o navegador.
  * **Comunicação com API Externa**: Busca e exibe dados de currículos de uma fonte de dados centralizada.

-----

## Primeiros Passos

Para rodar este projeto localmente, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

  * [Python 3.x](https://www.python.org/downloads/)
  * [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)

### Configuração

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/blink992/jinja_curriculum_render.git
    cd jinja_curriculum_render
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências do Python:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração da API:**
    Este projeto espera que uma **API RESTful de currículos** esteja rodando em um endereço acessível.

      * Crie um arquivo `.env` na raiz do projeto (se necessário) e defina a URL da sua API:
        ```
        API_URL=http://localhost:8000/api
        ```
      * Certifique-se de que a API esteja funcionando e acessível.

### Executando a Aplicação

1. **Ative o ambiente virtual:**
   ```
   .\venv\scripts\activate
   ```
3.  **Execute o servidor uvicorn:**
    ```bash
    uvicorn main:app --reload --reload-dir
    ```
4.  Abra seu navegador e acesse `http://localhost:5000` (ou a porta configurada).

-----

## Estrutura do Projeto

```
jinja_curriculum_render/
├── venv/                 # Ambiente virtual do Python
├── static/               # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/              # CSS compilado do SCSS
|   └── scss/             # Código-fonte SCSS
|       ├── partials/     # Arquivos parciais importados pelo main.scss
|       └── main.scss
├── templates/            # Templates Jinja2
│   └── index.html
├── api.py                # Inicialização do FastAPI
├── external_api.py       # Comunicação com a api externa
├── main.py               # Lógica principal da aplicação Python
├── requirements.txt      # Dependências do Python
└── README.md             # Este arquivo
```

-----

## Contribuição

Contribuições são bem-vindas\! Se você tiver sugestões ou encontrar bugs, por favor, abra uma issue ou envie um pull request.

-----

## Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](./LICENSE.md) para mais detalhes.

-----
## Contato

Pedro Arthur Gregório Abreu - pedro.agb2004@gmail.com


