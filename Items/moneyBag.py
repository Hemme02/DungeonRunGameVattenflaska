from Items.itemClass import Items

class moneyBag(Items):

    def __init__(self):
        gold_ = 6
        rarity_ = 20

        Items.__init__(self,gold_, rarity_)