from characterClass import Character

class Orc(Character):
    def __init__(self):
        initiative_ = 6
        endurance_ = 3
        attack_ = 4
        agility_ = 4
        rarity_ = 10
        alive_ = True
        Character.__init__(self, "Orc", initiative_, endurance_, attack_, agility_)

    def toString(self):
        returnValue = "A smelly green Orc with a large club charges!"
        return returnValue

    def toStringSingle(self):
        returnValue = "an Orc looks up from his meal and smiles while drooling at you before \n" \
                        "heafting his large club and swings it towards your head!"
        return returnValue
