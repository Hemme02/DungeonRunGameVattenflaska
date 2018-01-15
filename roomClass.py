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

#This function generates a room, calls two other funcs.
    def roomGenerator(self):
        self.monsterGenerator()
        self.itemGenerator()

#This function will empty the room and turn it into the exit-room.
    def exitRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.exit = True
#This function will create a startingroom that will clear the room and make the room visited.
    def startingRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.visited = True

# If you visit a room the status will be changed to visited.
    def visitedRoom(self):
        self.visited = True
        return self.visited

#Function with a generator that spawns spawn mob-objects in a room.
    def monsterGenerator(self):
        if self.Randomizer() <= 5:
            self.aliveMonsters.append(Troll())
        if self.Randomizer() <= 15:
            self.aliveMonsters.append(Skeleton())
        if self.Randomizer() >= 10:
            self.aliveMonsters.append(Orc)
        if self.Randomizer() <= 20:
            self.aliveMonsters.append(GiantSpider)
        return self.aliveMonsters

#Function with a generator that spawns treasure-objects in a room.
    def itemGenerator(self):
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

#Function that randomize
    def Randomizer(self):
        randomizer = random.randint(1, 100)
        return randomizer

