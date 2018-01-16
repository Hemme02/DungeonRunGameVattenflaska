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
        returnValue = "on the floor sits a chest full of valuable items. This is what you been looking for."
        return returnValue