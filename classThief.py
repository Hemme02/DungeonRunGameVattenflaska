from characterClass import Character


class Thief(Character):
    treasure_saved = 0
    treasure_carried = 0

    def __init__(self, name_):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)



    def earn_treasure(self):
        self.treasure_saved += self.treasure_carried
        self.treasure_carried = 0

    def to_String(self):
        return ("3")
