import time
import random
from Clear import clear_screen
from Dice_throw import dice_throw



def startFight(player, monsters, map):
    current_map = map
    active_player = player
    list_of_monsters = monsters

    #Soldier blockar första slaget varje combat
    #denna sätts till false efter första gången
    startFight.soldier_special = True


    def turn_taking(player, monsters):
        turn_list = []

        player_result = dice_throw(player.initiative)

        turn_list.append((player, player_result))

        for monster in monsters:
            monster_result = dice_throw(monster.initiative)
            for i in range(0, len(turn_list)):
                if monster_result > turn_list[i][1]:
                    turn_list.insert(i, (monster, monster_result))
                    break

                elif i == len(turn_list) - 1:
                    turn_list.append((monster, monster_result))

        return turn_list
        #########################################################################

    def try_flee():

        try_to_flee = active_player.agility * 10
        dice_turn = random.randint(0, 100)

        if active_player.class_type == "Wizard":
            try_to_flee = 80

        if dice_turn <= try_to_flee:
            print("Escaped")
            return True

        else:
            print("Failed to escape")
            return False

    def player_combat_action(player, list_of_monsters):
        while True:
            print("Chose your action: ")
            for i in range(0, len(list_of_monsters)):
                print(str(i + 1) + ": Attack " + list_of_monsters[i].name)
            print("0, Escape to previous room")

            try:
                action_input = int(input())
                break
            except ValueError:
                print("Wrong choice!")
                continue
        while True:
            if action_input == 0:
               return "flee"
            elif action_input <= len(list_of_monsters):
                player_attack(player, list_of_monsters[action_input - 1])
                return "attack"
            else:
                print("Must enter a valid input")

    def player_attack(player, target):
        player_atk = dice_throw(player.attack)
        target_agil = dice_throw(target.agility)
        if player_atk >= target_agil:
            if player.class_type == "Thief" and random.randint(1, 100) <= 25:
                print("Double strike hit for 2 endurance")
                target.endurance -= 2
            else:
                print("Attack hit")
                target.endurance -= 1
            if target.endurance <= 0:
                print("you've killed " + target.name)
                list_of_monsters.remove(target)

        else:
            print("You missed")
        time.sleep(1)


    def monster_attack(fighter, target):
        monster_atk = dice_throw(target.attack)
        player_agil = dice_throw(fighter.agility)

        if monster_atk > player_agil:

            if player.class_type == "Knight" and startFight.soldier_special:
                print("Shield blocked the attack, you take no damage")
                startFight.soldier_special = False
            else:
                print(target.name + " hit you for 1 endurance")
                fighter.endurance -= 1
                if fighter.endurance <= 0:
                    current_map.playerDeath()
        else:
            print(target.name + " missed!")

        time.sleep(1)


    list_of_turn = (turn_taking(player, list_of_monsters))

    while len(list_of_turn) > 1 and active_player.IsAlive:
        clear_screen()
        print("Turn_list")
        for i in range(len(list_of_turn)):
            if list_of_turn[i][0].endurance <= 0:
                list_of_turn.pop(i)
        for i in range(len(list_of_turn)):
            print(str(i+1) +":   "+ list_of_turn[i][0].name + ", Endurance left: "+ str(list_of_turn[i][0].endurance))
        print()
        time.sleep(1)
        for creature in list_of_turn:
            if not active_player.IsAlive:
                break
            elif creature[0] == active_player:
                player_action = player_combat_action(active_player, list_of_monsters)
                if player_action == "flee":
                    if try_flee():
                        return list_of_monsters
                if len(list_of_monsters)==0:
                    return list_of_monsters
            elif creature[0].endurance > 0:
                monster_attack(active_player, creature[0])
    return list_of_monsters





#Attack:
#Göra: Spelare/Monster ska kunna attackera motpart, vid träff göra skada
#Hur: Funktion som tar emot attackerare och mål. Returnera träff/miss.
#Drar av health vid träff.
#Om monster dör, tar bort från rumslista och turordningslista.
#Riddare blockar alltid första attacken vid träff mot den i varje strid.
#Tjuv gör dubbel skada 25% av tiden



