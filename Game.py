from SaveGame import save_game_current
from SaveGame import save_game_dead
from SaveGame import save_ai

class Game:
    active_character = None
    currentCharacters = []
    deadCharacters = []
    aiCharacters = []

    def __init__(self, currentCharacters, deadCharacters, aiCharacter):
        self.currentCharacters = currentCharacters
        self.deadCharacters = deadCharacters
        self.aiCharacters = aiCharacter

    def add_character(self, newChar):
        self.currentCharacters.append(newChar)
        save_game_current(self.currentCharacters)
        self.active_character = newChar

    def save_characters(self):
        save_game_current(self.currentCharacters)
        save_game_dead(self.deadCharacters)

    def add_character_ai(self, newAI):
        self.aiCharacters.append(newAI)
        save_ai(self.aiCharacters)

