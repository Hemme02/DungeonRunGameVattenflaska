from characterClass import Character

class Troll(Character):
    def __init__(self):
        initiative_ = 2
        endurance_ = 4
        attack_ = 7
        agility_ = 2
        rarity_ = 5
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)