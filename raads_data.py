# raads_data.py

# Estrutura: (ID, Pergunta, Subescala, Inverter_Pontuacao)
# Inverter_Pontuacao: True para perguntas onde "Nunca" indica traço autista.
# As subescalas são: Social, Linguagem, Sensório, Interesses

questions_data = [
    (1, "Sou uma pessoa simpática.", "Social", True),
    (2, "Costumo usar palavras e frases de filmes e televisão em conversas.", "Linguagem", False),
    (3, "Muitas vezes fico surpreso quando os outros me dizem que fui rude.", "Social", False),
    (4, "Às vezes falo muito alto ou muito baixo e não percebo.", "Linguagem", False),
    (5, "Muitas vezes não sei como agir em situações sociais.", "Social", False),
    (6, "Eu consigo me colocar no lugar das outras pessoas.", "Social", True),
    (7, "Tenho dificuldade em entender o significado de algumas frases, como 'você é a menina dos meus olhos'.", "Linguagem", False),
    (8, "Só gosto de conversar com pessoas que tenham os mesmos interesses que os meus.", "Social", False),
    (9, "Eu me concentro nos detalhes em vez da ideia geral.", "Sensório", False),
    (10, "Eu sempre noto como a comida fica na minha boca. Isso é mais importante para mim do que o gosto dela.", "Sensório", False),
    (11, "Sinto falta dos meus melhores amigos ou familiares quando ficamos separados por muito tempo.", "Social", True),
    (12, "Às vezes ofendo os outros ao dizer o que estou pensando, mesmo que não seja minha intenção.", "Social", False),
    (13, "Só gosto de pensar e falar sobre algumas coisas que me interessam.", "Interesses", False),
    (14, "Prefiro sair para comer em um restaurante sozinho do que com alguém que conheço.", "Social", False),
    (15, "Não consigo imaginar como seria estar na pele de outra pessoa.", "Social", False),
    (16, "Já me disseram que sou desajeitado ou descoordenado.", "Sensório", False),
    (17, "Os outros me consideram estranho ou diferente.", "Social", False),
    (18, "Eu entendo quando os amigos precisam ser consolados.", "Social", True),
    (19, "Sou muito sensível à sensação das roupas na minha pele.", "Sensório", False),
    (20, "Gosto de copiar as maneiras de falar e agir de certas pessoas. Isso me ajuda a parecer mais normal.", "Social", False),
    (21, "Pode ser muito intimidador para mim falar com mais de uma pessoa ao mesmo tempo.", "Social", False),
    (22, "Tenho que 'agir normalmente' para agradar outras pessoas.", "Social", False),
    (23, "Conhecer novas pessoas geralmente é fácil para mim.", "Social", True),
    (24, "Fico muito confuso quando alguém me interrompe quando estou falando.", "Interesses", False),
    (25, "É difícil para mim entender como as outras pessoas estão se sentindo.", "Social", False),
    (26, "Gosto de conversar com várias pessoas em volta de uma mesa.", "Social", True),
    (27, "Eu levo as coisas muito ao pé da letra.", "Linguagem", False),
    (28, "Costumo ter dificuldade para saber quando alguém está brincando comigo.", "Social", False),
    (29, "Algumas texturas comuns parecem muito ofensivas quando tocam minha pele.", "Sensório", False),
    (30, "Fico extremamente chateado quando a maneira como gosto de fazer as coisas muda.", "Interesses", False),
    (31, "Nunca quis ou precisei ter o que outras pessoas chamam de 'relacionamento íntimo'.", "Social", False),
    (32, "Costumo me interessar muito por certos tópicos e falar sobre eles sem parar.", "Interesses", False),
    (33, "Falo com um ritmo normal.", "Linguagem", True),
    (34, "O mesmo som, cor ou textura pode mudar repentinamente de muito sensível para muito opaco.", "Sensório", False),
    (35, "Tenho dificuldade em entender expressões idiomáticas ou metáforas.", "Linguagem", False),
    (36, "Às vezes, o som de uma palavra ou de um ruído agudo pode ser doloroso.", "Sensório", False),
    (37, "Sou uma pessoa compreensiva.", "Social", True),
    (38, "Não me conecto com personagens de filmes.", "Social", False),
    (39, "Não consigo perceber quando alguém está flertando comigo.", "Social", False),
    (40, "Costumo focar intensamente em um assunto específico.", "Interesses", False),
    (41, "Mantenho listas de coisas que me interessam, mesmo sem utilidade prática.", "Interesses", False),
    (42, "Quando me sinto sobrecarregado pelos sentidos, tenho que me isolar.", "Sensório", False),
    (43, "Gosto de conversar sobre as coisas com meus amigos.", "Social", True),
    (44, "Frequentemente fico inseguro sobre como agir em situações sociais.", "Social", False),
    (45, "Pode ser muito difícil ler o rosto e os movimentos do corpo de alguém.", "Social", False),
    (46, "A mesma coisa (como roupas) pode parecer muito diferente para mim em momentos diferentes.", "Sensório", False),
    (47, "Sinto-me muito confortável em situações sociais.", "Social", True),
    (48, "Tento ser o mais prestativo possível com problemas alheios.", "Social", True),
    (49, "Disseram-me que tenho uma voz incomum (monótona ou aguda).", "Linguagem", False),
    (50, "Às vezes, um pensamento fica preso na minha mente e tenho que falar sobre ele.", "Interesses", False),
    (51, "Faço certas coisas com as mãos repetidamente (bater palpas, girar objetos).", "Sensório", False),
    (52, "Nunca me interessei pelo que a maioria das pessoas considera interessante.", "Interesses", False),
    (53, "Sou considerado uma pessoa que entende o sentimento dos outros.", "Social", True),
    (54, "Eu me dou bem com outras pessoas seguindo um conjunto de regras específicas.", "Social", False),
    (55, "É muito difícil para mim trabalhar e atuar em grupos.", "Social", False),
    (56, "É difícil mudar de assunto em uma conversa.", "Interesses", False),
    (57, "Às vezes, preciso tapar os ouvidos para bloquear ruídos.", "Sensório", False),
    (58, "Posso conversar e bater papo com as pessoas.", "Social", True),
    (59, "Às vezes, coisas que deveriam ser dolorosas não são.", "Sensório", False),
    (60, "Tenho dificuldade em saber quando é minha vez de falar.", "Social", False),
    (61, "Sou considerado um solitário por aqueles que me conhecem.", "Social", False),
    (62, "Normalmente falo com um tom de voz normal.", "Linguagem", True),
    (63, "Gosto que as coisas sejam exatamente as mesmas dia após dia.", "Interesses", False),
    (64, "Como fazer amigos e socializar são um mistério para mim.", "Social", False),
    (65, "Quando estou estressado, me acalmo balançando ou girando.", "Sensório", False),
    (66, "A frase 'Ele usa o coração na manga' não faz sentido para mim.", "Linguagem", False),
    (67, "Cheiros, texturas ou luzes brilhantes me deixam ansioso.", "Sensório", False),
    (68, "Eu sei quando alguém diz uma coisa, mas quer dizer outra.", "Social", True),
    (69, "Gosto de ficar sozinho o máximo que posso.", "Social", False),
    (70, "Mantenho meus pensamentos em pastas de arquivo na memória.", "Interesses", False),
    (71, "O mesmo som às vezes parece muito alto ou muito baixo.", "Sensório", False),
    (72, "Gosto de passar tempo comendo e conversando com família e amigos.", "Social", True),
    (73, "Não tolero coisas que não gosto (cheiros, sons).", "Sensório", False),
    (74, "Não gosto de ser abraçado ou segurado.", "Sensório", False),
    (75, "Tenho que seguir uma rotina conhecida quando vou a algum lugar.", "Interesses", False),
    (76, "É difícil descobrir o que as outras pessoas esperam de mim.", "Social", False),
    (77, "Gosto de ter amigos próximos.", "Social", True),
    (78, "As pessoas me dizem que eu dou muitos detalhes.", "Linguagem", False),
    (79, "Muitas vezes me dizem que faço perguntas embaraçosas.", "Social", False),
    (80, "Costumo apontar os erros dos outros.", "Social", False)
]

def calculate_raads_score(responses):
    """
    responses: dicionário vindo do formulário { 'q1': 'valor', 'q2': 'valor' ... }
    """
    points_map = {
        "Verdade agora e quando eu era jovem": 3,
        "Verdade só agora": 2,
        "Verdade apenas quando eu tinha menos de 16 anos": 1,
        "Nunca é verdade": 0
    }
    
    total = 0
    scores = {"Social": 0, "Linguagem": 0, "Sensório": 0, "Interesses": 0}
    
    for q_id, text, cat, is_reverse in questions_data:
        ans_text = responses.get(f"q{q_id}")
        if ans_text:
            val = points_map[ans_text]
            # Se for pergunta inversa (neurotípica), invertemos o valor: 3 vira 0, 0 vira 3.
            final_val = (3 - val) if is_reverse else val
            
            total += final_val
            scores[cat] += final_val
            
    return total, scores