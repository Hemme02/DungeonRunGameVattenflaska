from itemClass import  Items

class gemStone(Items):
    def __init__(self):
        gold_ = 14
        rarity_ = 10

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "a briliant ruby lies in the dirth."
        return returnValue

    def toStringSingle(self):
        returnValue = "gemstones glitter in the torchlights."
        return returnValue

