from Controller.LoadGame import load_game_characters
from Controller.Welcome import welcome

currentCharacters, deadCharacters = load_game_characters()
welcome()

