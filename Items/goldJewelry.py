from Items.itemClass import  Items

class goldJewelry(Items):

    def __init__(self):
        gold_ = 10
        rarity_ = 15

        Items.__init__(self,gold_, rarity_)

    def toString(self):
        returnValue = "A beautiful golden necklace"
        return returnValue

    def toStingSingle(self):
        returnValue = "Golden jewelry has always been your favorite. And know you own one more golden necklace."
        return returnValue