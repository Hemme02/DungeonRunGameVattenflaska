import pickle


def save_game_current(list_of_characters):
    save_good = False
    try:
        pickle.dump(list_of_characters, open("SaveFiles/AliveCharacters.p", "rb"))
        save_good = True
    except():
        pass
    finally:
        return save_good


def save_game_dead(list_of_characters):
    save_good = False
    try:
        pickle.dump(list_of_characters, open("SaveFiles/DeadCharacters.p", "rb"))
        save_good = True
    except():
        pass
    finally:
        return save_good


