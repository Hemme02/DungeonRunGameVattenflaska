from Controller.Game import Game
from Controller.LoadGame import load_game_characters
from Controller.Menu import createMenu
from Controller.Clear import clear_screen
from Model.classWizard import Wizard
from Model.classKnight import Knight
from Model.classThief import Thief

import time


def welcomeMenu ():
    print('******************************\n'"Welcome to our Dungeon Run game!" '\n******************************\n')
    time.sleep(0.5)
    clear_screen()
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
    welcome()
    return

def welcome():
    print( "\nDungeon Run\nPlease choose one of following:\n" "1. Create a character & start an adventure\n""2. Continue with your saved character \n""3. Close program\n")

    while True:
        choice = input("Your choice: ")
        if choice == "1":
            createMenu()
        elif choice == "2":
            select_character()
        elif choice == "3":
            exit()
            answer = input("Do you really want to exit?:")
            if answer.lower() == ("no"):
                print("Ok, carry on then")
            if answer.lower() == ("yes"):
                sys.exit()


        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3")
            welcome()

def menuToStartGame():
    print ("\nStart Adventure\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Theif \n\n""Or""\n""4. Show more info \n""5. Go back to start menu \n""6. Close program \n")
    return

def createCharacter(number):
    character_name = input("Your name for the character: ")

    for character in (newGame.currentCharacters):
        if character.name == character_name:
            print ("Name occupied. Try again")
            createCharacter(number)

    if number =="1":
        new_wizard = Wizard(character_name)
        newGame.add_character(new_wizard)

    elif number =="2":
        new_Knight = Knight(character_name)
        newGame.add_character(new_Knight)

    elif number == "3":
        new_thief = Thief(character_name)
        newGame.add_character(new_thief)

def createMenu ():
    menuToStartGame()

    while True:
        choice_start_game = input("Your choice: ")

        # 1.Wizard
        if choice_start_game == "1":
            createCharacter("1")

        # 2.Knight
        elif choice_start_game == "2":
            createCharacter("2")

        # 3.Thief
        elif choice_start_game == "3":
            createCharacter("3")

        # 4.Show more info about characters
        elif choice_start_game == "4":
            print(" Info ")

       # Back to start menu
        elif choice_start_game == "5":
            welcome()

        # Close
        elif choice_start_game == "6":
            answer = input("Do you really want to exit?:")
            if answer.lower() == ("no"):
                print("Ok, carry on then")
            if answer.lower() == ("yes"):
                sys.exit()

def select_character():
    if len(newGame.currentCharacters) != 0:
        print("Select character:")
        num = 1
        for character in newGame.currentCharacters:
            print(str(num)+":  "+character.name)
            num += 1
        print(str(num) + ":  Go Back")
        try:
            while True:
                character_choice =int(input("\nYour choice: "))
                if character_choice > (len(newGame.currentCharacters)+2) or character_choice <= 0:
                    print("Wrong choice")
                    continue
                elif(character_choice == len(newGame.currentCharacters)+1):
                    welcomeMenu()
                else:
                    newGame.active_character = newGame.currentCharacters[character_choice-1]
                    print(newGame.active_character.name)


        except(ValueError):
            print("Wrong choice")
            welcomeMenu()



currentCharacters, deadCharacters = load_game_characters()
newGame = Game(currentCharacters, deadCharacters)
welcomeMenu()

