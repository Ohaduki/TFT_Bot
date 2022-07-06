import sys
import math
from PyGameClass import Gamechamp
from player import Player
from Champions import Champion
import pygame


def dist(obj1, obj2):
    return math.sqrt(((obj1[0] - obj2[0])**2) + ((obj1[1] - obj2[1])**2))

def direction(start, end):
    return math.atan2((end[1] - start[1]), (end[0] - start[0]))

def spawn(player1, player2):
    team1 = []
    team2 = []
    for i in range(4):
        for j in range(7):
            if player1.board[i][j] != 0:
                newchamp = Gamechamp(location= [(j * 143) + 70, (i * 125) + 62], champion = player1.board[i][j], isalive = True)
                team1.append(newchamp)

            if player2.board[i][j] != 0:
                newchamp = Gamechamp(location= [(j * 143) + 70, 1000 - ((i * 125) + 62)], champion = player2.board[i][j], isalive = True)
                team2.append(newchamp)

    return (team1, team2)


def fightinground(team1, team2):
    pygame.init()
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    redimg = pygame.image.load('red_circle.png')
    blueimg = pygame.image.load('blue_circle.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()
        screen.fill((0, 0, 0))

        for champ in team1:
            if champ.hp <= 0:
                champ.kill()
            if champ.isalive:
                screen.blit(blueimg, champ.location)
                if not champ.target or not champ.target.isalive:
                    champ.target = champ.targetlock(team2)
                if dist(champ.location, champ.target.location) <= champ.atkrange * 154 and current_time - champ.atktime >= (1000*(1/champ.atkspd)):
                    champ.target.hp -= champ.damage*(100/100+champ.target.armor)
                if dist(champ.location, champ.target.location) >= champ.atkrange * 154:
                    champ.location = [champ.location[0] + math.cos(direction(champ.location, champ.target.location)),
                                      champ.location[1] + math.sin(direction(champ.location, champ.target.location))]

        for champ in team2:
            if champ.hp <= 0:
                champ.kill()
            if champ.isalive:
                screen.blit(redimg, champ.location)
                if not champ.target or not champ.target.isalive:
                    champ.target = champ.targetlock(team1)
                if dist(champ.location,
                        champ.target.location) <= champ.atkrange * 154 and current_time - champ.atktime >= (
                        1000 * (1 / champ.atkspd)):
                    champ.target.hp -= champ.damage * (100 / (100 + champ.target.armor))
                if dist(champ.location, champ.target.location) >= champ.atkrange * 154:
                    champ.location = [champ.location[0] + math.cos(direction(champ.location, champ.target.location)),
                                      champ.location[1] + math.sin(direction(champ.location, champ.target.location))]

        team1count = len(team1)
        for champ in team1:
            if not champ.isalive:
                team1count -= 1
        if team1count == 0:
            return (team2)

        team2count = len(team2)
        for champ in team2:
            if not champ.isalive:
                team2count -= 1
        if team2count == 0:
            return (team1)

        if current_time >= 60000:
            return "DRAW"

        pygame.display.update()