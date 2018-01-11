# Menu to start game

def menuToStartGame ():

    print ("\nSelect your character:\n" "1. Mage \n""2. Warrior  \n""3. Theif \n""4. Show more info \n""5. Close \n")
    return



print ("Start the adventure:")
print("Menu")
menuToStartGame ()

while True:

    try:
        choice_start_game = input("Your choice: ")

        # 1.Mage
        if choice_start_game == 1:
            break

        # 2.Warrior
        elif choice_start_game == 2:
            break

        # 3.Theif
        elif choice_start_game == 3:
            break


        # 4.Show more info about characters
        elif choice_start_game == 4:
            break

        # Close
        elif choice_start_game == 5:
            menuToStartGame()

        else:
            print(" Try again ! ")

    except:
        print(" Try again! ")
        print(" ")





