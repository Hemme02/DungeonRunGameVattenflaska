from itemClass import Items

class looseCoins(Items):

    def __init__(self):
        gold_ = 2
        rarity_ = 40

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "some coins lying around"
        return returnValue

    def toStringSingle(self):
        returnValue = "A few coins are spread out around the floor.."
        return returnValue