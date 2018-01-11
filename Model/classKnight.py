from Model.characterClass import Character

class Knight(Character):
    def __init__(self):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        Character.__init__(self, initiative_, endurance_, attack_, agility_)
