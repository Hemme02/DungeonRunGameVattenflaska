from Items.itemClass import  Items

class gemStone(Items):
    def __init__(self):
        gold_ = 14
        rarity_ = 10

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "A briliant ruby."
        return returnValue

    def toStingSingle(self):
        returnValue = "Gemstones glitter in the torchlights."
        return returnValue

