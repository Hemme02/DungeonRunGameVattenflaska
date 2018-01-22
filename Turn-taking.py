from Dice_throw import dice_throw

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

            elif i == len(turn_list)-1:
                turn_list.append((monster, monster_result))

    return turn_list


