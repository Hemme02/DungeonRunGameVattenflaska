from characterClass import Character

class Skeleton(Character):
    def __init__(self):
        initiative_ = 4
        endurance_ = 2
        attack_ = 3
        agility_ = 3
        rarity_ = 15
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)

    def toString(self):
        returnValue = "An undead warrior turns and attacks you!"
        return returnValue

    def toStringSingle(self):
        returnValue = "as you regard the graves along the wall you hear a noise behind you." \
                      "\nWhen you turn a skeleton wielding a sword attacks you!"
        return returnValue