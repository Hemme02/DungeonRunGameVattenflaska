from Items.itemClass import Items

class looseCoins(Items):

    def __init__(self):
        gold_ = 2
        rarity_ = 40

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "Some coins"
        return returnValue

    def toStingSingle(self):
        returnValue = "A few coins are spread out around the floor"
        return returnValue