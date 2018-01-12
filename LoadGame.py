import pickle
import io

def load_game_characters():

    try:
        current_char = pickle.load(open("AliveCharacters.p", "rb"))
    except(io.UnsupportedOperation, FileNotFoundError, EOFError):
        current_char = []

    try:
        dead_char = pickle.load(open('DeadCharacters.p', "rb"))
    except(io.UnsupportedOperation, FileNotFoundError, EOFError):
        dead_char = []

    return(current_char, dead_char)