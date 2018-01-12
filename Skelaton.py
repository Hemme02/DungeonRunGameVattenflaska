from characterClass import Character

class Skelaton(Character):
    def __init__(self):
        initiative_ = 4
        endurance_ = 2
        attack_ = 3
        agility_ = 3
        rarity_ = 15
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)