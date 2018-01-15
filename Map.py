import random
import roomClass


class Map:

    def __init__(self, size_, player_position_):
        self.size = size_
        self.player_position = player_position_
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
        x_pos = random.randint(0,self.size)
        y_pos = random.randint(0,self.size)
        return (x_pos, y_pos)

    def place_exit(self):
        while True:
            x, y = self.random_room()
            if x == self.player_position[0] and y == self.player_position[1]:
                continue
            else:
                break
        self.actual_map[x][y].exitRoom()


    def place_player(self):
        x,y = self.player_position
        self.actual_map[x][y].startingRoom()


newMap = Map(5, (1, 2))
print(newMap.actual_map[1][4])