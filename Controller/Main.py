import sys

from Controller.Game import Game
from Controller.LoadGame import load_game_characters
from Controller.Menu import createMenu
from Controller.Clear import clear_screen
from Model.classWizard import Wizard
from Model.classKnight import Knight
from Model.classThief import Thief

import time


def welcomeMenu ():
    print('________                                             __________    ')
    print('\______ \  __ __  ____    ____   ____  ____   ____   \______   \__ __  ____   ')
    print(' |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \   |       _/  |  \/    \ ')
    print(' |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \  |    |   \  |  /   |  \ ')
    print('/_______  /____/|___|  /\___  / \___  >____/|___|  /  |____|_  /____/|___|  / ')
    print('        \/           \//_____/      \/           \/          \/           \/ ')
    time.sleep(1)
    print("_____________________________________________________________________________________________")
    print('This game is a hardcore roguelike dungeon crawler, your character will be deleted upon death.')
    time.sleep(0.5)
    print('**** Developers: Jens, Belkiz, Johanna, Uzko, Sanju and Simon. *****')
    print('______________________________________________________________________________________________')
    time.sleep(2.5)
    clear_screen()
    print ("\nPlease choose one of following:\n" "1. Create a character & start an adventure\n""2. Continue with your saved character \n""3. Close program\n4. Show menu\n")
    return

def welcome():
    print ('******************************\n'"Welcome to our Dungeon Run game!" '\n******************************\n')
    time.sleep(0.5)
    clear_screen()
    welcomeMenu()

    while True:
        choice = input("Your choice: ")
        if choice == "1":
            createMenu(newGame)
        elif choice == "2":
            break
            #Load saved character

        elif choice == "3":
            answer = input("Do you really want to exit?:")
            if answer.lower() == ("no"):
                print("Ok, carry on then")
            if answer.lower() == ("yes"):
                sys.exit()


        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3 or push 4 to see the menu again")



def menuToStartGame():
    print ("\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Theif \n""4. Show more info \n""5. Go back to start menu \n""6. Close \n")
    return



def createCharacter(number, newGame):

    character_name = input("Your name for the character: ")
    if number =="1":
        new_wizard = Wizard(character_name)
        newGame.add_character(new_wizard)

    elif number =="2":
        new_Knight = Knight(character_name)
        newGame.add_character(new_Knight)

    elif number == "3":
        new_thief = Thief(character_name)
        newGame.add_character(new_thief)


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
            answer = input("Do you really want to exit?:")
            if answer.lower() == ("no"):
                print("Ok, carry on then")
            if answer.lower() == ("yes"):
                sys.exit()




currentCharacters, deadCharacters = load_game_characters()
newGame = Game(currentCharacters, deadCharacters)
welcome()

