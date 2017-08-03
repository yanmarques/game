import os

class Settings():

    global __dificulty
    __dificulty = 1

    global __repeated_numbers
    __repeated_numbers = 'false'

    def __init__(self):
        self.__configs = []
        self.__config_file = "config.csv"

    def get_config(self):
        return self.__configs

    def initialize_config(self):
        config_file_exists = os.path.isfile(self.__config_file)
        lines = None

        if config_file_exists:
            lines = self.read_config_file()
        else:
            lines = self.write_config_file(self.configuration())

        for line in lines:
            key_value = line.split("=")
            self.__configs.append(key_value)

    def update_config(self):
        lines = self.read_config_file()

        counter = 0
        for line in lines:
            key_value = line.split("=")
            self.__configs[counter] = key_value

            counter += 1

    def read_config_file(self):
        archive = None
        lines = []
        try:
            archive = open(self.__config_file, "r")
            for line in archive:
                lines.append(line)

            return lines
        except IOError as erro:
            print(erro)
        finally:
            if archive is not None:
                archive.close()

    def write_config_file(self, text):
        archive = None
        try:
            archive = open(self.__config_file, "w")
            for line in text:
                archive.write(line)

            return text
        except IOError as erro:
            print(erro)
        finally:
            if archive is not None:
                archive.close()

    def configuration(self, new_configs = None):
        global __dificulty
        global __repeated_numbers

        if new_configs is None:
            configs = ["dificulty={}\n".format(__dificulty), "repeated_numbers={}".format(__repeated_numbers)]
            return configs

        configs = self.read_config_file()
        value = new_configs.split("=")
        new_configs = None

        if value[0] == "dificulty":
            new_configs = ["{}={}\n".format(value[0], value[1]), configs[1]]
        elif value[0] == "repeated_numbers":
            new_configs = [configs[0], "{}={}".format(value[0], value[1])]

        return new_configs

    def configure(self):
        choice = None

        while choice != '3':
            print ("1 para {}". format(self.__configs[0][0]), "| 2 para {}". format(self.__configs[1][0]), "| 3 para voltar")
            choice = input()

            new_configs = None

            if choice == '1':
                new = input("Digite o novo valor da dificuldade > ")
                new_configs = 'dificulty={}'.format(new)

            if choice == '2':
                new = input("Digite 1 para repetir os numeros| Digite 2 para nao repetir os numeros > ")
                if new == '1':
                    new_configs = 'repeated_numbers={}'.format('true')
                elif new == '2':
                    new_configs = 'repeated_numbers={}'.format('false')

            self.update_config()
            self.write_config_file(self.configuration(new_configs))

            if choice == '3':
                return False

            return True        
