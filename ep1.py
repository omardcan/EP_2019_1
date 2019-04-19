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

with open("treasures.txt", 'r') as aa:
    treasures_dict = json.loads(aa.read())


def carregar_cenarios():
    with open('cenarios.json', 'r') as aa:
        cenarios = json.loads(aa.read())
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

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

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir
        # o cenário atual.
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

        inv_or_mov = input("")
        print('')
        
        if inv_or_mov == "0":
            for i in player["inventario"]:
                print(i)



        elif inv_or_mov == "1":
            opcoes = cenario_atual['opcoes']
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                game_over = True
            else:

                # Aluno B: substitua este comentário e a linha abaixo pelo código
                # para pedir a escolha do usuário.
                print('')
                for e in opcoes:
                    print(str(e)+ ": " + str(opcoes[e]))
                escolha = input("Você decidi ir para: ")
                print('')


                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
