class Levels():
    def __init__(self):
        self

    @staticmethod
    def up(game, dificulty, level, attempt = 1):
        new_level = level + 1
        value = (level * 10) * (dificulty / attempt)

        total_attempts = 3

        if dificulty > 20:
            total_attempts = 10

        elif dificulty > 10:
            total_attempts = 6

        game.start(level, int(value), total_attempts, True)
