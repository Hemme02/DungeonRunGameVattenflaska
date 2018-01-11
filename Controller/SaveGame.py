import pickle


def save_game_current(list_of_characters):
    pickle.dump(list_of_characters, open("SaveFiles/AliveCharacters.p", "wb"))
    print("save gjord")


def save_game_dead(list_of_characters):

    pickle.dump(list_of_characters, open("SaveFiles/DeadCharacters.p", "wb"))
    save_good = True



