import pygame
from pygame.draw import *
from random import randint
pygame.init()

#длина и ширина экрана 
a = 800
b = 600

FPS = 30
screen = pygame.display.set_mode((a, b))

#цвета 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

#количество мишеней разных видов
balls_quantity = 0
squares_quantity = 5

#списки с данными для круглых мишеней
balls_x = [0] * balls_quantity
balls_y = [0] * balls_quantity
balls_Vx = [0] * balls_quantity
balls_Vy = [0] * balls_quantity
balls_r = [0] * balls_quantity
balls_color = [0] * balls_quantity

#списки с данными для квадратных мишеней
squares_x = [0] * squares_quantity
squares_y = [0] * squares_quantity
squares_Vx = [0] * squares_quantity
squares_Vy = [0] * squares_quantity
squares_r = [0] * squares_quantity
squares_color = [0] * squares_quantity
squares_x0 = [0] * squares_quantity
squares_y0 = [0] * squares_quantity

def new_ball(i):
    global balls_x, balls_y, balls_r, balls_Vx, balls_Vy, balls_color
    balls_x[i] = randint(100, a - 100)
    balls_y[i] = randint(100, b - 100)
    balls_r[i] = randint(30,50)
    balls_Vx[i] = randint(-10, 10)
    balls_Vy[i] = randint(-10, 10) 
    balls_color[i] = COLORS[randint(0, 5)]
    circle(screen, balls_color[i], (balls_x[i], balls_y[i]), balls_r[i])

def new_square(i):
    global squares_x, squares_y, squares_Vx, squares_Vy, squares_r, squares_color, squares_x0, squares_y0
    squares_x[i] = randint(150, a - 150)
    squares_y[i] = randint(150, b - 150)
    squares_r[i] = randint(10,20)
    squares_x0[i] = randint(squares_r[i], a - squares_r[i])
    squares_y0[i] = randint(squares_r[i], b - squares_r[i])
    squares_Vx[i] = randint(3, 5)
    squares_Vy[i] = randint(3, 5)
    squares_color[i] = COLORS[randint(0, 5)]
    rect(screen, squares_color[i], (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                    squares_r[i] * 2, squares_r[i] * 2))

def ball_move(i):
    global balls_x, balls_y, balls_r, balls_Vx, balls_Vy, balls_color
    circle(screen, BLACK, (balls_x[i], balls_y[i]), balls_r[i])
    balls_x[i] += balls_Vx[i]
    balls_y[i] += balls_Vy[i]

    #отскакивание от стенок
    if balls_x[i] - balls_r[i] <= 50:
        balls_Vx[i] = -balls_Vx[i]
        balls_x[i] =  50 + balls_r[i]
    if balls_x[i] + balls_r[i] >= a - 50:
        balls_Vx[i] = -balls_Vx[i]
        balls_x[i] = a - 50 - balls_r[i]
    if balls_y[i] - balls_r[i] <= 50:
        balls_Vy[i] = -balls_Vy[i]
        balls_y[i] =  50 + balls_r[i]
    if balls_y[i] + balls_r[i] >= b - 50:
        balls_Vy[i] = -balls_Vy[i]
        balls_y[i] = b - 50 - balls_r[i]   
    circle(screen, balls_color[i], (balls_x[i], balls_y[i]), balls_r[i])

def square_move(i):
    global squares_x, squares_y, squares_Vx, squares_Vy
    rect(screen, BLACK, (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                    squares_r[i] * 2, squares_r[i] * 2))
    if squares_x[i] == squares_x0[i] and squares_y[i] == squares_y0[i]:
        new_square(i)
    else:
        if squares_x[i] < squares_x0[i]:
            if squares_x[i] + squares_Vx[i] < squares_x0[i]:
                squares_x[i] += squares_Vx[i]
            else:
                squares_x[i] = squares_x0[i]
                squares_Vy[i] += squares_Vy[i]
        if squares_x[i] > squares_x0[i]:
            if squares_x[i] - squares_Vx[i] > squares_x0[i]:
                squares_x[i] -= squares_Vx[i]
            else:
                squares_x[i] = squares_x0[i]
                squares_Vy[i] += squares_Vy[i]
        if squares_y[i] < squares_y0[i]:
            if squares_y[i] + squares_Vy[i] < squares_y0[i]:
                squares_y[i] += squares_Vy[i]
            else:
                squares_y[i] = squares_y0[i]
                squares_Vx[i] += squares_Vx[i]
        if squares_y[i] > squares_y0[i]:
            if squares_y[i] - squares_Vy[i] > squares_y0[i]:
                squares_y[i] -= squares_Vy[i]
            else:
               squares_y[i] = squares_y0[i]
               squares_Vx[i] += squares_Vx[i]
        rect(screen, squares_color[i], (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                    squares_r[i] * 2, squares_r[i] * 2))
        
def click(event):
    global score
    event.x = event.pos[0]
    event.y = event.pos[1]
    for i in range(0, balls_quantity):
        if (event.x - balls_x[i]) ** 2 + (event.y - balls_y[i]) **2 <= balls_r[i]**2:
            score += 1
            circle(screen, BLACK, (balls_x[i], balls_y[i]), balls_r[i])
            new_ball(i)
    for i in range (0, squares_quantity):
        if (squares_x[i] - squares_r[i] <= event.x) and (event.x <= squares_x[i] + squares_r[i]):
                if (squares_y[i] - squares_r[i] <= event.y) and (event.y <= squares_y[i] + squares_r[i]):
                    score += 2
                    rect(screen, BLACK, (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                            squares_r[i] * 2, squares_r[i] * 2))
                    new_square(i)
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

for i in range(0, balls_quantity):
    new_ball(i)
for i in range(0, squares_quantity):
    new_square(i)
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваш счет:',score)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    for i in range(0, balls_quantity):
        ball_move(i)
    for i in range(0, squares_quantity):
        square_move(i)
    pygame.display.update()

pygame.quit()
