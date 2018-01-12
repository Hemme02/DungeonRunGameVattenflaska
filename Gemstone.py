from Goldclass import gold

class Gemstone(gold):
    def __init__(self):
        self.agility = 10
        self.rarity = 14
        gold.__init__(self.gold, self.rarity,self.agility)