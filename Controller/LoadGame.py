import pickle
import io


def load_game_characters():

    try:
        current_char = pickle.load(open("SaveFiles/AliveCharacters.p", "wb"))
    except(io.UnsupportedOperation, FileNotFoundError):
        current_char = []

    try:
        dead_char = pickle.load(open('SaveFiles/DeadCharacters.p', "wb"))
    except(io.UnsupportedOperation, FileNotFoundError):
        dead_char = []

    return(current_char, dead_char);


print(load_game_characters())