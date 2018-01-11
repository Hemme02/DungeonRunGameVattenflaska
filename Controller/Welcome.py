#lägg till clear funk
#smile
from Controller.Menu import createMenu
def welcomeMenu ():
    print ("\nPlease choose one of following:\n" "1. Create a character & start an adventure\n""2. Continue with your saved character \n""3. Close program\n")
    return

def welcome():
    print ("Welcome to Dungeon Run")
    welcomeMenu()

    while True:
        choice = input("Your choice: ")
        if choice == "1":
            createMenu()
        elif choice == "2":
            break
            #Load saved character
        elif choice == "3":
            break
        elif choice == "4":
            welcomeMenu()
        else:
            print ("\nWrong number. Choose one between 1-3 or push 4 to see the menu again")