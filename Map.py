class Map:

    def __init__(self, size_, player_position_):
        self.size = size_
        self.player_position = player_position_
        self.actual_map = self.createMap()


    def createMap(self):
        map_list = []

        for i in range(self.size):
            map_list.append([])
            for l in range(self.size):
                newRoom = None #roomFunctionen
                map_list[i].append(newRoom)
        return map_list
