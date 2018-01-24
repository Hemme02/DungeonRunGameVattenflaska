from characterClass import Character


class Wizard(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Wizard"


    def __init__(self, name_):
        initiative_ = 6
        endurance_ = 4
        attack_ = 9
        agility_ = 5
        self.AI = False
        self.IsAlive = True
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)



    def earn_treasure(self):
        for treasure in self.treasure_carried:
            self.treasure_saved += treasure.gold
        self.treasure_carried = []

    def to_String(self):
        return("1")