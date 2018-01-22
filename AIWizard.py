from characterClass import Character

class AIWizard(Character):
    treasure_saved = 0
    treasure_carried = []

    def __init__(self):
        initiative_ = 6
        endurance_ = 4
        attack_ = 9
        agility_ = 5
        AI = True
        Character.__init__(self, initiative_, endurance_, attack_, agility_, AI)

    def earn_treasure(self):
        self.treasure_saved += self.treasure_carried
        self.treasure_carried = []

    def to_String(self):
        return("1")
