from itemClass import  Items

class gemStone(Items):
    def __init__(self):
        gold_ = 14
        rarity_ = 10

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "a brilliant ruby lies in the dirt."
        return returnValue

    def toStringSingle(self):
        returnValue = "a few gemstones glitter in the torchlight."
        return returnValue

