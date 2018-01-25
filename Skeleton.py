from characterClass import Character

class Skeleton(Character):
    def __init__(self):
        initiative_ = 4
        endurance_ = 2
        attack_ = 3
        agility_ = 3
        rarity_ = 15
        alive_ = True

        Character.__init__(self, "Skeleton", initiative_, endurance_, attack_, agility_)

    def toString(self):
        returnValue = "A spooky scary skeleton!"
        return returnValue

    def toStringSingle(self):
        returnValue = "graves along the walls when you suddenly hear a noise behind you," \
                      "\nwhen you turn around a skeleton wielding a rusty sword attacks you!"
        return returnValue