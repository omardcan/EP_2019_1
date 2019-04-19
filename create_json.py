import json

cenarios = {
    "inicio": {
        "titulo": "Saguao do perigo",
        "descricao": "Voce esta no saguao de entrada do insper",
        "opcoes": {
            "andar professor": "Tomar o elevador para o andar do professor",
            "biblioteca": "Ir para a biblioteca"
        }
    },
    "andar professor": {
        "titulo": "Andar do desespero",
        "descricao": "Voce chegou ao andar da sala do seu professor",
        "opcoes": {
            "inicio": "Tomar o elevador para o saguao de entrada",
            "professor": "Falar com o professor"
        }
    },
    "professor": {
        "titulo": "O monstro do Python",
        "descricao": "Voce foi pedir para o professor adiar o EP. "
                     "O professor revelou que é um monstro disfarçado "
                     "e devorou sua alma.",
        "opcoes": {}
    },
    "biblioteca": {
        "titulo": "Caverna da tranquilidade",
        "descricao": "Voce esta na biblioteca",
        "opcoes": {
            "inicio": "Voltar para o saguao de entrada"
        }
    }
}

string_cenarios = json.dumps(cenarios, sort_keys=False, indent=4)
with open('cenarios.json', 'w') as arquivo:
    arquivo.write(string_cenarios)


player = {}
player["vida"] = 150
player["arma atual"] = "punhos"
player["velocidade"] = 10
player["inventario"] = {}
player["inventario"]["Dinheiro"] = 0
player["inventario"]["Poções de Vida"] = 0
player["inventario"]["Monsters"] = 0
player["inventario"]["Armas"] = ["punhos", "notebook"]

string_player = json.dumps(player, sort_keys=False, indent=4)
with open('player.json', 'w') as arquivo:
    arquivo.write(string_player)


enemys = {}

enemys["professores"] = {}
enemys["professores"]["Raul"] = {}
enemys["professores"]["Raul"]['vida'] = 200
enemys["professores"]["Raul"]['dano'] = 15
enemys["professores"]["Raul"]['velocidade'] = 8

enemys['alunos'] = {}
enemys['alunos']["Duarte"] = {}
enemys["alunos"]["Duarte"]['vida'] = 130
enemys["alunos"]["Duarte"]['dano'] = 10
enemys["alunos"]["Duarte"]['velocidade'] = 20

string_enemys = json.dumps(enemys, sort_keys=False, indent=4)
with open('enemys.json', 'w') as arquivo:
    arquivo.write(string_enemys)


treasures = ["cartão de crédito","espada de papelão","estilete do FabLab"]

string_treasures = json.dumps(treasures, sort_keys=False, indent=4)
with open('treasures.txt', 'w') as arquivo:
    arquivo.write(string_treasures)
