from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pycnpj_cpf.core import cnpj_or_cpf_is_valid

from .utils import generate_cnpj, generate_cpf

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    """Renderiza a página inicial da aplicação."""
    return render_template('index.html.j2')


@app.route('/validador', methods=['POST'])
def validador():
    """Processa a validação de um CPF ou CNPJ enviado via formulário.

    Esta view é acionada por uma requisição POST e espera receber um
    campo 'cpf_cnpj' no corpo do formulário. A função verifica se o
    valor recebido é um CPF ou CNPJ válido e renderiza uma página de
    resposta com uma mensagem indicando o resultado da validação.

    O template 'validador.html.j2' é utilizado para exibir a mensagem
    ao usuário.

    Form Data:
        cpf_cnpj (str): O número de CPF ou CNPJ a ser validado.

    Returns:
        werkzeug.wrappers.Response: Uma resposta HTTP contendo a página
        HTML renderizada com a mensagem de validação.
    """
    cpf_cnpj = request.form['cpf_cnpj']
    result = cnpj_or_cpf_is_valid(cpf_cnpj)

    messages = {
        None: 'Informe um valor a ser verificado!',
        True: f'{cpf_cnpj} é válido!',
        False: f'{cpf_cnpj} é inválido.',
    }

    message = messages[None] if not cpf_cnpj else messages[result]

    return render_template('validador.html.j2', message=message)


@app.route('/gerador', methods=['POST'])
def gerador():
    """Gera um número de CPF ou CNPJ com base na seleção do usuário.

    Esta view é acionada por uma requisição POST e espera um campo 'tipo'
    no formulário para determinar qual documento gerar ('cpf' ou 'cnpj').
    Após chamar a função geradora apropriada, o número resultante é
    renderizado no template 'gerador.html.j2'.

    Form Data:
        tipo (str): O tipo de documento a ser gerado.
                    Valores esperados são 'cpf' ou 'cnpj'.

    Contexto do Template:
        message (str or None): O número do CPF ou CNPJ gerado como uma string.
                               Será `None` se o tipo for inválido.
        type (str): O valor original do campo 'tipo' enviado no formulário,
                    usado para manter o estado da seleção na página.

    Returns:
        werkzeug.wrappers.Response: Uma resposta HTTP contendo a página HTML
        'gerador.html.j2' renderizada com o número gerado.
    """
    tipo = request.form['tipo']
    messages = {
        'cpf': f'{generate_cpf()}',
        'cnpj': f'{generate_cnpj()}',
    }

    return render_template(
        'gerador.html.j2', message=messages.get(tipo), type=tipo
    )


if __name__ == '__main__':
    app.run()
