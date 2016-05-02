import pygame
import random
import sys
import math

pygame.init()

class vector():

    def __init__(self, x = [0]):
        self.x = x

    def __add__(self, b):
        c = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            c.x[i] = self.x[i] + b.x[i]
        return c

    def __sub__(self, b):
        d = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            d.x[i] = self.x[i] - b.x[i]
        return d

    def scalar(self, b):
        c = 0
        for i in range(0,len(self.x)):
            c = c + self.x[i] * b.x[i]
        return c


size = width, height = 600, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
a = 1000

v = vector([random.random()*1000, random.random()*1000])
r = vector([100, 100])
player = [vector([250,595]), vector([0,0])]

prev_t = pygame.time.get_ticks()
ar = pygame.PixelArray(screen)

while True:
    delta = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()



    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player[1].x[0] -= delta * a
    elif pressed[pygame.K_RIGHT]:
        player[1].x[0] += delta * a
    else:
        player[1].x[0] = 0

    if player[0].x[0] <= 25:
        player[1].x[0] = math.fabs(player[1].x[0]/2)
    if player[0].x[0] >= 575:
        player[1].x[0] = -math.fabs(player[1].x[0]/2)


    player[0].x[0] += delta * player[1].x[0]

    blocks = []

    for i in range(25, 600, 50):
        blocks.append(vector((i, 100)))

    r.x[0] += v.x[0] * delta
    r.x[1] += v.x[1] * delta

    if r.x[0] <= 5:
        if v.x[0] < 0:
            v.x[0] = -v.x[0]
            r.x[0] = 5
    if r.x[1] <= 5:
        if v.x[1] < 0:
            v.x[1] = -v.x[1]
            r.x[1] = 5
    if r.x[0] >= 595:
        if v.x[0] > 0:
            v.x[0] = -v.x[0]
            r.x[0] = 595
    if r.x[1] >= 595:
        if (v.x[1] > 0) and (math.fabs(r.x[0] - player[0].x[0]) < 25) :
            v.x[1] = -v.x[1]
            r.x[1] = 590



    screen.fill((0, 0, 0))
    col = 255


    for i in blocks:
        pygame.draw.line(screen, (25,25,50), (i.x[0]-24, i.x[1]), (i.x[0]+24, i.x[1]), 25)

    pygame.draw.line(screen, (255,255,255), (player[0].x[0] - 25, player[0].x[1]), (player[0].x[0] + 25, player[0].x[1]), 5)
    pygame.draw.circle(screen, (col/4, col/2, col/3), (int(r.x[0]), int(r.x[1])), 5)
    pygame.display.flip()
