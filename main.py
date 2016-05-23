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
    def __mul__(self, other):
        a = []
        for i in self.x:
            a.append(i * other)
        return vector(a)

    def scalar(self, b):
        c = 0
        for i in range(0,len(self.x)):
            c += self.x[i] * b.x[i]
        return c
    def abs(self):
        a = 0
        for i in self.x:
            a += i**2
        a **= 0.5
        return a


class Ball:
    def __init__(self, r, v, rad, color = (255/4, 255/2, 255/3)):
        self.r = r
        self.v = v
        self.rad = rad
        self.color = color

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.r.x[0]), int(self.r.x[1])), 5)


class Block:
    color = (93, 124, 79)

    def __init__(self, x1=0, y1=0, x2=0, y2=0, k=0):
        self.x1, self.y1, self.x2, self.y2 , self.k= \
            x1, y1, x2, y2, k

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x1, self.y1, self.x2-self.x1, self.y2-self.y1,))

    def collision(self, ball, delta):
        if (ball.r.x[0] + ball.v.x[0] * delta > self.x1) and (ball.r.x[0] + ball.v.x[0] * delta < self.x2)and (ball.r.x[1] + ball.v.x[1] * delta < self.y2) and (ball.r.x[1] + ball.v.x[1] * delta > self.y1):
            self.k = 1
            if (ball.r.x[0] > self.x2):
                ball.v.x[0] = math.fabs(ball.v.x[0])
            elif (ball.r.x[0] < self.x1):
                ball.v.x[0] = -math.fabs(ball.v.x[0])
            elif (ball.r.x[1] > self.y2):
                ball.v.x[1] = math.fabs(ball.v.x[1])
            elif (ball.r.x[1] < self.y1):
                ball.v.x[1] = -math.fabs(ball.v.x[1])


size = width, height = 600, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
a = 1000

ball = Ball(vector([100, 100]),vector([random.random()*100+100, random.random()*100+100]),  5)

player = [vector([250,595]), vector([0,0])]

prev_t = pygame.time.get_ticks()
ar = pygame.PixelArray(screen)

some = [600]
for i in range(50,600,50):
    some.append(random.random()*30+570)
some.append(600)

blocks = []
for i in range(25, 550, 50):
    y = random.random()*200 + 20
    blocks.append(Block(i,y, i+50, y+ 20))

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
    t = int(player[0].x[0])/50

    pos = vector([t*50 + 50, some[t+1]]) - vector([t*50, some[t]])
    player[0].x[1] = some[t] + pos.x[1]*(player[0].x[0] - t*50)/50
    pos = vector([player[0].x[0] - t*50, player[0].x[1]-some[t]])
    if (pos.x[0] != 0) and (pos.x[1] != 0):
        ab = (pos.x[0]**2 + pos.x[1]**2)**(-0.5)
        pos *= ab
    posn = vector([pos.x[1], -pos.x[0]])
    print(ball.v.scalar(posn))

    ball.r +=  ball.v * delta

    if ball.r.x[0] <= 5:
        if ball.v.x[0] < 0:
            ball.v.x[0] = -ball.v.x[0]
            ball.r.x[0] = 5
    if ball.r.x[1] <= 5:
        if ball.v.x[1] < 0:
            ball.v.x[1] = -ball.v.x[1]
            ball.r.x[1] = 5
    if ball.r.x[0] >= 595:
        if ball.v.x[0] > 0:
            ball.v.x[0] = -ball.v.x[0]
            ball.r.x[0] = 595

    if (ball.v.x[1] > 0) and (math.fabs(ball.r.x[0] - player[0].x[0]) < 25) :
        if math.fabs(ball.r.x[1] - (ball.r.x[0] - player[0].x[0])*pos.x[1] - player[0].x[1]) < 5:
            ball.v = pos * ball.v.scalar(pos) - posn * ball.v.scalar(posn)


    screen.fill((0, 0, 0))
    col = 255

    for i in blocks:
        i.collision(ball, delta)
        if i.k == 1:
            blocks.remove(i)
    for i in blocks:
        i.render(screen)

    for i in range(0, 600, 50):
        pygame.draw.line(screen, (255,255,255), (i, some[i/50]), (i+50, some[i/50 + 1]), 3)

    pygame.draw.line(screen, (255,255,255), (player[0].x[0] - 25, player[0].x[1] - pos.x[1]*25), (player[0].x[0] + 25, player[0].x[1] + pos.x[1]*25), 5)
    ball.render(screen)
    pygame.display.flip()

    if ball.r.x[1] > 600:
        sys.exit()
    if blocks == []:
        sys.exit()