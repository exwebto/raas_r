import os
import sqlite3
import urllib.parse
from flask import Flask, render_template, request

from raads_data import questions_data, calculate_raads_score
from asrs_data import asrs_questions, calculate_asrs_score

app = Flask(__name__)

MEU_WHATSAPP = "5533991726976"
DADOS_CLINICA = {
    "nome": "Sua Clínica de Psicologia",
    "profissional": "Seu Nome Completo",
    "crp": "00/00000",
    "endereco": "Rua Exemplo, 123 - Cidade/UF"
}

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT, email TEXT, tipo_teste TEXT, 
            pontuacao_total INTEGER, detalhes TEXT, data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('home.html', clinica=DADOS_CLINICA)

@app.route('/asrs', methods=['GET', 'POST'])
def asrs_test():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        total = calculate_asrs_score(request.form)
        
        conclusao = "Indícios de TDAH" if total >= 24 else "Abaixo do ponto de corte"
        mensagem = f"*Novo Teste ASRS-1.1 (TDAH)*\n*Nome:* {nome}\n*Total:* {total} pontos\n*Status:* {conclusao}"
        link_wa = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={urllib.parse.quote(mensagem)}"
        
        return render_template('resultado.html', tipo="ASRS-1.1", total=total, link_wa=link_wa, clinica=DADOS_CLINICA)
    return render_template('asrs.html', questions=asrs_questions, clinica=DADOS_CLINICA)

@app.route('/ficha', methods=['GET', 'POST'])
def ficha():
    if request.method == 'POST':
        d = request.form
        msg = f"*FICHA INICIAL*\n*Nome:* {d.get('nome')}\n*Motivo:* {d.get('motivo')}"
        link_wa = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={urllib.parse.quote(msg)}"
        return render_template('resultado.html', tipo="Ficha Inicial", total="Enviada", link_wa=link_wa, clinica=DADOS_CLINICA)
    return render_template('ficha.html', clinica=DADOS_CLINICA)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
