from characterClass import Character

class Troll(Character):
    def __init__(self):
        initiative_ = 2
        endurance_ = 4
        attack_ = 7
        agility_ = 2
        rarity_ = 5
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)

    def toString(self):
        returnValue = "A giant troll looks at you hungerly."
        return returnValue

    def toStringSingle(self):
        returnValue = "Sturing a large pot a huge troll is cooking her dinner. She looks at you and smiles\n" \
                      "You have a sinking feeling that she wants you in that pot. Then she swings here ladel at you!"
        return returnValue