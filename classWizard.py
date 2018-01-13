from characterClass import Character


class Wizard(Character):
    treasure_saved = 0
    treasure_caried = 0

    def __init__(self, name_):
        initiative_ = 6
        endurance_ = 4
        attack_ = 9
        agility_ = 5
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)


    def earn_treasure(self):
        self.treasure_saved += self.treasure_carried
        self.treasure_carried = 0