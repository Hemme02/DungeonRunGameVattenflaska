from Goldclass import gold

class Money_purse(gold):
    def __init__(self):
        self.agility = 20
        self.rarity = 6
        gold.__init__(self.gold, self.agility, self.rarity)
