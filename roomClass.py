from Troll import Troll
from Skeleton import Skeleton
from Orc import Orc
from GiantSpider import GiantSpider
import random
from Items.itemClass import  Items
from Items.gemStone import gemStone
from Items.goldJewelry import goldJewelry
from Items.looseCoins import looseCoins
from Items.moneyBag import moneyBag
from Items.smallTreasureChest import smallTreasureChest





class Room:
    def __init__(self,):
        self.aliveMonsters = []
        self.existingItems = []
        self.visited = False
        self.exit = False
        self.roomGenerator()



    def roomGenerator(self):  # körs i varje rum
        self.monsterGenerator()
        self.itemGenerator()


    def exitRoom(self, i):  ## design fråga, men kan vara användbar
        self.existingItems = []
        self.aliveMonsters = []
        self.exit = True

    def startingRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.visited = True


    def visitedRoom(self):

        self.visited = True

        return self.visited


    def monsterGenerator(self):  # vi kan optimera random generatorn tror vi.

        if self.Randomizer() <= 5:
            self.aliveMonsters.append(Troll())

        if self.Randomizer() <= 15:
            self.aliveMonsters.append(Skeleton())

        if self.Randomizer() >= 10:
            self.aliveMonsters.append(Orc)

        if self.Randomizer() <= 20:
            self.aliveMonsters.append(GiantSpider)

        return self.aliveMonsters


    def itemGenerator(self):  # vi kan optimera random generatorn tror vi.

        if self.Randomizer() <= 40:
            self.existingItems.append(looseCoins())

        if self.Randomizer() <= 20:
            self.existingItems.append(moneyBag())

        if self.Randomizer() <= 15:
            self.existingItems.append(goldJewelry())

        if self.Randomizer() <= 10:
            self.existingItems.append(gemStone())

        if self.Randomizer() <= 5:
            self.existingItems.append(smallTreasureChest())

        return self.existingItems


    def Randomizer(self):
        randomizer = random.randint(1, 100)

        return randomizer

