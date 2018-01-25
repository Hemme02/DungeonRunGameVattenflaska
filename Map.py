import random
import time
import roomClass
from Clear import clear_screen
from startFight import startFight


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
        self.times_fleed = 0
        self.fleed_room = None



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


        self.PickUpItems()
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

        if self.active_character.AI:
            self.AI_event()
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
        if not self.active_character.AI:
            if len(self.actual_map[self.player_y][self.player_x].aliveMonsters) != 0:
                input("Print a key to continue to the fight")


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
            self.print_map()
            actual_position.aliveMonsters = startFight(self.active_character, actual_position.aliveMonsters, self)
            if not self.active_character.IsAlive:
                self.playerDeath()
            else:
                if len(actual_position.aliveMonsters) == 0:
                    print("You won the fight. You have "+str(self.active_character.endurance) + " endurance left.")
                    input("Press any key to continue")
                    if len(actual_position.existingItems) != 0:
                        print("You find" + actual_position.printTreasure())
                        self.print_map()
                        self.move_player()
                    else:
                        self.print_map()
                        self.move_player()
                elif len(actual_position.aliveMonsters) > 0:
                    self.move_on_map(self.old_room)
                    self.print_map()
                    self.move_player()
                else:
                    self.print_map()
                    self.move_player()

        elif len(actual_position.existingItems) != 0:
            self.print_map()
            self.move_player()

        else:
            self.print_map()
            self.move_player()

    def PickUpItems(self):
        actual_position = self.actual_map[self.player_y][self.player_x]
        for items in actual_position.existingItems:
            self.active_character.treasure_carried.append(items)
        actual_position.existingItems = []



    def playerDeath(self):
        clear_screen()

        print( "*** You have died ""***\n " + "The treasures you picked up during this run will be lost, all data will be saved.\n\n")
        self.active_character.treasure_carried = []
        self.active_character.IsAlive = False
        self.game.deadCharacters.append(self.game.active_character)

        for i in range (len(self.game.currentCharacters)):
            if self.game.currentCharacters[i] == self.game.active_character:
                self.game.currentCharacters.pop(i)
                self.game.save_characters()


        input("Press any key to continue!")
        return

    def ai_Death(self):
        pass

    def AI_finish(self):
        pass

    def AI_move(self):
        self.print_map()
        rooms = []
        visited_room = []
        max_int = self.size - 1

        if self.player_y != 0:
            rooms.append([self.actual_map[self.player_y - 1][self.player_x], "y", False])
        if self.player_y != max_int:
            rooms.append([self.actual_map[self.player_y + 1][self.player_x], "y", True])
        if self.player_x != 0:
            rooms.append([self.actual_map[self.player_y][self.player_x - 1], "x", False])
        if self.player_x != max_int:
            rooms.append([self.actual_map[self.player_y][self.player_x + 1], "x", True])

        for i in range(len(rooms) - 1, -1, -1):
            if rooms[i][0].visited:
                visited_room.append(rooms[i])
                rooms.pop(i)

        if len(rooms) == 0:
            random_choice = random.randint(0, len(visited_room) - 1)
            room_to_go_to = visited_room[random_choice]

        elif len(rooms) == 1:
            room_to_go_to = rooms[0]

        else:
            random_choice = random.randint(0, len(rooms) - 1)
            room_to_go_to = rooms[random_choice]

        if room_to_go_to[1] == "y":
            if room_to_go_to[2]:
                self.move_on_map("down")
            else:
                self.move_on_map("up")

        elif room_to_go_to[1] == "x":
            if room_to_go_to[2]:
                self.move_on_map("right")
            else:
                self.move_on_map("left")

    def AI_event(self):
        if not self.active_character.doing_multiple_runs:
            time.sleep(1)
        current_room = self.actual_map[self.player_y][self.player_x]
        if current_room.exit:
            print("You found the exit")
            return
        else:
            if current_room.aliveMonsters == 0 and current_room.existingItems == 0:
                self.AI_move()
            elif current_room.aliveMonsters == 0 and current_room.existingItems != 0:
                self.AI_move()
            else:
                self.actual_map[self.player_y][self.player_x].aliveMonsters = startFight(self.active_character, current_room.aliveMonsters, self)
                if not self.active_character.IsAlive:
                    self.ai_Death()
                else:
                    if len(self.actual_map[self.player_y][self.player_x].aliveMonsters) == 0:
                        print("You won the fight. You have " + str(
                            self.active_character.endurance) + " endurance left.")
                        if len(current_room.existingItems) != 0:
                            print("You find" + current_room.printTreasure())
                            self.AI_move()
                        else:
                            self.AI_move()
                    elif len(self.actual_map[self.player_y][self.player_x].aliveMonsters) > 0:
                        print("You flee backwards to the previous room. None follow you.")
                        self.fleed_room = current_room
                        self.times_fleed += 1
                        self.move_on_map(self.old_room)

                    else:
                        self.AI_move()





