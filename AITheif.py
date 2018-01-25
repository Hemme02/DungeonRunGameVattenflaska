from characterClass import Character

class AIThief(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Thief"

    def __init__(self):
        initiative_ = 7
        endurance_ = 5
        attack_ = 5
        agility_ = 7
        self.AI = True
        self.IsAlive = True
        self.doing_multiple_runs = False
        self.class_name = "Thief"
        self.run = 0
        self.runFinished = 0
        self.aiDead = 0
        self.roomAmounts = 0
        self.enemiesKilled = 0
        self.multiRuns = 0
        self.multiFinished = 0
        self.multiDead = 0
        self.multiRooms = 0
        self.multiEnemies = 0
        self.multiTreasures = 0
        self.totalRuns = 0
        self.totalFinished = 0
        self.totalDead = 0
        self.totalRooms = 0
        self.totalEnemies = 0
        Character.__init__(self, "AIThief", initiative_, endurance_, attack_, agility_)

    def earn_treasure(self):
        for item in self.treasure_carried:
            self.treasure_saved += item.gold
        self.treasure_carried = []

    def to_String(self):
        return "3"

    def multipleRuns(self):
        self.multiRuns += self.run
        self.multiFinished += self.runFinished
        self.multiDead += self.aiDead
        self.multiRooms += self.roomAmounts
        self.multiEnemies += self.enemiesKilled
        self.multiTreasures += self.treasure_carried


    def multiMath(self):
        print ("HEj")


    def thiefStatisticsTotal(self):
        self.totalRuns += self.run
        self.run = 0
        self.totalFinished += self.runFinished
        self.runFinished = 0
        self.totalDead += self.aiDead
        self.aiDead = 0
        self.totalRooms += self.roomAmounts
        self.roomAmounts = 0
        self.totalEnemies += self.enemiesKilled
        self.enemiesKilled = 0

