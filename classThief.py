from characterClass import Character


class Thief(Character):
    def __init__(self, name_):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)

        treasure_saved = 0
        treasure_caried = 0