from characterClass import Character

class AIWizard(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Wizard"

    def __init__(self):
        initiative_ = 6
        endurance_ = 4
        attack_ = 9
        agility_ = 5
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
        self.totalGold = 0
        Character.__init__(self, "AI-Wizard", initiative_, endurance_, attack_, agility_)

    def earn_treasure(self):
        for item in self.treasure_carried:
            self.treasure_saved += item.gold
        self.treasure_carried = []

    def to_String(self):
        return "1"

    def multipleRuns(self):
        self.multiRuns += self.run
        self.multiFinished += self.runFinished
        self.multiDead += self.aiDead
        self.multiRooms += self.roomAmounts
        self.multiEnemies += self.enemiesKilled
        gold = 0
        for items in self.treasure_carried:
            gold += items.gold
        self.multiTreasures += gold

        self.clear_run()

    def clear_run(self):
        self.run = 0
        self.runFinished = 0
        self.aiDead = 0
        self.roomAmounts = 0
        self.enemiesKilled = 0
        self.treasure_carried = []

    def resetMulti(self):
        self.multiRuns = 0
        self.multiFinished = 0
        self.multiDead = 0
        self.multiRooms = 0
        self.multiEnemies = 0
        self.multiTreasures = 0



    def wizardStatisticsTotal(self):
        self.totalRuns += self.run
        self.totalFinished += self.runFinished
        self.totalDead += self.aiDead
        self.totalRooms += self.roomAmounts
        self.totalEnemies += self.enemiesKilled
        self.treasure_saved += self.multiTreasures

    def print_single_run(self):
        print("Run statistics for AI-Wizard: \n")
        finshed = True
        if self.aiDead == 1:
            finshed = False
        print("Finished run: " +str(finshed))
        print("Cleared rooms: [" + str(self.roomAmounts) + "]\n")
        print("Killed monsters: [" + str(self.enemiesKilled) + "]\n")
        print("Fund treasures: [" + str(self.treasure_saved) + "]\n")
        input("Press any key to return to the previous screen.")
        self.wizardStatisticsTotal()
        self.clear_run()

    def print_stats(self):
        if self.doing_multiple_runs:
            self.printAIWmultiStat()
        else:
            self.print_single_run()

    def totalWStats(self):
        if self.totalRuns == 0:
            print("No runs recorded")
        else:
            print("Total statistics for AI-Wizard: \n")
            print("Total runs: ["+str(self.totalRuns)+"]\n")
            print("Runs completed: [" + str(self.totalFinished) + "]\n")
            print("Total deaths: [" + str(self.totalDead) + "]\n")
            print("Average cleared rooms: [" + str(round(self.totalRooms / self.totalRuns)) + "]\n")
            print("Average killed monsters: [" + str(round(self.totalEnemies / self.totalRuns)) + "]\n")
            print("Average found treasures: [" + str(round(self.treasure_saved / self.totalRuns)) + "]\n")



    def printAIWmultiStat(self):
        print("You are done with " + str(self.multiRuns) + " run(s) with the AI-Wizard class.\nThe statistics are:\n")
        print("It completed the dungeon " + str(self.multiFinished) + " times.\n")
        if self.multiDead > 0:
            print("The AI died " + str(self.multiDead) + " time(s) during the runs.\n")
        print("The average amount of visited rooms are: " + str(round(self.multiRooms / self.multiRuns)) + "\n")
        print("The average amount of killed monsters during the runs are: " + str(round(self.multiEnemies / self.multiRuns)) + "\n")
        print("The average amount of treasures gathered during the runs: " + str(round(self.multiTreasures / self.multiRuns)) + "\n\n")

        self.resetMulti()
