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

#Function that generates rooms with mobs and Items, triggers two other functions.
    def roomGenerator(self):
        self.monsterGenerator()
        self.itemGenerator()

#Function that clear the room and turn it into a exit-room.
    def exitRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.exit = True

# Function that clears the room, turn visited to true, then creates a starting-room.
    def startingRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.visited = True

#Changes the visited to true when you visited the room.
    def visitedRoom(self):

        self.visited = True

    # Generate mobs into the room.
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

#Generates items and put them in the created room.
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

#Function with a randomizer
    def Randomizer(self):
        randomizer = random.randint(1, 100)

        return randomizer

