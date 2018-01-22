from characterClass import Character

class AIKnight(Character):
    treasure_saved = 0
    treasure_carried = 0

    def __init__(self):
        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        AI = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, AI)

    def earn_treasure(self):
        self.treasure_saved += self.treasure_carried
        self.treasure_carried = 0

    def to_String(self):
        return ("2")
