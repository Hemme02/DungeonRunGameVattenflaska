from characterClass import Character


class Thief(Character):
    treasure_saved = 0
    treasure_caried = 0

    def __init__(self, name_):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)


    def earn_treasure(self):
        self.treasure_saved += self.treasure_caried
        self.treasure_caried = 0