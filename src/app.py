from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pycnpj_cpf.core import cnpj_or_cpf_is_valid

from .utils import generate_cnpj, generate_cpf

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html.j2')


@app.route('/validador', methods=['POST'])
def validador():
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
    tipo = request.form['tipo']
    messages = {
        'cpf': f'{generate_cpf()}',
        'cnpj': f'{generate_cnpj()}',
    }

    return render_template('gerador.html.j2', message=messages.get(tipo))


if __name__ == '__main__':
    app.run()
