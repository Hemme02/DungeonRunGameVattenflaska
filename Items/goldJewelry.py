from Items.itemClass import  Items

class goldJewelry(Items):

    def __init__(self):
        gold_ = 10
        rarity_ = 15

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "a beautiful golden necklace lies on a table"
        return returnValue

    def toStringSingle(self):
        returnValue = "golden jewelry has always been your favorite. And know you own one more golden necklace."
        return returnValue