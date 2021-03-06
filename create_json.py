import json

cenarios = {
    "inicio": {
        "titulo": "Saguao do perigo",
        "descricao": "Voce esta no saguao de entrada do insper",
        "opcoes": {
            "andar professor": "Tomar o elevador para o andar do professor",
            "biblioteca": "Ir para a biblioteca",
            "quarto andar": "Ir para o quarto andar"
        }
    },
    "andar professor": {
        "titulo": "Andar do desespero",
        "descricao": "Voce chegou ao andar da sala do seu professor",
        "opcoes": {
            "inicio": "Tomar o elevador para o saguao de entrada",
            "professor": "Falar com o professor",
            "quarto andar": "Ir para o quarto andar"
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


cenarios["quarto andar"] = {}
cenarios["quarto andar"]["titulo"] = "Casa 2.0"
cenarios["quarto andar"]["descricao"] = "Você esta na sua nova casa"
cenarios["quarto andar"]["opcoes"] = {}
cenarios["quarto andar"]["opcoes"]["inicio"] = "Voltar para o saguao de entrada"
cenarios["quarto andar"]["opcoes"]["maquina"] = "Ir comprar algo na maquina"
cenarios["quarto andar"]["opcoes"]["andar professor"] = "Tomar o elevador para o andar do professor"

cenarios["maquina"] = {}
cenarios["maquina"]["titulo"] = "Maquina de Comida/Bebida"
cenarios["maquina"]["descricao"] = "Não sei por que você decidiu ir comprar algo, sendo q seu ep ta uma merda ainda, mas já que estamos aqui..."
cenarios["maquina"]["opcoes"] = {}
cenarios["maquina"]["opcoes"]["sair"] = "Você para de olhar a maquina"







string_cenarios = json.dumps(cenarios, sort_keys=False, indent=4)
with open('cenarios.json', 'w') as arquivo:
    arquivo.write(string_cenarios)


player = {}
player["vida"] = 90
player["arma"] = "punhos"
player["velocidade"] = 10
player["Dinheiro"] = 100
player["inventario"] = {}
player["inventario"]["poção de vida"] = [2]
player["inventario"]["RedBull"] = [2]
player["inventario"]["Armas"] = {}
player["inventario"]["Armas"]["punho"] = 10
player["inventario"]["Armas"]["notebook"] = 20

string_player = json.dumps(player, sort_keys=False, indent=4)
with open('player.json', 'w') as arquivo:
    arquivo.write(string_player)


enemys = {}

enemys["professores"] = {}
enemys["professores"]["Raul"] = {}
enemys["professores"]["Raul"]['vida'] = 70
enemys["professores"]["Raul"]['dano'] = 15
enemys["professores"]["Raul"]['velocidade'] = 8

enemys['alunos'] = {}
enemys['alunos']["Duarte"] = {}
enemys["alunos"]["Duarte"]['vida'] = 40
enemys["alunos"]["Duarte"]['dano'] = 10
enemys["alunos"]["Duarte"]['velocidade'] = 20

string_enemys = json.dumps(enemys, sort_keys=False, indent=4)
with open('enemys.json', 'w') as arquivo:
    arquivo.write(string_enemys)


treasures_items = ["poção de vida", "RedBull"]

string_treasures_items = json.dumps(treasures_items, sort_keys=False, indent=4)
with open('treasures_items.json', 'w') as arquivo:
    arquivo.write(string_treasures_items)

treasures_weapons = {}
treasures_weapons["espada de papelão"] = 17
treasures_weapons["estilete do FabLab"] = 30

string_treasures_weapons = json.dumps(treasures_weapons, sort_keys=False, indent=4)
with open('treasures_weapons.json', 'w') as arquivo:
    arquivo.write(string_treasures_weapons)


store = {}
store["RedBull"] = {}
store["RedBull"]["preco"] = 10
store["RedBull"]["quantidade"] = 5

store["poção de vida"] = {}
store["poção de vida"]["preco"] = 20
store["poção de vida"]["quantidade"] = 5

store["??????"] = {}
store["??????"]["preco"] = 500
store["??????"]["quantidade"] = 5
store["??????"]["dano"] = 120

string_store = json.dumps(store, sort_keys=False, indent=4)
with open('store.json', 'w') as arquivo:
    arquivo.write(string_store)
