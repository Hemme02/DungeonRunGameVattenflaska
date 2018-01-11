from Controller.characterClass import Character


class Thief(Character):
    def __init__(self):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        Character.__init__(self, initiative_, endurance_, attack_, agility_)