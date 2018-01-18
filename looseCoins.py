from itemClass import Items

class looseCoins(Items):

    def __init__(self):
        gold_ = 2
        rarity_ = 40

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "you see some coins lying around.."
        return returnValue

    def toStringSingle(self):
        returnValue = "you find a few golden coins that are spread out on the floor.."
        return returnValue