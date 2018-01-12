from characterClass import Character

class Knight(Character):
    treasure_saved = 0
    treasure_caried = 0

    def __init__(self, name_):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        Character.__init__(self,name_, initiative_, endurance_, attack_, agility_)


    def earn_treasure(self):
        self.treasure_saved += self.treasure_caried
        self.treasure_caried = 0
