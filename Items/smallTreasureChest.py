from Items.itemClass import Items

class smallTreasureChest(Items):

    def __init__(self):
        gold_ = 20
        rarity_ = 5

        Items.__init__(self,gold_, rarity_)