import sys
import time

from Game import Game
from LoadGame import load_game_characters
from classKnight import Knight
from classWizard import Wizard

from Clear import clear_screen
from classThief import Thief


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
    print('**** Developers: Jens, Belkiz, Johanna, Usko, Sanju and Simon. *****')
    print('______________________________________________________________________________________________')
    time.sleep(2.5)

    welcome()
    return

def welcome():
    clear_screen()
    print( "\nDungeon Run\nPlease choose one of following:\n" "1. Create a character & start an adventure\n""2. Continue with your saved character \n""3. Close program\n")

    while True:
        choice = input("Your choice: ")
        if choice == "1":
            createMenu()
        elif choice == "2":
            select_character()
        elif choice == "3":
            answer = input("Do you really want to exit? yes/no:")
            if answer.lower() == ("yes"):
                sys.exit()
            else:
                welcome()

        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3")
            input("Press any key to continue")
            welcome()

def menuToStartGame():
    clear_screen()
    print ("\nStart Adventure\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Thief \n\n""Or""\n""4. Show more info \n""5. Go back to start menu \n""6. Close program \n")
    return

def createCharacter(number):
    while True:
        character_name = input("Your name for the character: ")
        name_occupied = True
        for character in (newGame.currentCharacters):
            if character.name == character_name:
                print ("Name occupied. Try again")
                name_occupied = False
                createCharacter(number)
                break
        break

    if name_occupied:
        if number =="1":
            new_wizard = Wizard(character_name)
            newGame.add_character(new_wizard)
            print("Charachter created. Quiting")
            exit()

        elif number =="2":
            new_Knight = Knight(character_name)
            newGame.add_character(new_Knight)
            print("Charachter created. Quiting")
            exit()

        elif number == "3":
            new_thief = Thief(character_name)
            newGame.add_character(new_thief)
            print("Charachter created. Quiting")
            exit()

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
            more_info()

       # Back to start menu
        elif choice_start_game == "5":
            welcome()

        # Close
        elif choice_start_game == "6":
            answer = input("Do you really want to exit? yes/no:")
            if answer.lower() == ("yes"):
                sys.exit()
            else:
                welcome()

def select_character():
    clear_screen()
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
                    print("Character selected:" + newGame.active_character.name)
                    exit()


        except(ValueError):
            print("Wrong choice")
            welcomeMenu()

def more_info():
    clear_screen()
    print("Select which character you want to know more of:")
    print("\n 1. Wizard\n 2. Knight\n 3. Thief\n 4. Go back")
    info_choice = input("Your choice: ")

    def showInToWizard():
        clear_screen()
        print('WIZARD  ,    _   Stats  ')
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
        print("therefore always 80% chance of fleeing from battles.")
        input("Press key to continue")
        more_info()

    def showInfoKnight():
        clear_screen()
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
        input("Press key to continue")
        more_info()

    def showInfoThief():
        clear_screen()
        print('THIEF//|\  ___Stats___')
        time.sleep(0.3)
        print("     //&')  Initiative = 7 ")
        time.sleep(0.3)
        print('      '')( ) Endurance = 5')
        time.sleep(0.3)
        print('      ((_)  Attack = 5')
        time.sleep(0.3)
        print('      )( (  Agility = 7')
        time.sleep(0.3)
        print('  <###(](=M=)')
        time.sleep(0.3)
        print('      (()   ')
        time.sleep(0.3)
        print('      (( ) ')
        time.sleep(0.3)
        print('      ((__,) ')
        time.sleep(0.3)
        print('*****Passive Ability*****')
        time.sleep(0.3)
        print('Critical hit: The thief has a 25% chance to hit a critical hit which deals double damage.')
        time.sleep(1)
        input("Press key to continue")
        more_info()

    if info_choice == "1":
        showInToWizard()
    elif info_choice == "2":
        showInfoKnight()
    elif info_choice == "3":
        showInfoThief()
    elif info_choice == "4":
        createMenu()
    else:
        print("Wrong choice")
        more_info()

currentCharacters, deadCharacters = load_game_characters()
newGame = Game(currentCharacters, deadCharacters)
welcomeMenu()

