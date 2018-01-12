import pickle


def save_game_current(list_of_characters):
    pickle.dump(list_of_characters, open("AliveCharacters.p", "wb"))


def save_game_dead(list_of_characters):

    pickle.dump(list_of_characters, open("DeadCharacters.p", "wb"))
    save_good = True



