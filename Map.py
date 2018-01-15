import random
import roomClass


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
            if not (enteredRoom.visited and enteredRoom.exit):
                string_to_return = "The room you entered looks empty"
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
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            valid_move = True

        elif move == "down" and self.player_y != max_size:
            self.player_y = self.player_y + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            valid_move = True

        elif move == "left" and self.player_x != 0:
            self.player_x = self.player_x - 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            valid_move = True

        elif move == "right" and self.player_x != max_size:
            self.player_x = self.player_x + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            print(self.string_for_room_event(self.actual_map[self.player_y][self.player_x]))
            valid_move = True

        return valid_move

    def print_map(self):
        for y in range(0, self.size):
            print("\n"+"-"*(self.size*3))
            for x in range(0, self.size):
                room = self.actual_map[y][x]
                if room.visited and not (self.player_y == y and self.player_x == x):
                    print(" _ ", end='')
                elif self.player_y == y and self.player_x == x:
                    print(" P ", end="")
                else:
                    print(" X ", end='')

newMap = Map(8, (1,2))
newMap.move_on_map("up")
newMap.move_on_map("right")
newMap.move_on_map("left")
newMap.move_on_map("left")
newMap.print_map()