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


    def move_on_map(self, move):
        valid_move = False
        max_size = self.size - 1

        if move == "up" and self.player_y != 0:
            self.player_y = self.player_y - 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move == "down" and self.player_y != max_size:
            self.player_y = self.player_y + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move == "left" and self.player_x != 0:
            self.player_x = self.player_x - 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        elif move == "right" and self.player_x != max_size:
            self.player_x = self.player_x + 1
            self.actual_map[self.player_y][self.player_x].visitedRoom()
            valid_move = True

        return valid_move
