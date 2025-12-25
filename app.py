import os
print(os.getcwd())
import sqlite3
import urllib.parse
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from raads_data import questions_data, calculate_raads_score
from flask import Flask, render_template, request, redirect, url_for
from raads_data import questions_data, calculate_raads_score

app = Flask(__name__)

# CONFIGURAÇÕES - ALTERE AQUI
MEU_WHATSAPP = "5533991726976"  # Coloque seu número com DDD (apenas números)

# Função para inicializar o Banco de Dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            pontuacao_total INTEGER,
            social INTEGER,
            linguagem INTEGER,
            sensorio INTEGER,
            interesses INTEGER,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coleta dados do usuário
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        # Calcula a pontuação usando a lógica do raads_data.py
        total, subescalas = calculate_raads_score(request.form)
        
        # 1. SALVAR NO BANCO DE DADOS
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO resultados (nome, email, pontuacao_total, social, linguagem, sensorio, interesses)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nome, email, total, subescalas['Social'], subescalas['Linguagem'], subescalas['Sensório'], subescalas['Interesses']))
        conn.commit()
        conn.close()

        # 2. GERAR LINK DO WHATSAPP
        conclusao = "Possibilidade de TEA" if total >= 65 else "Abaixo do ponto de corte"
        mensagem = f"""*Novo Teste RAADS-R*
*Nome:* {nome}
*Email:* {email}
-----------------------
*Total: {total}* ({conclusao})
Social: {subescalas['Social']}
Linguagem: {subescalas['Linguagem']}
Sensório: {subescalas['Sensório']}
Interesses: {subescalas['Interesses']}
-----------------------
_Dados salvos no banco de dados._"""
        
        texto_url = urllib.parse.quote(mensagem)
        link_wa = f"https://api.whatsapp.com/send?phone={MEU_WHATSAPP}&text={texto_url}"
        
        # 3. REDIRECIONAR PARA RESULTADO (E abrir WhatsApp em nova aba via JS se preferir)
        return render_template('resultado.html', total=total, sub=subescalas, link_wa=link_wa)

    return render_template('index.html', questions=questions_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)