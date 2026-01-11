import os
import sqlite3
import urllib.parse
import sys
from flask import Flask, render_template, request, redirect, url_for

# Garante que o Python encontre os módulos locais na mesma pasta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importação dos dados e lógicas dos testes
from raads_data import questions_data, calculate_raads_score
from asrs_data import asrs_questions, calculate_asrs_score

app = Flask(__name__)

# CONFIGURAÇÕES
MEU_WHATSAPP = "5533991726976"

# Inicialização do Banco de Dados atualizado para suportar múltiplos testes
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Tabela unificada com coluna 'tipo_teste' para diferenciar
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            tipo_teste TEXT,
            pontuacao_total INTEGER,
            detalhes TEXT,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# --- ROTA: PÁGINA INICIAL (MENU) ---
@app.route('/')
def index():
    return render_template('home.html')

# --- ROTA: TESTE RAADS-R (AUTISMO) ---
@app.route('/raads', methods=['GET', 'POST'])
def raads_test():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        total, subescalas = calculate_raads_score(request.form)
        
        # Salvar no Banco
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO resultados (nome, email, tipo_teste, pontuacao_total, detalhes)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, 'RAADS-R', total, str(subescalas)))
        conn.commit()
        conn.close()

        # Link WhatsApp
        conclusao = "Possibilidade de TEA" if total >= 65 else "Abaixo do ponto de corte"
        mensagem = f"""*Novo Teste RAADS-R (Autismo)*
*Nome:* {nome}
*Email:* {email}
-----------------------
*Total: {total}* ({conclusao})
Social: {subescalas['Social']}
Linguagem: {subescalas['Linguagem']}
Sensório: {subescalas['Sensório']}
Interesses: {subescalas['Interesses']}
-----------------------"""
        
        link_wa = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={urllib.parse.quote(mensagem)}"
        
        return render_template('resultado.html', tipo="RAADS-R", total=total, sub=subescalas, link_wa=link_wa)

    return render_template('raads.html', questions=questions_data)

# --- ROTA: TESTE ASRS-1.1 (TDAH) ---
@app.route('/asrs', methods=['GET', 'POST'])
def asrs_test():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        total = calculate_asrs_score(request.form)
        
        # Salvar no Banco
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO resultados (nome, email, tipo_teste, pontuacao_total, detalhes)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, email, 'ASRS-1.1', total, 'N/A'))
        conn.commit()
        conn.close()

        # Link WhatsApp
        conclusao = "Indícios de TDAH" if total >= 24 else "Abaixo do ponto de corte"
        mensagem = f"""*Novo Teste ASRS-1.1 (TDAH)*
*Nome:* {nome}
*Email:* {email}
-----------------------
*Total: {total} pontos*
Status: {conclusao}
-----------------------"""
        
        link_wa = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={urllib.parse.quote(mensagem)}"
        
        return render_template('resultado.html', tipo="ASRS-1.1", total=total, sub=None, link_wa=link_wa)

    return render_template('asrs.html', questions=asrs_questions)

if __name__ == '__main__':
    init_db()
    # Configuração para Render (dinâmico) ou Local (5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
