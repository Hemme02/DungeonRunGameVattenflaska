from Items.itemClass import Items

class LooseCoins(Items):

    def __init__(self):
        gold_ = 2
        rarity_ = 40

        Items.__init__(self,gold_, rarity_)