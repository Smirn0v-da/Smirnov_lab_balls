import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 10
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r, Vx, Vy, color
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def ball_move():
    global x, y, Vx, Vy, r
    x += Vx
    y += Vy
    screen.fill(BLACK)
    circle(screen, color, (x, y), r)

def click(event):
    global n
    x1 = event.pos[0]
    y1 = event.pos[1]
    if (x1 - x) ** 2 + (y1 - y) **2 <= r**2:
        n += 1
    screen.fill(BLACK)
    new_ball()
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

n = 0
new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваши очки:',n)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    ball_move()
    pygame.display.update()

pygame.quit()
