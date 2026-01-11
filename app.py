import os
import sqlite3
import urllib.parse
from flask import Flask, render_template, request

from raads_data import questions_data, calculate_raads_score
from asrs_data import asrs_questions, calculate_asrs_score

app = Flask(__name__)

# CONFIGURAÇÕES PROFISSIONAIS
MEU_WHATSAPP = "5533991726976"
CLINICA = {
    "nome": "Nome da Sua Clínica",
    "profissional": "Seu Nome Completo",
    "crp": "00/00000",
    "endereco": "Endereço da Clínica, Cidade/UF"
}

@app.route('/')
def index():
    return render_template('home.html', clinica=CLINICA)

@app.route('/asrs', methods=['GET', 'POST'])
def asrs_test():
    if request.method == 'POST':
        nome = request.form.get('nome')
        total = calculate_asrs_score(request.form)
        conclusao = "Indícios de TDAH" if total >= 24 else "Abaixo do ponto de corte"
        
        msg = f"*Novo Teste ASRS-1.1*\n*Paciente:* {nome}\n*Total:* {total} pontos\n*Resultado:* {conclusao}"
        link = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={urllib.parse.quote(msg)}"
        
        return render_template('resultado.html', tipo="ASRS-1.1", total=total, link_wa=link, clinica=CLINICA)
    return render_template('asrs.html', questions=asrs_questions, clinica=CLINICA)

# Se for usar a Ficha Inicial depois:
@app.route('/ficha', methods=['GET', 'POST'])
def ficha():
    return render_template('ficha.html', clinica=CLINICA)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
