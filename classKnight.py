from characterClass import Character

class Knight(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = ""

    def __init__(self, name_):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        AI = False
        IsAlive = True
        Character.__init__(self,name_, initiative_, endurance_, attack_, agility_)



    def earn_treasure(self):
        for treasure in self.treasure_carried:
            self.treasure_saved += treasure.gold
        self.treasure_carried = []


    def to_String(self):
        return ("2")
