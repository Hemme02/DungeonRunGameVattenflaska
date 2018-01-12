from characterClass import Character

class Knight(Character):
    def __init__(self, name_):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        Character.__init__(self,name_, initiative_, endurance_, attack_, agility_)

        treasure_saved = 0
        treasure_caried = 0
