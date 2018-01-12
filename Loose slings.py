from Goldclass import gold

class Loose_slings(gold):
    def __init__(self):
        self.agility = 40
        self.rarity = 2
        gold.__init__(self.gold, self.rarity,self.agility)


