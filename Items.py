class Item:
    def __init__(self, name, tier=1, combination = None):
        self.name = name
        self.tier = tier
        self.combination = combination

class BFSword(Item):
    def __init__(self):
        Item.__init__(self, "B.F. Sword", 1, 0)

class DeathBlade(Item):
    def __init__(self):
        Item.__init__(self, "Deathblade", 2)


# Function to combine items


itemchart = [[DeathBlade()]]


def itemcombine(item1, item2):
    return itemchart[item1.combination][item2.combination]


item = BFSword()