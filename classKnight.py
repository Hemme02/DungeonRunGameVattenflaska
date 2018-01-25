from characterClass import Character
from GiantSpider import GiantSpider
from Orc import Orc
from Skeleton import Skeleton
from Troll import Troll
class Knight(Character):
    treasure_saved = 0
    treasure_carried = []
    class_type = "Knight"

    def __init__(self, name_):

        initiative_ = 5
        endurance_ = 9
        attack_ = 6
        agility_ = 4
        self.dead_giantSpider = 0
        self.dead_troll = 0
        self.dead_skeleton = 0
        self.dead_orc = 0
        self.runFinished = 0
        self.treasures = 0
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

    def totalOfFinishedRun(self):
        self.runFinished = self.runFinished + 1

    def toStringStatistics(self):
        to_return = ("Total Giant Spiders killed:" + str(self.dead_giantSpider) + "\n" "Total Troll Killed:" + str(
            self.dead_troll) + "\n" "Total Skeleton killed:" +
                     str(self.dead_skeleton) + "\n" "Total Orc killed:" + str(
            self.dead_orc) + "\n" "Total gold :" + str(
            self.treasure_saved) + "\n" "Total runs finished :" + str(self.runFinished))
        return to_return











