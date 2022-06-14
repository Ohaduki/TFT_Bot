class Champion:
    def __init__(self, name, cost, health, mana, startingmana, armor, mr, damage, atkspd, crate, atkrange, origins, classes, level=1, items=[0,0,0]):

        self.name = name
        self.cost = cost
        self.health = health
        self.mana = mana
        self.startingmana = startingmana
        self.armor = armor
        self.mr = mr
        self.damage = damage
        self.atkspd = atkspd
        self.crate = crate
        self.range = atkrange
        self.origins = origins
        self.classes = classes
        self.level = level
        self.items = items


# 1 Cost Champs
class Caitlyn(Champion):
    def __init__(self):
        Champion.__init__(self, "Caitlyn", 1, [500, 900, 1620], 110, 0, 15, 15, [50, 90, 162], 0.75, 0.25, 5, ["enforcer"], ["sniper"])


# 2 Cost Champs
class BlitzCrank(Champion):
    def __init__(self):
        Champion.__init__(self, "Blitzcrank", 2, [650, 1170, 2106], 175, 175, 45, 45, [65,117,211], 0.5, 0.25, 1, ["scrap"], ["bodyguard"])


# 3 Cost Champs
class GangPlank(Champion):
    def __init__(self):
        Champion.__init__(self, "Gangplank", 3, [750, 1350, 2430], 50, 0, 40, 40, [75, 135, 243], 0.75, 0.25, 1, ["mercenary"], ["twinshot"])


# 4 Cost Champs
class Alistar(Champion):
    def __init__(self):
        Champion.__init__(self, "Alistar", 4, [1400, 2520, 4536], 170, 85, 80, 80, [100, 180, 324], 0.6, 0.25, 1, ["hextech"], ["colossus"])


# 5 Cost Champs
class Silco(Champion):
    def __init__(self):
        Champion.__init__(self, "Silco", 5, [850, 1530, 2754], 40, 0, 40, 40, [60, 108, 194], 0.65, 0.25, 4, ["mastermind"], ["scholar"])




