import pygame
from sys import exit
import random
import math

pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

current_time = 0

yellowimg = pygame.image.load('yellow_circle.png')

deadimg = pygame.image.load('dead.png')

redimg = pygame.image.load('red_circle.png')
redpos = [random.randint(0,984), random.randint(0,984)]
redhp = 100
reddmg = 10
redatkspd = 0.5
redatktime = 0

blueimg = pygame.image.load('blue_circle.png')
bluepos = [random.randint(0,984), random.randint(0,984)]
bluehp = 100
bluedmg = 20
blueatkspd = 0.3
blueatktime = 0

def dist(obj1, obj2):
    return math.sqrt(((obj1[0] - obj2[0])**2) + ((obj1[1] - obj2[1])**2))

def direction(start, end):
    return math.atan2((end[1] - start[1]), (end[0] - start[0]))


running = True
while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if redhp > 0:
        if current_time - redatktime < 100:
            screen.blit(yellowimg, redpos)
        else:
            screen.blit(redimg, redpos)

    if redhp <= 0:
        screen.blit(deadimg, redpos)

    if bluehp > 0:
        if current_time - blueatktime < 100:
            screen.blit(yellowimg, bluepos)
        else:
            screen.blit(blueimg, bluepos)
    elif bluehp <= 0:
        screen.blit(deadimg, bluepos)

    if dist(redpos, bluepos) > 300:
        newrad = direction(redpos, bluepos)
        newx = redpos[0] + (0.3 * math.cos(newrad))
        newy = redpos[1] + (0.3 * math.sin(newrad))
        redpos = [newx, newy]

    elif dist(redpos, bluepos) <= 300 and current_time - redatktime >= 1000*(1/redatkspd) and redhp > 0 and bluehp > 0:
        bluehp -= reddmg
        print(f"Blue {bluehp} hp")
        redatktime = pygame.time.get_ticks()



    if dist(redpos, bluepos) > 100:
        newrad = direction(bluepos, redpos)
        newx = bluepos[0] + (0.3 * math.cos(newrad))
        newy = bluepos[1] + (0.3 * math.sin(newrad))
        bluepos = [newx, newy]

    elif dist(redpos, bluepos) <= 100 and abs(blueatktime - current_time) >= 1000*(1/blueatkspd) and bluehp > 0 and redhp > 0:
        redhp -= bluedmg
        print(f"Red {redhp} hp")
        blueatktime = current_time

    if bluepos[0] <= 0:
        bluepos[0] = 0
    if bluepos[0] >= 984:
        bluepos[0] = 984
    if bluepos[1] <= 0:
        bluepos[1] = 0
    if bluepos[1] >= 984:
        bluepos[1] = 984

    if redpos[0] <= 0:
        redpos[0] = 0
    if redpos[0] >= 984:
        redpos[0] = 984
    if redpos[1] <= 0:
        redpos[1] = 0
    if redpos[1] >= 984:
        redpos[1] = 984





    pygame.display.update()







