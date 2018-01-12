from SaveGame import save_game_current
from classWizard import Wizard


class Game:
    active_character = Wizard("Kim")
    currentCharacters = []
    deadCharacters = []

    def __init__(self, currentCharacters, deadCharacters):
        self.currentCharacters = currentCharacters
        self.deadCharacters = deadCharacters

    def add_character(self, newChar):
        self.currentCharacters.append(newChar)
        save_game_current(self.currentCharacters)
