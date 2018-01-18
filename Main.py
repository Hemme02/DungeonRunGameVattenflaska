import sys
import time
import winsound
from Game import Game
from LoadGame import load_game_characters
from classKnight import Knight
from classWizard import Wizard
from Clear import clear_screen
from classThief import Thief
from Map import Map

def welcomeMenu ():
    winsound.PlaySound("intro.wav", winsound.SND_ASYNC)
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
    time.sleep(0.5)
    input("Press any key to start the game")
    winsound.PlaySound(None, winsound.SND_PURGE)
    welcome()
    return

def finish():
    answer = input("Do you really want to exit? yes/no:")
    if answer.lower() == ("yes"):
        sys.exit()
    else:
        return False

def welcome():
    clear_screen()
    print( "\nMenu\nPlease choose one of following:\n" "1. Create a character & start an adventure\n""2. Continue with your saved character \n""3. Exit\n")

    while True:
        choice = input("Your choice: ")
        if choice == "1":
            createMenu()
        elif choice == "2":

            select_character()
        elif choice == "3":
            result = finish()
            if result == False:
                welcome()
        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3")
            input("Press any key to continue")
            welcome()

def menuToStartGame():
    clear_screen()
    print ("\nStart Adventure\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Thief \n\n""Or""\n""4. Show more info \n""5. Go back to start menu \n")
    return

def createCharacter(number):
    while True:
        character_name = input("Your name for the character: ")
        name_occupied = True
        for character in (newGame.currentCharacters):
            if character.name == character_name.lower:
                print ("Name occupied. Try again")
                name_occupied = False
                createCharacter(number)
                break
        break

    if name_occupied:
        if number =="1":
            new_wizard = Wizard(character_name)
            newGame.add_character(new_wizard)
            mapMenu(character_name, "1")

        elif number =="2":
            new_Knight = Knight(character_name)
            newGame.add_character(new_Knight)
            mapMenu(character_name, "2")

        elif number == "3":
            new_thief = Thief(character_name)
            newGame.add_character(new_thief)
            mapMenu(character_name, "3")

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

        else:
            print ("Wrong choise, try again")


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
                    mapMenu(newGame.active_character.name, newGame.active_character.to_String())

        except(ValueError):
            print("Wrong choice")
            welcomeMenu()
    else:
        print("No alive characters to choose from. You have to create a new one.")
        input("Press any key to continue")
        welcome()

def more_info():
    clear_screen()
    print("Select which option you want to know more of:")
    print("\n 1. Wizard\n 2. Knight\n 3. Thief\n 4. Map \n 5. Go back")
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

    def mapInfo():
        clear_screen()
        print( "Players can select map size for each new adventure as follows: ")
        print(" Small = 4x4, Medium = 5x5, Large = 8x8  ")
        print(" [X] = one room  ")
        input("Press key to continue")
        more_info()

    if info_choice == "1":
        showInToWizard()
    elif info_choice == "2":
        showInfoKnight()
    elif info_choice == "3":
        showInfoThief()
    elif info_choice == "4":
        mapInfo()
    elif info_choice == "5":
        createMenu()
    else:
        print("Wrong choice")
        more_info()

def startPosition(maxSize):

    while True:
        print("Choose starting position,\n 1: North West \n 2: North East. \n 3: South West \n 4: South East  ")
        choice = input("\n Your choice: ")
        if choice == "1":
            startingPos = 0,0

        elif choice == "2":
            startingPos = 0,maxSize -1
            print(maxSize)
        elif choice == "3":
            startingPos = maxSize - 1, 0
        elif choice == "4":
            startingPos = maxSize - 1, maxSize - 1
        else:
            print("Wrong Input.")

        return startingPos

# Menu: You are this character,  Which map size do you want to have?
def mapMenu(name, typeOfCharacter):
    clear_screen()

    def foorLoop():
        if typeOfCharacter == "1":
            return "Wizard"
        elif typeOfCharacter == "2":
            return "Knight"
        elif typeOfCharacter == "3":
            return "Thief"
        else:
            print("Error")

    result = foorLoop()

    print("\nYou are a "+result+" with name "+name+"\nSelect map size: \n" "1. Small \n""2. Medium  \n""3. Large  \n"" Or \n""4. Go back \n")
    size = mapSize()
    newMap = Map(size, startPosition(size))
    newMap.print_map()
    finish_dungeon()

def mapSize():
    while True:
        choice_size_map = input("\n Your choice: ")
        # Size small
        if choice_size_map == "1":
            return 4


        # Size medium
        elif choice_size_map == "2":
            return 5

        # Size large
        elif choice_size_map == "3":
            return 8

        # Go back
        elif choice_size_map == "4":
            createMenu()

        else:
            print("Try again")
            input("Press any key to continue")
            welcomeMenu()

def finish_dungeon():
    print("You manage to get out of the dungeon.\nYou are carrying "+ str(newGame.active_character.treasure_carried)+" gold with you")
    newGame.active_character.earn_treasure()
    newGame.save_characters()
    print("Your total wealth are now "+ str(newGame.active_character.treasure_saved)+" gold!")
    input("\n\nPress key to continue")
    while True:
        clear_screen()
        print("\n\nWhat do you want to do now?\n1.  Try another dungeon\n2.  Change character\n3.  Exit ")
        end_game_choice = input("Your choice :")
        if end_game_choice == "1":
            mapMenu(newGame.active_character.name, newGame.active_character.to_String())
        elif end_game_choice == "2":
            newGame.active_character = None
            welcome()
        elif end_game_choice == "3":
            result = finish()
            if result == False:
                welcome()
        else:
           input("Wrong choice. Press any key to continue!")

currentCharacters, deadCharacters = load_game_characters()
newGame = Game(currentCharacters, deadCharacters)
welcomeMenu()
size = mapSize()
Map(size,startPosition(size))


