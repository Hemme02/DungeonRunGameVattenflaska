import random
from GiantSpider import GiantSpider


def dice_throw(number_of_dices):
    result = 0

    for dice in range(number_of_dices):
        number = random.randint(1,6)
        result += number

    return result
