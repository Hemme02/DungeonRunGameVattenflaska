from Items.itemClass import  Items

class goldJewelry(Items):

    def __init__(self):
        gold_ = 10
        rarity_ = 15

        Items.__init__(self,gold_, rarity_)