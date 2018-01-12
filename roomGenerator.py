from roomClass import Room
from Troll import Troll
from Skeleton import Skeleton
from Orc import Orc
from GiantSpider import GiantSpider
import random

class collectionOfObjects(Room):
    def __init__(self):
        self.aliveMonsters = []
        self.existingItems = []


    def roomGenerator(self): # körs i varje rum
        self.monsterGenerator()
        self.itemGenerator()



    def exitRoom(self,i): ## design fråga, men kan vara användbar

        if self.exit == True:
            self.existingItems.pop(all(i))
            self.aliveMonsters.pop(all(i))


    def visitedRoom(self):

        self.visited = True

        return self.visited


    def monsterGenerator(self): # vi kan optimera random generatorn tror vi.
        randomizer1 = random.randint(1,100)
        randomizer2 = random.randint(1,100)
        randomizer3 = random.randint(1,100)
        randomizer4 = random.randint(1,100)

        if randomizer1 <= 5:
            self.aliveMonsters.append(Troll())
        if randomizer2 <= 15:
            self.aliveMonsters.append(Skeleton())
        if randomizer3 >= 10:
            self.aliveMonsters.append(Orc)
        if randomizer4 <= 20:
            self.aliveMonsters.append(GiantSpider)

        return self.aliveMonsters


    def itemGenerator(self):# vi kan optimera random generatorn tror vi.
        randomizer1 = random.randint(1, 100)
        randomizer2 = random.randint(1, 100)
        randomizer3 = random.randint(1, 100)
        randomizer4 = random.randint(1, 100)

        if randomizer1 <= 40:
            self.existingItems.append(LooseCoins())
        if randomizer2 <= 20:
            self.existingItems.append(MoneyBag())
        if randomizer3 <= 15:
            self.existingItems.append(GoldJewelry())
        if randomizer4 <= 10:
            self.existingItems.append(GemStone())
        if randomizer5 <= 5:
            self.existingItems(SmallTreasureChest())

        return self.existingItems


