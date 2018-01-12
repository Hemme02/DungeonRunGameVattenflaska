from Goldclass import gold

class Gold_jewelry(gold):
    def __init__(self):
        self.agility = 15
        self.rarity = 10
        gold.__init__(self.gold, self.rarity,self.agility)