# Menu to start game


import time

from classKnight import Knight
from classWizard import Wizard

from SaveGame import save_game_current
from classThief import Thief


def menuToStartGame():
    print ("\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Thief \n""4. Show more info \n""5. Go back to start menu \n""6. Close \n")
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
    time.sleep(0.3)
    print("   / /     \  | ")
    time.sleep(0.3)
    print("_.'  \'-'  /  |   ")
    time.sleep(0.3)
    print("`----'`=-='   ' ")
    time.sleep(0.3)
    print("*****Passive Ability")
    time.sleep(0.3)
    print("Light Rail. The wizard can make the monster blind and has")
    time.sleep(0.3)
    print("therefore always 80% chance of flying from battles.")
    try:
        select = int(input("Press 1 to return "))
    except ValueError:
        print('Error')
    if select == 1:
        createMenu()

def showInfoKnight():
    print('    KNIGHT   /    ___Stats___')
    time.sleep(0.3)
    print('      ,~~   /     Initiative = 5  ')
    time.sleep(0.3)
    print('  _  <=)  _/_     Endurance = 9')
    time.sleep(0.3)
    print(' /I\.="==.{>      Attack = 6')
    time.sleep(0.3)
    print(" \I/-\T/-         Agility = 4")
    time.sleep(0.3)
    print('     /_\    _   ')
    time.sleep(0.3)
    print("   _// \\\_  ")
    time.sleep(0.3)
    print('*****Passive Ability*****')
    time.sleep(0.3)
    print('Shield block: The knight always blocks the first attack in a fight with his shield')
    print('')
    time.sleep(1)
    try:
        select = int(input(" Press 1 to return "))
    except ValueError:
        print('Error')
    if select == 1:
        createMenu()

def showInfoThief():
    print('THIEF//|\  ___Stats___')
    time.sleep(0.3)
    print("    //&')  Initiative = 7 ")
    time.sleep(0.3)
    print('     '')( ) Endurance = 5')
    time.sleep(0.3)
    print('     ((_)  Attack = 5')
    time.sleep(0.3)
    print('     )( (  Agility = 7')
    time.sleep(0.3)
    print(' <###(](=M=)')
    time.sleep(0.3)
    print('     (()   ')
    time.sleep(0.3)
    print('     (( ) ')
    time.sleep(0.3)
    print('     ((__,) ')
    time.sleep(0.3)
    print('*****Passive Ability*****')
    time.sleep(0.3)
    print('Critical hit: The thief has a 25% chance to hit a critical hit which deals double damage.')
    time.sleep(1)
    try:
        select = int(input("Press 1 to return "))
    except ValueError:
        print('Error')
    if select == 1:
        createMenu()

