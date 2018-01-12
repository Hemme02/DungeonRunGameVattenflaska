from SaveGame import save_game_current
from SaveGame import save_game_dead
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

    def save_characters(self):
        save_game_current(self.currentCharacters)
        save_game_dead(self.deadCharacters)
