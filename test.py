import random


def random_room():
    x_pos = random.randint(0, 5)
    y_pos = random.randint(0, 5)
    return (x_pos, y_pos)

print(random_room())


