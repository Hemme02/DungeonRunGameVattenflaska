from itemClass import Items

class moneyBag(Items):

    def __init__(self):
        gold_ = 6
        rarity_ = 20

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "you find a bag of coins"
        return returnValue

    def toStringSingle(self):
        returnValue = "someone has dropped their bag of coins. Finders keepers!"
        return returnValue