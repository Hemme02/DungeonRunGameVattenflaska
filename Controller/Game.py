from Controller.SaveGame import save_game_current

class Game:

    active_character = None
    currentCharacters = []
    deadCharacters = []
    def __init__(self, currentCharacters, deadCharacters):
        self.currentCharacters = currentCharacters
        self.deadCharacters = deadCharacters

    def add_character(self, newChar):
        self.currentCharacters.append(newChar)
        save_game_current(self.currentCharacters)