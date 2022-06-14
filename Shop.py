import random
from player import Player
from Champions import Caitlyn, BlitzCrank, GangPlank, Alistar, Silco


def reroll(player, pool):
    # Generates a new shop of champions from the pool that corresponds to the player's level
    if player.level in [1,2]:
        droprate = [100, 0, 0, 0, 0]

    elif player.level == 3:
        droprate = [75, 25, 0, 0, 0]

    elif player.level == 4:
        droprate = [55, 30, 15, 0, 0]

    elif player.level == 5:
        droprate = [45, 33, 20, 2, 0]

    elif player.level == 6:
        droprate = [25, 40, 30, 5, 0]

    elif player.level == 7:
        droprate = [19, 30, 35, 15, 1]

    elif player.level == 8:
        droprate = [16, 20, 35, 25, 4]

    elif player.level == 9:
        droprate = [15, 30, 30, 30, 16]

    elif player.level == 10:
        droprate = [5, 10, 20, 40, 25]

    elif player.level == 11:
        droprate = [1, 2, 12, 50, 35]


    champtiers = random.choices([1,2,3,4,5], weights = droprate, k=5)

    shop = []
    for i in champtiers:
        random.shuffle(pool[i])
        shop.append(pool[i].pop())
    return shop




