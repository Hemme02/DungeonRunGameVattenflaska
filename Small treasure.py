from Goldclass import gold

class Small_treasure(gold):
    def __init__(self):
        self.agility = 5
        self.rarity = 20
        gold.__init__(self.gold, self.rarity,self.agility)