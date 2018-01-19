import random

from gemStone import gemStone
from goldJewelry import goldJewelry
from looseCoins import looseCoins
from smallTreasureChest import smallTreasureChest

from GiantSpider import GiantSpider
from Orc import Orc
from Skeleton import Skeleton
from Troll import Troll
from moneyBag import moneyBag


class Room:
    def __init__(self,):
        self.aliveMonsters = []
        self.existingItems = []
        self.visited = False
        self.cleared = False
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
        self.cleared = True

# Function that clears the room, turn visited to true, then creates a starting-room.
    def startingRoom(self):
        self.existingItems = []
        self.aliveMonsters = []
        self.visited = True

#Changes the visited to true when you visited the room.
    def visitedRoom(self):

        self.visited = True

    # Generate mobs into the room.

    def clear_room(self):
        self.cleared = True

    def monsterGenerator(self):

        if self.Randomizer() <= 5:
            self.aliveMonsters.append(Troll())

        if self.Randomizer() <= 15:
            self.aliveMonsters.append(Skeleton())

        if self.Randomizer() <= 10:
            self.aliveMonsters.append(Orc())

        if self.Randomizer() <= 20:
            self.aliveMonsters.append(GiantSpider())



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

#Function with a randomizer
    def Randomizer(self):
        randomizer = random.randint(1, 100)

        return randomizer

    def printMobs(self):
        if len(self.aliveMonsters) > 1:
            return self.printListOfMobs()
        else:
            return self.printSingleMob()

    def printSingleMob(self):
        return self.aliveMonsters[0].toStringSingle()

    def printListOfMobs(self):
        returnString = ""
        number_in_list = 0
        length = len(self.aliveMonsters)

        for monster in self.aliveMonsters:
            number_in_list+=1
            returnString += monster.toString()
            if number_in_list < length:
                returnString += "\n"

        return returnString

    def printSingleTreasure(self):
        return self.existingItems[0].toStringSingle()

    def printListOfTreasuer(self):
        returnString = ""
        number_in_list = 0
        length = len(self.existingItems)
        for treasure in self.existingItems:
            number_in_list += 1
            returnString += treasure.toString()
            if number_in_list < length:
                returnString += "\n"
        return returnString

    def printTreasure(self):
        if len(self.existingItems) > 1:
            return self.printListOfTreasuer()
        else:
            return self.printSingleTreasure()

