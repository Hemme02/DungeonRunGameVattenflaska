import random

import sys

from characterClass import Character
import roomClass
from Clear import clear_screen
from classWizard import Wizard



class Map:

    def __init__(self, size_, player_position_, active_character, game_):
        self.size = size_
        self.player_y, self.player_x = player_position_
        self.actual_map = self.createMap()
        self.place_exit()
        self.place_player()
        self.exited_map = False
        self.start_y, self.start_x = player_position_
        self.start = True
        self.old_room = ""
        self.active_character = active_character
        self.game = game_



    def createMap(self):
        map_list = []
        for i in range(self.size):
            map_list.append([])
            for l in range(self.size):
                newRoom = roomClass.Room()
                map_list[i].append(newRoom)
        return map_list

    def random_room(self):
        x_pos = random.randint(0, self.size-1)
        y_pos = random.randint(0, self.size-1)
        return x_pos, y_pos

    def place_exit(self):
        while True:
            x, y = self.random_room()
            if y == self.player_y and x == self.player_x:
                continue
            else:
                break
        self.actual_map[y][x].exitRoom()


    def place_player(self):
        self.actual_map[self.player_y][self.player_x].startingRoom()

    def string_for_room_event(self, enteredRoom):
        string_to_return = ""
        if self.start:
            string_to_return = "** You enter the dungeon and it is very dark.. **"
            self.start = False
            self.actual_map[self.player_y][self.player_x].clear_room()
        elif len(enteredRoom.aliveMonsters) == 0 and len(enteredRoom.existingItems) == 0:
            if enteredRoom.exit:
                string_to_return = "** You have found the exit of the dungeon! **"
            elif enteredRoom.cleared:
                string_to_return = "You can see your boot tracks on the ground. You have already been here.."
            else:
                string_to_return = "** The room you entered looks empty.. **"
                self.actual_map[self.player_y][self.player_x].clear_room()

        elif len(enteredRoom.existingItems) != 0 and len(enteredRoom.aliveMonsters) == 0:
            string_to_return = "The room is empty of monsters but  \n" + enteredRoom.printTreasure()

        elif len(enteredRoom.existingItems) == 0 and len(enteredRoom.aliveMonsters) != 0:
            string_to_return = "You enter a room and when you look around you see \n" + enteredRoom.printMobs()


        elif len(enteredRoom.existingItems) != 0 and len(enteredRoom.aliveMonsters) != 0:
            string_to_return = "You see something shiny but your attention is quickly drawn elsewhere, " \
                               "in front of the treasures you see \n" + enteredRoom.printMobs()




        return string_to_return


    def move_on_map(self, move):
        valid_move = False
        max_size = self.size - 1

        if move.lower() == "up" and self.player_y != 0:
            self.old_room = "down"
            self.player_y = self.player_y - 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move.lower() == "down" and self.player_y != max_size:
            self.old_room = "up"
            self.player_y = self.player_y + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move.lower() == "left" and self.player_x != 0:
            self.old_room = "right"
            self.player_x = self.player_x - 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move.lower() == "right" and self.player_x != max_size:
            self.old_room = "left"
            self.player_x = self.player_x + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True


        return valid_move

    def print_map(self):
        clear_screen()
        for y in range(0, self.size):
            print("\n"+"-"*(self.size*5))
            for x in range(0, self.size):
                room = self.actual_map[y][x]
                if room.visited and not ((self.player_y == y and self.player_x == x) or room.exit):
                    print('' + "| _ |", end='')
                elif self.player_y == y and self.player_x == x:
                    print('' + "| P |" , end="")
                elif room.exit and room.visited:
                    print('' + "| E |", end="")
                else:
                    print('' + "| X |", end='')

        print("\n" + "-" * (self.size * 5))
        print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
        self.move_player()

    def player_can_exit(self):
        if self.actual_map[self.player_y][self.player_x].exit:
            return True
        else:
            return False

    def move_player(self):
        current_room_y = self.player_y
        current_room_x = self.player_x
        current_room_complete = self.actual_map[self.player_y][self.player_x]
        max_room = self.size-1


        while True and not self.exited_map:
            print("\n\nWhere do you want to go: ")

            if(current_room_y != 0 and current_room_y != max_room) and (current_room_x != 0 and current_room_x != max_room):
                if current_room_complete.exit:
                    print("Exit the dungeon (Print Exit)")
                print("Up\nDown\nLeft\nRight")

            if current_room_x != max_room:

                if current_room_y == 0 and current_room_x != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Down\nLeft\nRight")

                elif current_room_y == 0 and current_room_x == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Down\nRight")

                elif current_room_y == max_room and current_room_x != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Up\nLeft\nRight")

                elif current_room_y == max_room and current_room_x == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Up\nRight")

            if current_room_y != max_room:

                if current_room_x == 0 and current_room_y != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Up\nDown\nRight")

                elif current_room_x == max_room and current_room_y != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Up\nDown\nLeft")

                elif current_room_x == max_room and current_room_y == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("Down\nLeft")

            if current_room_y == max_room and current_room_x == max_room:
                if current_room_complete.exit:
                    print("Exit the dungeon (Print Exit)")
                print("Up\nLeft")

            player_move = input("Your choice : ")
            if player_move.lower() == "up" or player_move.lower() == "down" or player_move.lower() == "left" or player_move.lower() == "right" or ( player_move.lower()== "exit" and current_room_complete.exit):
               break
            else:
                self.print_map()
                input("Invalid move, Press any key to continue")
                continue
        if not self.exited_map:
            if player_move.lower() == "up":
                if not self.move_on_map("up"):
                    self.print_map()
                    print("Ouch, you walked into a wall. You cant go that way!")
                    self.move_player()
                else:
                    self.player_event()

            elif player_move.lower() == "down":
                if not self.move_on_map("down"):
                    self.print_map()
                    print("Ouch, you walked into a wall. You cant go that way!")
                    self.move_player()
                else:
                    self.player_event()

            elif player_move.lower() == "left":
                if not self.move_on_map("left"):
                    self.print_map()
                    print("Ouch, you walked into a wall. You cant go that way!")
                    self.move_player()
                else:
                    self.player_event()

            elif player_move.lower() == "right":
                if not self.move_on_map("right"):
                    self.print_map()
                    print("Ouch, you walked into a wall. You cant go that way!")
                    self.move_player()
                else:
                    self.player_event()


            elif player_move.lower() == "exit":
                if not current_room_complete.exit:
                    print("You try to exit thru a solid wall. You take damage.")
                    #TODO take damage
                    self.move_player()
                else:
                    self.exited_map = True
                    return
        return

    def player_event(self):

        actual_position = self.actual_map[self.player_y][self.player_x]

        if len(actual_position.aliveMonsters) != 0:
            self.playerDeath()
            #self.print_map()
            #TODO start fight

        elif len(actual_position.existingItems) != 0:

            #self.PickUpItems()
            self.print_map()

        else:
            self.print_map()

    def PickUpItems(self):
        print("pick up")
        actual_position = self.actual_map[self.player_y][self.player_x]
        for items in actual_position.existingItems:
            self.active_character.treasure_carried.append(items)

        print(self.active_character.treasure_carried)
        actual_position.existingItems = []





    def try_flee(self):

        try_to_flee = self.active_character.agility * 10
        dice_turn = random.randrange(0, 100)

        if self.active_character.class_type == "Wizard":
            try_to_flee = 80

        if dice_turn <= try_to_flee:
            print("Escaped")
            self.move_on_map(self.old_room)
            return True

        else:
            print("Failed to escape")
            return False


    def playerDeath(self):


        print( "*** You have died ""***\n " + "The treasures you picked up during this run will be lost, all data will be saved.\n\n")
        self.active_character.treasure_carried = []
        self.game.deadCharacters.append(self.game.currentCharacters)
        print(self.game.currentCharacters)
        for i in range (len(self.game.currentCharacters)):

            if self.game.currentCharacters[i] == self.game.active_character:
                self.game.currentCharacters.pop(i)
                print(self.game.currentCharacters)
                print(self.game.deadCharacters)
                self.game.save_characters()


        input("Press any key to continue!")






