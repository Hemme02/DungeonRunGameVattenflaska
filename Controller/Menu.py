# Menu to start game


from Model.classWizard import Wizard
from Model.classKnight import Knight
from Model.classThief import Thief
from Controller.SaveGame import save_game_current
import time


def menuToStartGame():
    print ("\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Theif \n""4. Show more info \n""5. Go back to start menu \n""6. Close \n")
    return



def createCharacter(number, newGame):

    character_name = input("Your name for the character: ")
    if number =="1":
        new_wizard = Wizard(character_name)
        newGame.currentCharacters.append(new_wizard)
        save_game_current(newGame.currentCharacters)

    elif number =="2":
        new_Knight = Knight(character_name)
        newGame.currentCharacters.append(new_Knight)
        save_game_current(newGame.currentCharacters)

    elif number == "3":
        new_thief = Thief(character_name)
        newGame.currentCharacters.append(new_thief)
        save_game_current(newGame.currentCharacters)



def createMenu (_newGame):

    print ("Start the adventure:")
    print("Menu")
    menuToStartGame()


    while True:


        choice_start_game = input("Your choice: ")

        # 1.Wizard
        if choice_start_game == "1":
            createCharacter("1", _newGame)

        # 2.Knight
        elif choice_start_game == "2":
            createCharacter("2", _newGame)

        # 3.Thief
        elif choice_start_game == "3":
            createCharacter("3", _newGame)

        # 4.Show more info about characters
        elif choice_start_game == "4":
            print(" Info ")

       # Back to start menu
        elif choice_start_game == "5":
            break

        # Close
        elif choice_start_game == "6":
            exit()

        else:
            print(" Try again ! ")


def showInToWizard():
    print('Wizard  ,    _   Stats  ')
    time.sleep(0.3)
    print('       /|   | |  initiative = 6   ')
    time.sleep(0.3)
    print('      _/_\_  >_< endurance = 4   ')
    time.sleep(0.3)
    print("     .-\-/.   |  attack = 9 ")
    time.sleep(0.3)
    print("    /  | | \_ |  agility = 5  ")
    time.sleep(0.3)
    print("    \ \| |\__(/")
    time.sleep(0.3)
    print("    /(`---')  |   ")
    print("   / /     \  | ")
    print("_.'  \'-'  /  |   ")
    print("`----'`=-='   ' ")
    time.sleep(0.3)
    print("*****Passive Ability")
    print("Light Rail. The wizard can make the monster blind and has")
    print("therefore always 80% chance of flying from battles.")

showInToWizard()

