import random
import roomClass
#

class Map:

    def __init__(self, size_, player_position_):
        self.size = size_
        self.player_y, self.player_x = player_position_
        self.actual_map = self.createMap()
        self.place_exit()
        self.place_player()



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
        self.actual_map[x][y].exitRoom()


    def place_player(self):
        self.actual_map[self.player_y][self.player_x].startingRoom()

    def string_for_room_event(self, enteredRoom):
        string_to_return = ""
        if len(enteredRoom.aliveMonsters) == 0 and len(enteredRoom.existingItems) == 0:
            if not (enteredRoom.visited or enteredRoom.exit):
                print(enteredRoom.visited)
                string_to_return = "The room you entered looks empty"
                self.actual_map[self.player_y][self.player_x].clear_room()
            else:
                if enteredRoom.cleared:
                    string_to_return = "You can see your boot tracks on the floor. You have already been here."
                elif enteredRoom.exit:
                    string_to_return = "You have found the exit of the dungeon!"
                else:
                    string_to_return = "You enter to continue the fight against "+ enteredRoom.printMobs()

        elif len(enteredRoom.existingItems) != 0 and len(enteredRoom.aliveMonsters) == 0:
            string_to_return = "The room is empty of monsters but, "+ enteredRoom.printTreasure()

        elif len(enteredRoom.existingItems) == 0 and len(enteredRoom.aliveMonsters) != 0:
            string_to_return = "You enter a room and when you look around you see. " + enteredRoom.printMobs()

        elif len(enteredRoom.existingItems) != 0 and len(enteredRoom.aliveMonsters) != 0:
            string_to_return = "You see something shiny but your attention is quickly drawn elsewhere ," + enteredRoom.printMobs()


        return string_to_return


    def move_on_map(self, move):
        valid_move = False
        max_size = self.size - 1

        if move == "up" and self.player_y != 0:
            self.player_y = self.player_y - 1
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            self.print_map()
            valid_move = True

        elif move == "down" and self.player_y != max_size:
            self.player_y = self.player_y + 1
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            self.print_map()
            valid_move = True

        elif move == "left" and self.player_x != 0:
            self.player_x = self.player_x - 1
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            self.print_map()
            valid_move = True

        elif move == "right" and self.player_x != max_size:
            self.player_x = self.player_x + 1
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            self.print_map()
            valid_move = True

        return valid_move

    def print_map(self):

        for y in range(0, self.size):
            print("\n"+"-"*(self.size*5))
            for x in range(0, self.size):
                room = self.actual_map[y][x]
                if room.visited and not (self.player_y == y and self.player_x == x):
                    print('' + "| _ |", end='')
                elif self.player_y == y and self.player_x == x:
                    print('' + "| P |" , end="")
                else:
                    print('|' + " X ", end='')
        self.move_player()
                    print('' + "| X |", end='')
        print("\n" + "-" * (self.size * 5))

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


        while True:

            if(current_room_y != 0 and current_room_y != max_room) and (current_room_x != 0 and current_room_x != max_room):
                if current_room_complete.exit:
                    print("Exit the dungeon (Print Exit)")
                print("\nUp\nDown\nLeft\nRight")

            if current_room_x != max_room:

                if current_room_y == 0 and current_room_x != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nDown\nLeft\nRight")

                elif current_room_y == 0 and current_room_x == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nDown\nRight")

                elif current_room_y == max_room and current_room_x != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nUp\nLeft\nRight")

                elif current_room_y == max_room and current_room_x == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nUp\nRight")

            if current_room_y != max_room:

                if current_room_x == 0 and current_room_y != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nUp\nDown\nRight")

                elif current_room_x == max_room and current_room_y != 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nUp\nDown\nLeft")

                elif current_room_x == max_room and current_room_y == 0:
                    if current_room_complete.exit:
                        print("Exit the dungeon (Print Exit)")
                    print("\nDown\nLeft")

            if current_room_y == max_room and current_room_x == max_room:
                if current_room_complete.exit:
                    print("Exit the dungeon (Print Exit)")
                print("\nUp\nLeft")

            player_move = input("Where do you want to go: ")
            if player_move == "up" or player_move == "down" or player_move == "left" or player_move == "right" or (player_move == "exit" and current_room_complete.exit):
               break
            else:
                input("Invalid move, Press any key to continue")
                continue

        if player_move.lower() == "up":
            if not self.move_on_map("up"):
                print("Ouch, you walked into a wall. You cant go that way!")
                self.print_map()
                self.move_player()
            else:
                self.player_event()

        elif player_move.lower() == "down":
            if not self.move_on_map("down"):
                print("Ouch, you walked into a wall. You cant go that way!")
                self.print_map()
                self.move_player()
            else:
                self.player_event()

        elif player_move.lower() == "left":
            if not self.move_on_map("left"):
                print("Ouch, you walked into a wall. You cant go that way!")
                self.print_map()
                self.move_player()
            else:
                self.player_event()

        elif player_move.lower() == "right":
            if not self.move_on_map("right"):
                print("Ouch, you walked into a wall. You cant go that way!")
                self.print_map()
                self.move_player()
            else:
                self.player_event()


        elif player_move.lower() == "exit":
            if not current_room_complete.exit:
                print("You try to exit thru a solid wall. You take damage.")
                #TODO take damage
                self.move_player()
            else:
                pass
                #TODO exitfunction



    def player_event(self):
        actual_position = self.actual_map[self.player_y][self.player_x]

        if len(actual_position.aliveMonsters) != 0:
            self.move_player()
            #TODO start fight

        elif len(actual_position.existingItems) != 0:
            self.move_player()
            #TODO pick up treasure

        else:
            self.move_player()


#newMap = Map(4, (1,2))
#newMap.move_player()