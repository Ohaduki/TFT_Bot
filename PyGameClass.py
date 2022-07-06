import math

def dist(obj1, obj2):
    return math.sqrt(((obj1[0] - obj2[0])**2) + ((obj1[1] - obj2[1])**2))

def direction(start, end):
    return math.atan2((end[1] - start[1]), (end[0] - start[0]))

class Gamechamp():
    def __init__(self, location, champion, atktime = 0, isalive = False, stunned = False, target = None):
        self.champion = champion
        self.location = location
        self.mana = self.champion.mana
        self.startingmana = self.champion.startingmana
        self.hp = self.champion.hp[self.champion.level-1]
        self.armor = self.champion.armor
        self.mr = self.champion.mr
        self.damage = self.champion.damage[self.champion.level-1]
        self.atkspd = self.champion.atkspd
        self.atkrange = self.champion.atkrange
        self.atktime = atktime
        self.isalive = isalive
        self.stunned = stunned
        self.target = target


    def kill(self):
        self.isalive = False
        return

    def stun(self):
        self.stun = False
        return


    def targetlock(self, enemies):
        alivenemies = []
        for enemy in enemies:
            if enemy.isalive:
                alivenemies.append(enemy)
        return min(alivenemies, key = lambda a:dist(a.location,self.location))


