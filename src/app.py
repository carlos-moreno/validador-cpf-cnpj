from datetime import datetime, timezone

from flask import Flask, render_template, request
from pycnpj_cpf.core import cnpj_or_cpf_is_valid

from .utils import generate_cnpj, generate_cpf

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html.j2')


@app.route('/validador', methods=['POST'])
def validador():
    cpf_cnpj = request.form.get('cpf_cnpj', '').strip()
    if not cpf_cnpj:
        return '<div class="alert alert-warning">Informe um valor!</div>'

    is_valid = cnpj_or_cpf_is_valid(cpf_cnpj)
    color = 'success' if is_valid else 'danger'
    status = 'válido' if is_valid else 'inválido'
    icon = 'check-circle' if is_valid else 'exclamation-triangle'

    return f"""
    <div class="alert alert-{color} d-flex align-items-center animate__animated animate__fadeIn">
        <i class="bi bi-{icon} me-2"></i>
        <div>{cpf_cnpj} é <strong>{status}</strong>!</div>
    </div>
    """


@app.route('/gerador', methods=['POST'])
def gerador():
    tipo = request.form.get('tipo')
    valor = generate_cpf() if tipo == 'cpf' else generate_cnpj()

    return render_template('partials/resultado_gerador.html.j2', valor=valor, tipo=tipo)


@app.context_processor
def inject_now():
    return {'now': datetime.now(timezone.utc)}


if __name__ == '__main__':
    app.run()
