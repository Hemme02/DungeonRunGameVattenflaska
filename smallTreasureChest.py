from itemClass import Items

class smallTreasureChest(Items):

    def __init__(self):
        gold_ = 20
        rarity_ = 5

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "a small chest"
        return returnValue

    def toStringSingle(self):
        returnValue = "On the floor sits a chest full of valuable items, this is what you have been looking for."
        return returnValue