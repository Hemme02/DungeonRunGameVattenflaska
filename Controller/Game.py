from Controller.SaveGame import save_game_current

class Game:
<<<<<<< HEAD
    def __init__(self):
        currentCharacters, deadCharacters = load_game_characters()
=======

    active_character = None
    currentCharacters = []
    deadCharacters = []
    def __init__(self, currentCharacters, deadCharacters):
        self.currentCharacters = currentCharacters
        self.deadCharacters = deadCharacters

    def add_character(self, newChar):
        self.currentCharacters.append(newChar)
        save_game_current(self.currentCharacters)
>>>>>>> cca8559608ca9654d72b5fdd4c8bb8310075a0fb
