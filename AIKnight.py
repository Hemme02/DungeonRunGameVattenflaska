from characterClass import Character

class AIKnight(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Knight"

    def __init__(self):
        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        self.AI = True
        self.IsAlive = True
        self.doing_multiple_runs = False
        self.class_name = "Knight"
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
        Character.__init__(self, "AI-Knight", initiative_, endurance_, attack_, agility_)

    def earn_treasure(self):
        for item in self.treasure_carried:
            self.treasure_saved += item.gold
        self.treasure_carried = []

    def to_String(self):
        return "2"

    def multipleRuns(self):
        self.multiRuns += self.run
        self.multiFinished += self.runFinished
        self.multiDead += self.aiDead
        self.multiRooms += self.roomAmounts
        self.multiEnemies += self.enemiesKilled
        self.multiTreasures += self.treasure_carried

    def resetMulti(self):
        self.multiRuns = 0
        self.multiFinished = 0
        self.multiDead = 0
        self.multiRooms = 0
        self.multiEnemies = 0
        self.multiTreasures = 0

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


    def totalStats(self):
        print("Total statistics for AI-Knight: \n")
        print("Total runs: ["+str(self.totalRuns)+"]\n")
        print("Runs completed: [" + str(self.totalFinished) + "]\n")
        print("Total deaths: [" + str(self.totalDead) + "]\n")
        print("Average cleared rooms: [" + str(round(self.totalRooms / self.totalRuns)) + "]\n")
        print("Average killed monsters: [" + str(round(self.totalEnemies / self.totalRuns)) + "]\n")
        print("Average found treasures: [" + str(round(self.treasure_saved / self.totalRuns)) + "]\n")
        input("Press any key to return to the previous screen.")

    def printAImultiStat(self):
        print("You are done with" + str(self.multiRuns) + " run(s) with the AI-Knight class.\nThe statistics are:\n")
        print("It completed the dungeon " + str(self.multiFinished) + " times.\n")
        if self.multiDead > 0:
            print("The AI died " + str(self.multiDead) + " time(s) during the runs.\n")
        print("The average amount of visited rooms are: " + str(round(self.multiRooms / self.multiRuns)) + "\n")
        print("The average amount of killed monsters during the runs are " + str(round(self.multiEnemies / self.multiRuns)) + "\n")
        print("The average amount of treasures gathered during the runs: " + str(round(self.multiTreasures / self.multiRuns)) + "\n\n")
        input("All data will be saved in the database, press any key to return to the startscreen!")
        self.resetMulti()

