from characterClass import Character


class Wizard(Character):
    def __init__(self, name_):
        initiative_ = 6
        endurance_ = 4
        attack_ = 9
        agility_ = 5
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)

        treasure_saved = 0
        treasure_caried = 0