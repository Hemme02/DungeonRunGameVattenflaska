#lägg till clear funk
#smile
from Controller.Menu import createMenu
from Controller.Clear import clear_screen

import time

def cls():
    print("\n" * 100)

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

def welcome(newGame):
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
            exit()

        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3 or push 4 to see the menu again")
