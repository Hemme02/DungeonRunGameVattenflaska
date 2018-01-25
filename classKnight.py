from characterClass import Character

class Knight(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Knight"

    def __init__(self, name_):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        self.AI = False
        self.doing_multiple_runs = False
        self.IsAlive = True
        self.class_name = "Knight"
        Character.__init__(self,name_, initiative_, endurance_, attack_, agility_)



    def earn_treasure(self):
        for treasure in self.treasure_carried:
            self.treasure_saved += treasure.gold
        self.treasure_carried = []


    def to_String(self):
        return ("2")
