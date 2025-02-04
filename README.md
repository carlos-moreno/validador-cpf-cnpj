# Validador de CPF/CNPJ

Este é um sistema web desenvolvido em Python utilizando o framework Flask, para validar se um CPF ou CNPJ informado é válido. Além disso, o sistema pode gerar um número de CPF ou CNPJ válido.

## Funcionalidades

- Validação de CPF
- Validação de CNPJ
- Geração de CPF válido
- Geração de CNPJ válido

## Instalação

Para executar este projeto, siga os seguintes passos:

1. Clone o repositório:

```bash
git clone https://github.com/carlos-moreno/validador-cpf-cnpj.git
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
uv sync
source .venv/bin/activate
```
## Uso

1. Inicie o servidor Flask:

```bash
FLASK_APP=src/app.py flask run
```

2. Abra o navegador e acesse `http://127.0.0.1:5000`.

3. Na interface web, você pode inserir um CPF ou CNPJ para validação ou gerar um novo número válido.

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a lógica da aplicação.
- `templates/`: Diretório que contém os templates HTML.
- `static/`: Diretório para arquivos estáticos, como CSS e JavaScript.
- `utils.py`: Contém funções de validação e geração de CPF/CNPJ.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
