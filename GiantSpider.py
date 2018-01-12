from characterClass import Character

class GiantSpider(Character):
    def __init__(self):
        initiative_ = 7
        endurance_ = 1
        attack_ = 2
        agility_ = 3
        rarity_ = 20
        alive_ = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, rarity_)