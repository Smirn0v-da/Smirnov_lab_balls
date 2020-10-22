import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

k = 10
n = 0
x = [0] * k
y = [0] * k
Vx = [0] * k
Vy = [0] * k
r = [0] * k
color = [0] * k

def new_ball(i):
    global x, y, r, Vx, Vy, color
    x[i] = randint(100,700)
    y[i] = randint(100,500)
    r[i] = randint(30,50)
    Vx[i] = randint(-10, 10)
    Vy[i] = randint(-10, 10) 
    color[i] = COLORS[randint(0, 5)]
    circle(screen, color[i], (x[i], y[i]), r[i])

def ball_move(i):
    global x, y, r, Vx, Vy, color
    circle(screen, BLACK, (x[i], y[i]), r[i])
    x[i] += Vx[i]
    y[i] += Vy[i]
    if x[i] - r[i] <= 50:
        Vx[i] = -Vx[i]
        x[i] =  50 + r[i]
    if x[i] + r[i] >= 750:
        Vx[i] = -Vx[i]
        x[i] = 750 - r[i]
    if y[i] - r[i] <= 50:
        Vy[i] = -Vy[i]
        y[i] =  50 + r[i]
    if y[i] + r[i] >= 550:
        Vy[i] = -Vy[i]
        y[i] = 550 - r[i]   
    circle(screen, color[i], (x[i], y[i]), r[i])

def click(event, k):
    global n
    event.x = event.pos[0]
    event.y = event.pos[1]
    for i in range(0, k):
        if (event.x - x[i]) ** 2 + (event.y - y[i]) **2 <= r[i]**2:
            n += 1
            circle(screen, BLACK, (x[i], y[i]), r[i])
            new_ball(i)
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False



for i in range(0, k):
    new_ball(i)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваши очки:',n)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, k)
    for i in range(0, k):
        ball_move(i)
    pygame.display.update()

pygame.quit()
