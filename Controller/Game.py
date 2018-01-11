from Controller.LoadGame import load_game_characters
from Controller.Welcome import welcome
class Game:
    def __init__(self):
        currentCharacters, deadCharacters = load_game_characters()
