# EP 2019-1: Escape Insper
#
# Alunos:
# - aluno A: Omar Dibo Calixto Afrange Neto, omardcan@al.insper.edu.br
# - aluno B: Elena De São Jose Santos, elenasjs@al.insper.edu.br
import random
import json

with open("player.json", 'r') as aa:
    player = json.loads(aa.read())

with open("enemys.json", 'r') as aa:
    enemys_dict = json.loads(aa.read())

with open("treasures_items.json", 'r') as aa:
    treasures_items_list = json.loads(aa.read())

with open("treasures_weapons.json", 'r') as aa:
    treasures_weapons_dict = json.loads(aa.read())

with open("store.json", 'r') as aa:
    store = json.loads(aa.read())

def carregar_cenarios():
    with open('cenarios.json', 'r') as aa:
        cenarios = json.loads(aa.read())
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

menu_combate = """
0- Correr
1- Bater
2- Poção de vida
3- RedBull
"""

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    speed_buff_timer = 0
    speed = player["velocidade"]

    combate = False

    cura = 30

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        if speed_buff_timer > 0:
            speed_buff_timer -= 1
        elif speed_buff_timer <= 0:
            player["velocidade"] = speed

        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual["titulo"])
        print('-'*len(cenario_atual['titulo']))
        print('')
        print(cenario_atual['descricao'])
        print('')
        print('')

        print("""
0- Abrir o inventario
1- Andar por ai
""")

        inv_or_mov = input("?: ")
        print('')

        if inv_or_mov == "0":
            print("Vida: " + str(player["vida"]))
            print("Dinheiro: " + str(player["Dinheiro"]))
            print("Arma: " + str(player["arma"]))
            print('')
            print("0- Voltar")

            a = 1
            for i in player["inventario"]:
                if len(player["inventario"][i]) == 1:
                    print(str(a) + "- " + str(i) + ": " + str(player["inventario"][i][0]))
                else:
                    print(str(a) + "- " + str(i) + ": ")
                    for e in player["inventario"][i]:
                        print("    -" + str(e))
                a += 1
            print('')
            opcao = input("?: ")
            print('')

            if opcao == "1":
                if player["inventario"]["poção de vida"][0] == 0:
                    print("Tu não tem poção animal")
                else:
                    player["inventario"]["poção de vida"][0] -= 1
                    print("Vida: " + str(player["vida"]) + "+" + str(cura))
                    player["vida"] += cura
                    print("Vida: " + str(player["vida"]))

            elif opcao == "2":
                if player["inventario"]["RedBull"][0] == 0:
                    print("Tu n tem RedBull animal")
                else:
                    player["inventario"]["RedBull"][0] -= 1
                    print("Tu ta no pique, mas quanto tempo durará?")
                    speed_buff = random.randint(5,10)
                    speed_buff_timer = random.randint(1,10)
                    player["velocidade"] += speed_buff

            elif opcao == "3":
                for i in player["inventario"]["Armas"]:
                    print("- " + str(i))
                escolha_arma = (input("?: "))
                if escolha_arma not in player["inventario"]["Armas"]:
                      escolha_arma = (input("digita certo animal: "))
                player["arma"] = escolha_arma

            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
            print('')


        elif inv_or_mov == "1":
            chance_enemy = random.randint(0,100)
            if chance_enemy <= 20:
                combate = True
                vezes_player = 1
                vezes_enemy = 1
                tipo_enemy = random.randint(0, len(enemys_dict["professores"]) + len(enemys_dict["alunos"])-1)
                if tipo_enemy < len(enemys_dict["professores"]):
                    enemy = enemys_dict["professores"]
                else:
                    enemy = enemys_dict["alunos"]

                for key, value in enemy.items():
                    print("A wild " + key + " apears")
                    nome = key

                if player["velocidade"] >= enemy[nome]["velocidade"]:
                    vez_player = True
                else:
                    vez_player = False


                if 2*player["velocidade"] <= enemy[nome]["velocidade"]:
                    vezes_enemy = 2

                print(menu_combate)
                opcao = input("?: ")
                while combate:
                    if player["velocidade"] >= 2*enemy[nome]["velocidade"]:
                        vezes_player = 2

                    if player["vida"] <= 0:
                        print("Você morreu que nem o perdedor que é")
                        combate = False
                        game_over = True

                    if vez_player:
                        if vezes_player == 1:
                            vez_player = False
                        else:
                            vezes_player -= 1

                        if opcao == "0":
                            if player["velocidade"] > enemy[nome]["velocidade"]:
                                print('Ufa, dessa vez foi por pouco')
                                combate = False
                            else:
                                print(nome + " é mais rapido do que você pensava")

                        if opcao == "1":
                            arma_player = player["arma"]
                            enemy[nome]["vida"] -= player["inventario"]["Armas"][arma_player]

                        if enemy[nome]["vida"] <= 0:
                            combate = False
                            consumivel_or_arma = random.randint(0,2)
                            if consumivel_or_arma <= 1:
                                loot = treasures_items_list[random.randint(0,len(treasures_items_list)-1)]
                            else:
                                loot = random.choice(list(treasures_weapons_dict.items()))[0]

                            money = random.randint(5,20)
                            player["Dinheiro"] += money


                            print("No corpo morto do " + nome + " você encontra: " + loot + " e " + str(money) + "$")
                            if loot == "poção de vida":
                                player["inventario"]['poção de vida'][0] += 1
                            elif loot == "RedBull":
                                player["inventario"]['RedBull'][0] += 1

                            else:
                                player["inventario"]["Armas"][loot] = treasures_weapons_dict[loot]

                        if opcao == "2":
                            if player["inventario"]["poção de vida"][0] == 0:
                                print("Tu não tem poção animal")
                            else:
                                player["inventario"]["poção de vida"][0] -= 1
                                print("Vida: " + str(player["vida"]) + "+" + str(cura))
                                player["vida"] += cura
                                print("Vida: " + str(player["vida"]))

                        if opcao == "3":
                            if player["inventario"]["RedBull"][0] == 0:
                                print("Tu n tem RedBull animal")
                            else:
                                player["inventario"]["RedBull"][0] -= 1
                                print("Tu ta no pique, mas quanto tempo durará? E isso lá é hora de se tomar RedBull")
                                speed_buff = random.randint(5,10)
                                speed_buff_timer = random.randint(1,10)
                                player["velocidade"] += speed_buff

                        if combate:
                            print(menu_combate)
                            opcao = input("?: ")

                    else:
                        if vezes_enemy == 1:
                            vez_player = True
                        else:
                            vezes_enemy -= 1
                        player["vida"] -= enemy[nome]["dano"]
                        print("Vida: " + str(player["vida"]))
                    print('')


            else:
                opcoes = cenario_atual['opcoes']
                if len(opcoes) == 0:
                    print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                    game_over = True

                else:

                    print('')
                    for e in opcoes:
                        print(str(e)+ ": " + str(opcoes[e]))
                    escolha = input("?: ")
                    print('')

                    if escolha in opcoes:
                        nome_cenario_atual = escolha
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True

                    if escolha == "maquina":
                        compras = True
                        while compras:
                            print("Dinheiro: " + str(player["Dinheiro"]))
                            print('')
                            for key, value in store.items():
                                print("- " + str(key) + ": " + str(value["preco"]) + "$")
                            opcao = input("?: ")
                            if opcao not in store:
                                compras = False
                            else:
                                if player["Dinheiro"] >= store[opcao]["preco"] and store[opcao]["quantidade"] > 0:
                                    player["Dinheiro"] -= store[opcao]["preco"]
                                    store[opcao]["quantidade"] -= 1

                                    if opcao == "poção de vida":
                                        player["inventario"]['poção de vida'][0] += 1

                                    elif opcao == "RedBull":
                                        player["inventario"]['RedBull'][0] += 1

                                    else:
                                        player["inventario"]["Armas"][opcao] = store[opcao]["dano"]
                                else:
                                    print("Acabou esse item na maquina")
        else:
            print("Sua indecisão foi sua ruína!")
            game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
