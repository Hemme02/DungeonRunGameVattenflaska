from characterClass import Character

class AIThief(Character):
    treasure_saved = 0
    treasure_carried = 0

    def __init__(self):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        AI = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, AI)

    def earn_treasure(self):
        self.treasure_saved += self.treasure_carried
        self.treasure_carried = 0

    def to_String(self):
        return ("3")
