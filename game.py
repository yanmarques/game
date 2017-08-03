import os
from core import Core
from settings import Settings

class Game():
    def __init__(self):
        self.settings = Settings()
        self.settings.initialize_config()
        self.init()
        self.help_file_name = "help.csv"

    def init(self):
        choice = None

        while choice != 'exit':
            print ("Para mais informacoes digite 'help', ou clique ENTER para comecar o jogo")
            print ("Para sair digite 'exit', para limpar campo digite 'clear'")
            print ("Para mudar as configuracoes digite 'config'")
            choice = input()

            if choice == "":
                 self.play()

            if choice == "help":
                self.help_game()

            if choice == "clear":
                os.system("clear")

            if choice == "config":
                configure = self.settings.configure()
                os.system("clear")
                if configure is True:
                    print ("*** Sua configuracao foi atualizada com sucesso. ***\n")

        print ("Ate logo...")

    def play(self):
        return Core(self.settings).up()

    def help_game(self):
        choice = None
        archive = None
        while choice != ":q":
            try:
                archive = open(self.help_file_name, "r")

                for linha in archive:
                    print (linha)

            except IOError as erro:
                print (erro)
            finally:
                if archive is not None:
                    archive.close()

            choice = input()
