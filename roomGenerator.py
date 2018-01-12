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

        if self.Randomizer() <= 5:
            self.aliveMonsters.append(Troll())

        if self.Randomizer() <= 15:
            self.aliveMonsters.append(Skeleton())

        if self.Randomizer() >= 10:
            self.aliveMonsters.append(Orc)

        if self.Randomizer() <= 20:
            self.aliveMonsters.append(GiantSpider)

        return self.aliveMonsters


    def itemGenerator(self):# vi kan optimera random generatorn tror vi.

        if self.Randomizer() <= 40:
            self.existingItems.append(LooseCoins())

        if self.Randomizer() <= 20:
            self.existingItems.append(MoneyBag())

        if self.Randomizer() <= 15:
            self.existingItems.append(GoldJewelry())

        if self.Randomizer() <= 10:
            self.existingItems.append(GemStone())

        if self.Randomizer() <= 5:
            self.existingItems(SmallTreasureChest())

        return self.existingItems


    def Randomizer(self):
        randomizer = random.randint(1,100)

        return randomizer