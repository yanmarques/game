import random
import os
import time

def game_core(fase, valor, tentativas, status = False):
    numero_aleatorio = random.randrange(0, valor)
    counter = 1

    os.system("clear")

    if status is True:
        print ("Voce acertou!")
        print ("*************")
        print ("Parabens, voce avancou para a fase {}" . format(fase))

    print ("Fase {}" . format(fase))
    status = False

    while counter <= tentativas and status is False:
        print ("Tentativa {} de {}" . format(counter, tentativas))

        chute_str = None
        chute = None

        status_input = False
        while status_input is False:
            try:
                chute_str = input("Digite o numero > ")

                if (chute_str == ":q"):
                    return

                chute = int(chute_str)
                status_input = True
            except ValueError:
                print ("Por favor digite um numero valido")

        if chute == numero_aleatorio:
            status = True
        else:
            print("Quase...")
            if chute < numero_aleatorio:
                print ("Seu chute foi menor que o numero aleatorio")
            else:
                print ("Seu chute foi maior que o numero aleatorio")

        counter += 1

    if status == True:
        avanca_fase(fase, counter - 1)
    else:
        print ("O numero era {}" . format(numero_aleatorio))
        print("Voce nao conseguiu, por favor tente novamente...")
        return

def init():
    escolha = None

    while escolha != 'exit':
        print ("Para mais informacoes digite 'help', ou clique ENTER para comecar o jogo")
        print ("Para sair digite 'exit', para limpar campo digite 'clear'")
        escolha = input()

        if escolha == "":
             game_core(1, 10, 3)

        if escolha == "help":
            help_game()

        if escolha == "clear":
            os.system("clear")

    print ("Ate logo...")

def help_game():
    escolha = None

    while escolha is None:
        print ("******* Jogo da Advinhacao em Python *******")
        print ("O objetivo do jogo e adivinhar um numero aleatorio. Na primeira fase sera um numero aleatorio entre 0 e 10.")
        print ("Quando voce acerta voce avanca de fase, dessa forma aumenta o numero de opcoes de numeros aleatorios.")
        print ("A qualquer momento do jogo voce pode voltar para o menu principal digitando ':q' em qualquer lugar.")
        print ("Se voce entendeu clique ':q' para mostrar que sim e sair :) ")
        escolha = input()

def avanca_fase(fase, tentativa):
    new_fase = fase + 1
    dificuldade = (12 / tentativa)
    valor = (new_fase * 10) * dificuldade

    tentativas = 3

    if dificuldade >= 12.0:
        tentativas = 8

    elif dificuldade >= 6.0:
        tentativas = 5

    game_core(new_fase, valor, tentativas, True)

print ("*************************************\n")
print ("BEM VINDO")

init()
