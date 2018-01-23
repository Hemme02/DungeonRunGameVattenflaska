from Dice_throw import dice_throw

def startFight(player, monsters):

    list_of_monsters = monsters
    toFlee = Map.flee


    def turn_taking(player, monsters):
        turn_list = []

        player_result = dice_throw(player.initiative)

        turn_list.append((player, player_result))

        for monster in monsters:
            monster_result = dice_throw(monster.initiative)
            for i in range(0, len(turn_list)):
                if monster_result > turn_list[i+1]:
                    turn_list.insert(i, (monster, monster_result))
                    break

                elif i == len(turn_list) - 1:
                    turn_list.append((monster, monster_result))

        return turn_list
        #########################################################################

    def player_combat_action(player, monsters):
        #list_of_monsters = monsters
        print("Chose your action: ")
        for i in list_of_monsters:
            print(str(i + 1) + ": Attack " + list_of_monsters[i])
        print("0, Escape to previous room")

        try:
            action_input = int(input())
        except ValueError:
            print("Wrong choice!")
            continue

        if action_input == 0:
            if toFlee:
                return list_of_monsters
        elif action_input <= len(list_of_monsters):
            player_attack(player, list_of_monsters[action_input - 1])
            return "attack"
        else:
            print("Must enter a valid input")

    def player_attack(fighter, target):
        player_atk = dice_throw(fighter.attack)
        target_agil = dice_throw(target.agillity)
        if player_atk >= target_agil:
            print("Attack hit")
            target.durability -= 1
            if target.durability <= 0:
                print("you've killed" + target)
                list_of_monsters.remove(target)
        else:
            print("You missed")

    def monster_attack(fighter, target):
        monster_atk = dice_throw(target.attack)
        player_agil = dice_throw(fighter.agillity)

        if monster_atk > player_agil:
            print(target + " hit you for 1 durability")
            fighter.durability -= 1
            if fighter.durability <= 0:
                playerisDead
        else:
            print(target + " Missed!")


    list_of_turn = (turn_taking(player, monsters))

    while len(list_of_turn) > 1 and player.alive:
        for creature in list_of_turn:
            if not player.alive:
                break
            elif creature.IsPlayer:
                player_action = player_combat_action(creature, monsters)
                if player_action == "escape":
                    escape()
            elif creature.durability > 0:
                monster_attack(player, creature)
    return True


#Attack:
#Göra: Spelare/Monster ska kunna attackera motpart, vid träff göra skada
#Hur: Funktion som tar emot attackerare och mål. Returnera träff/miss.
#Drar av health vid träff.
#Om monster dör, tar bort från rumslista och turordningslista.
#Riddare blockar alltid första attacken vid träff mot den i varje strid.
#Tjuv gör dubbel skada 25% av tiden