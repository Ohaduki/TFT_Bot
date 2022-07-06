"""from GameState import gamestate
from player import Player
from Champions import Caitlyn, BlitzCrank, GangPlank, Alistar, Silco
from Items import BFSword, DeathBlade
from Items import Item
from PyGameClass import dist, Gamechamp
from Battle import spawn, fightinground



player1 = Player("player1", gold= 10000, items = [BFSword(), BFSword(), 0, 0, 0, 0, 0, 0, 0, 0])
player2 = Player("player2", gold= 0)
player3 = Player("player3")
player4 = Player("player4")
player5 = Player("player5")
player6 = Player("player6")
player7 = Player("player7")
player8 = Player("player8")

players = [player1, player2, player3, player4, player5, player6, player7, player8]

pool = {1: [Caitlyn() for i in range(29)],
2: [BlitzCrank() for i in range(22)],
3: [GangPlank() for i in range(18)],
4: [Alistar() for i in range(12)],
5: [Silco() for i in range(10)]}


while True:
    gamestate(players, pool)


player1 = Player("player1", board = [[0,0,0,Caitlyn(),0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,Silco(),0,0],[0,0,0,0,0,0,0]])

player2 = Player("player2", board = [[0,0,0,Caitlyn(),0,0,0],[0,0,0,BlitzCrank(),0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,GangPlank(),0,0]])

test1 = spawn(player1, player2)[0]
test2 = spawn(player1, player2)[1]



print(fightinground(test1, test2))"""


