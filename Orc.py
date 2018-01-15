from characterClass import Character

class Orc(Character):
    def __init__(self):
        initiative_ = 6
        endurance_ = 3
        attack_ = 4
        agility_ = 4
        rarity_ = 10
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)

    def toString(self):
        returnValue = "a green skinned Orc with a large club charges!"
        return returnValue

    def toStringSingle(self):
        returnValue = "an Orc looks up from his meal and smiles drowling at you before heafting his large club and swings it at your head"
        return returnValue
