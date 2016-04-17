import pygame
import random

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

v = vector([random.random()*1000, random.random()*1000])
r = vector([100, 100])


prev_t = pygame.time.get_ticks()
ar = pygame.PixelArray(screen)

while True:
    delta = clock.tick(50) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    r.x[0] += v.x[0] * delta
    r.x[1] += v.x[1] * delta

    if r.x[0] < 200:
        if v.x[0] < 0:
            v.x[0] = -v.x[0]
            r.x[0] = 20
    if r.x[1] < 20:
        if v.x[1] < 0:
            v.x[1] = -v.x[1]
            r.x[1] = -20
    if r.x[0] > 600:
        if v.x[0] > 0:
            v.x[0] = -v.x[0]
            r.x[0] = 600
    if r.x[1] > 600:
        if v.x[1] > 0:
            v.x[1] = -v.x[1]
            r.x[1] = 600


    screen.fill((0, 0, 0))
    col = 255
    pygame.draw.circle(screen, (col/4, col/2, col/3), (int(r.x[0]), int(r.x[1])), 20)
    pygame.display.flip()
