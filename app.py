import os
import sqlite3
import urllib.parse
import sys
from flask import Flask, render_template, request, redirect, url_for

# Garante que o Python encontre os módulos locais na mesma pasta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importação dos dados e lógicas dos testes
from raads_data import questions_data, calculate_raads_score

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

# asrs_data.py

asrs_questions = [
    (1, "Com que frequência você tem dificuldade para finalizar os detalhes de um projeto, depois que as partes mais difíceis já foram feitas?"),
    (2, "Com que frequência você tem dificuldade para colocar as coisas em ordem quando está realizando uma tarefa que exige organização?"),
    (3, "Com que frequência você tem problemas para lembrar de compromissos ou obrigações?"),
    (4, "Quando você tem uma tarefa que exige muita concentração, com que frequência você evita ou adia o início dessa tarefa?"),
    (5, "Com que frequência você fica se mexendo na cadeira ou balançando as mãos ou os pés quando precisa ficar sentado por muito tempo?"),
    (6, "Com que frequência você se sente 'elétrico(a)' ou como se estivesse movido por um motor?"),
    # ... (Estas 6 acima são a Parte A - a mais crítica)
    (7, "Com que frequência você comete erros por falta de atenção quando tem que trabalhar num projeto chato ou difícil?"),
    (8, "Com que frequência você tem dificuldade em manter a atenção quando está fazendo um trabalho chato ou repetitivo?"),
    (9, "Com que frequência você tem dificuldade em se concentrar no que as pessoas dizem, mesmo quando elas estão falando diretamente com você?"),
    (10, "Com que frequência você coloca as coisas fora do lugar ou tem dificuldade de encontrar as coisas em casa ou no trabalho?"),
    (11, "Com que frequência você se distrai com sons ou atividades à sua volta?"),
    (12, "Com que frequência você deixa seu assento em reuniões ou em outras situações em que deveria ficar sentado?"),
    (13, "Com que frequência você se sente inquieto(a) ou agitado(a)?"),
    (14, "Com que frequência você tem dificuldade para sossegar e relaxar quando tem tempo livre para você?"),
    (15, "Com que frequência você se pega falando demais em situações sociais?"),
    (16, "Quando você está conversando, com que frequência você se pega terminando as frases das pessoas antes delas mesmas terminarem?"),
    (17, "Com que frequência você tem dificuldade de esperar a sua vez em situações em que isso é necessário?"),
    (18, "Com que frequência você interrompe os outros quando eles estão ocupados?")
]

def calculate_asrs_score(responses):
    # No ASRS, pontos acima de "As_vezes" ou "Frequentemente" em certas questões indicam TDAH
    # Simplificaremos para uma pontuação de 0 a 4 por questão
    points_map = {
        "Nunca": 0,
        "Raramente": 1,
        "As_vezes": 2,
        "Frequentemente": 3,
        "Muito_Frequentemente": 4
    }
    
    total = 0
    for i in range(1, 19):
        ans = responses.get(f"q{i}")
        if ans:
            total += points_map[ans]
            
    return total

if __name__ == '__main__':
    # FORÇAR ATUALIZAÇÃO DO BANCO (Pode apagar essas 2 linhas após funcionar uma vez)
    if os.path.exists('database.db'):
        os.remove('database.db')
        
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # Configuração para Render (dinâmico) ou Local (5000)
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)

