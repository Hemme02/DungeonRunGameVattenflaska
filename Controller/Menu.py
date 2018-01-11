# Menu to start game



from Model.classWizard import Wizard
from Model.classKnight import Knight
from Model.classThief import Thief
from Controller.Main import currentCharacters
from Controller.SaveGame import save_game_current

def menuToStartGame ():
    print ("\nSelect your character:\n" "1. Wizard \n""2. Knight  \n""3. Theif \n""4. Show more info \n""5. Close \n")
    return



def createCharacter (number):

    character_name = input("Your name for the character: ")
    if number =="1":
        new_wizard = Wizard(character_name)
        currentCharacters.append(new_wizard)
        save_game_current(currentCharacters)

    elif number =="2":
        new_Knight = Knight(character_name)
        currentCharacters.append(new_Knight)
        save_game_current(currentCharacters)

    elif number == "3":
        new_thief = Thief(character_name)
        currentCharacters.append(new_thief)
        save_game_current(currentCharacters)



def createMenu ():

    print ("Start the adventure:")
    print("Menu")
    menuToStartGame ()

    while True:


        try:

            choice_start_game = input("Your choice: ")

            # 1.Mage
            if choice_start_game == "1":
                createCharacter("1")


            # 2.Warrior
            elif choice_start_game == "2":
                createCharacter("2")


            # 3.Theif
            elif choice_start_game == "3":
                createCharacter("3")


            # 4.Show more info about characters
            elif choice_start_game == "4":
                print(" Info ")

            # Close
            elif choice_start_game == "5":
                menuToStartGame()

            else:
                print(" Try again ! ")

        except:
            print(" Try again! ")






