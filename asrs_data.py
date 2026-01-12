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
    # O dicionário com os seus novos termos com underscore
    points_map = {
        "Nunca": 0,
        "Raramente": 1,
        "As_vezes": 2,
        "Frequentemente": 3,
        "Muito_Frequentemente": 4
    }
    
    total = 0
    # O formulário tem 18 perguntas (q1 até q18)
    for i in range(1, 19):
        campo = f"q{i}"
        # .get() evita erro se a pergunta não foi respondida
        valor_recebido = responses.get(campo)
        
        if valor_recebido:
            # Limpa espaços invisíveis que o servidor possa ter inserido
            valor_limpo = valor_recebido.strip()
            # .get(valor_limpo, 0) tenta achar no dicionário. 
            # Se não achar (erro de digitação), ele soma 0 e NÃO trava o site.
            total += points_map.get(valor_limpo, 0)
            
    return total
