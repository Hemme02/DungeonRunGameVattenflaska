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
        returnValue = "A undead warrior turns and attacks you!"
        return returnValue

    def toStingSingle(self):
        returnValue = "You enter a masoleum. As you regard the graves along the wall you hear a noice behind you." \
                      "\nWhen you turn a sceleton wielding a sword attacks you!"
        return returnValue