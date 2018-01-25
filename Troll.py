from characterClass import Character

class Troll(Character):
    def __init__(self):
        initiative_ = 2
        endurance_ = 4
        attack_ = 7
        agility_ = 2
        rarity_ = 5
        alive_ = True

        Character.__init__(self, "Troll", initiative_, endurance_, attack_, agility_)

    def toString(self):
        returnValue = "A giant troll looking at you while drooling.."
        return returnValue

    def toStringSingle(self):
        returnValue = "a huge troll stirring her large pot in front of you. She looks at you and smiles\n" \
                      "You have a sinking feeling that she wants you in that pot while she swings her wooden club at you!"
        return returnValue