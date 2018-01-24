from characterClass import Character


class Thief(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = ""

    def __init__(self, name_):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        self.AI = False
        self.IsAlive = True
        self.class_name = "Thief"
        Character.__init__(self, name_, initiative_, endurance_, attack_, agility_)



    def earn_treasure(self):
        for treasure in self.treasure_carried:
            self.treasure_saved += treasure.gold
        self.treasure_carried = []


    def to_String(self):
        return ("3")
