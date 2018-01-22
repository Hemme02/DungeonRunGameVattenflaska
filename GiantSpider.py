from characterClass import Character

class GiantSpider(Character):
    def __init__(self):
        initiative_ = 7
        endurance_ = 1
        attack_ = 2
        agility_ = 3
        rarity_ = 20
        alive_ = True
        Character.__init__(self,"Giant Spider", initiative_, endurance_, attack_, agility_)

    def toString(self):
        returnValue = "A giant Spider hisses at you!"
        return returnValue

    def toStringSingle(self):
        returnValue = "a giant mass merge from the darkness, the giant spider attacks you!"
        return returnValue