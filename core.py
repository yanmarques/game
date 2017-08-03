import os
import random
from levels import Levels

class Core():

    global __numbers
    __numbers = []

    def __init__(self, settings):
        self.settings = settings

    def up(self, dificulty = None, level = 0, attempt = 1):
        new_level = level + 1

        if dificulty == None:
            dificulty = int(self.settings.get_config()[0][1])

        total_attempts = 3

        if dificulty > 20:
            total_attempts = 10

        elif dificulty > 10:
            total_attempts = 6

        value = None
        if level == 0:
            value = (10 * dificulty) / attempt
            self.start(new_level, int(value), total_attempts)
        else:
            value = ((new_level * 10) * dificulty) / attempt
            self.start(new_level, int(value), total_attempts, True)

    def start(self, level, value, attempts, status = False):
        global __configs
        random_number = self.random_number(value, self.settings.get_config()[1][1])
        counter = 1

        os.system("clear")

        if status is True:
            print ("*** Voce acertou! ***")
            print ("Parabens, voce avancou para a fase {}\n" . format(level))

        print ("Fase {}" . format(level))
        status = False

        while counter <= attempts and status is False:
            print ("Tentativa {} de {}" . format(counter, attempts))

            chute_str = None
            chute = None

            status_input = False
            while status_input is False:
                try:
                    chute_str = input("Digite o numero > ")

                    if (chute_str == ":q"):
                        os.system("clear")
                        return

                    chute = int(chute_str)
                    status_input = True
                except ValueError:
                    print ("Por favor digite um numero valido")

            if chute == random_number:
                status = True
            else:
                print("Quase...")
                if chute < random_number:
                    print ("Seu chute foi menor que o numero aleatorio")
                else:
                    print ("Seu chute foi maior que o numero aleatorio")

            counter += 1

        if status == True:
            dificulty = int(self.settings.get_config()[0][1])
            self.up(dificulty=dificulty, level=level, attempt=counter - 1)
        else:
            os.system("clear")
            print ("O numero era {}" . format(random_number))
            print("Voce nao conseguiu, por favor tente novamente...")
            return

    def random_number(self, value, config):
        global __numbers

        random_number = random.randrange(0, value)
        if config == 'true':
            return random_number

        status = False

        while status is False:
            if random_number not in __numbers:
                status = True
            else:
                random_number = random.randrange(0, value)

        __numbers.append(random_number)
        return random_number
