import random

class Player:
    """
    Represents a TFT player in the game.
    """

    def __init__(self, name, shop=[0,0,0,0,0], level=2, xp=0, gold=0, hp=100, bench=[0,0,0,0,0,0,0,0,0], board=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]], items=[0,0,0,0,0,0,0,0,0,0], isdead=False, matchmaking = [], isready = False):

        self.name = name
        self.shop = shop
        self.level = level
        self.xp = xp
        self.gold = gold
        self.hp = hp
        self.bench = bench
        self.board = board
        self.items = items
        self.isdead = isdead
        self.matchmaking = matchmaking
        self.isready = isready

    def status(self):
        return f"Player: {self.name} Level: {self.level} XP: {self.xp} Gold: {self.gold} HP: {self.hp}\nShop: {self.shopdisplay()}\nBench: {self.benchstatus()}\nItems: {self.itemstatus()}\nBoard\n{self.boardstatus()[0]}\n{self.boardstatus()[1]}\n{self.boardstatus()[2]}\n{self.boardstatus()[3]}"



    def itemstatus(self):
        display = []
        for item in self.items:
            if type(item) != int:
                display.append(item.name)
            else:
                display.append(0)
        return display

    def benchstatus(self):
        display = []
        for champ in self.bench:
            if type(champ) != int:
                display.append((champ.name, champ.level, champ.champitems()))
            else:
                display.append(champ)
        return display

    def boardstatus(self):
        status = []
        for row in self.board:
            display = []
            for champ in row:
                if type(champ) != int:
                    display.append((champ.name, champ.level, champ.champitems()))
                else:
                    display.append(champ)
            status.append(display)
        return status

    def shopdisplay(self):
        display = []
        for champ in self.shop:
            if type(champ) != int:
                display.append(champ.name)
            else:
                display.append(champ)
        return display

    def readycheck(self):
        self.isready = True

    def kill(self):
        self.isdead = True

    def matchup(self, players):
        for player in self.matchmaking:
            players.remove(player)
        return random.choice(players)


