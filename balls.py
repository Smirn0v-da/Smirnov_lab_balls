import pygame
from pygame.draw import *
from random import randint
pygame.init()

#длина и ширина экрана 
a = 800
b = 600
screen = pygame.display.set_mode((a, b))

#установка частоты кадров 
FPS = 30

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
balls_quantity = 10
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

def draw_ball(i):
    '''
    Функция рисует круглую мишень c заданными параметрами
    '''
    circle(screen, balls_color[i], (balls_x[i], balls_y[i]), balls_r[i])
    circle(screen, BLACK, (balls_x[i], balls_y[i]), balls_r[i], 1)

def new_ball(i):
    '''
    Функция задает параметры новой круглой мишени и рисует её
    i - номер мишени
    balls_x, balls_y - координаты центра мишени
    balls_r - радиус мишени
    balls_Vx, balls_Vy - проекции скоростей мишени на оси
    balls_color - цвет мишени
    '''
    global balls_x, balls_y, balls_r, balls_Vx, balls_Vy, balls_color
    balls_x[i] = randint(100, a - 100)
    balls_y[i] = randint(100, b - 100)
    balls_r[i] = randint(30,50)
    balls_Vx[i] = randint(-10, 10)
    balls_Vy[i] = randint(-10, 10) 
    balls_color[i] = COLORS[randint(0, 5)]
    draw_ball(i)

def draw_square(i):
    '''
    Функция рисует квадратную мишень с заданными параметрами
    '''
    rect(screen, squares_color[i], (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                    squares_r[i] * 2, squares_r[i] * 2))
    rect(screen, BLACK, (squares_x[i] - squares_r[i], squares_y[i] - squares_r[i],
                                    squares_r[i] * 2, squares_r[i] * 2), 1)
    
def new_square(i):
    '''
    Функция задает параметры новой квадратной мишени и рисует её
    i - номер мишени
    squares_x, squares_y - координаты центра мишени
    squares_r - половина длины мишени
    squares_x0, squares_y0 - координаты точки, к которой будет двигаться мишень
    squares_Vx, squares_Vy - проекции скоростей мишени на оси
    squares_color - цвет мишени
    '''
    global squares_x, squares_y, squares_Vx, squares_Vy, squares_r, squares_color, squares_x0, squares_y0
    squares_x[i] = randint(150, a - 150)
    squares_y[i] = randint(150, b - 150)
    squares_r[i] = randint(10,20)
    squares_x0[i] = randint(squares_r[i], a - squares_r[i])
    squares_y0[i] = randint(squares_r[i], b - squares_r[i])
    squares_Vx[i] = randint(5, 10)
    squares_Vy[i] = randint(5, 10)
    squares_color[i] = COLORS[randint(0, 5)]
    draw_square(i)

def ball_move(i):
    '''
    Функция для движения круглой мишени
    '''
    global balls_x, balls_y, balls_r, balls_Vx, balls_Vy, balls_color
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
        
    draw_ball(i)

def square_move(i):
    '''
    Функция для движения квадратной мишени к точке (squares_x0, squares_y0)
    Если одна из координат мишени достигает нужного значения, то её скорость по другой оси увеличивается
    '''
    global squares_x, squares_y, squares_Vx, squares_Vy
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
        draw_square(i)
        
def click(event):
    '''
    Функция считывает, попали ли мы по мишени, и ведет счет.
    При попадании мишень исчезает и рисуется новая
    '''
    global score
    #координаты курсора
    event.x = event.pos[0]
    event.y = event.pos[1]
    for i in range(0, balls_quantity):
        if (event.x - balls_x[i]) ** 2 + (event.y - balls_y[i]) **2 <= balls_r[i]**2:
            score += 1 #количество очков за круглую мишень
            screen.fill(BLACK)
            new_ball(i)
    for i in range (0, squares_quantity):
        if (squares_x[i] - squares_r[i] <= event.x) and (event.x <= squares_x[i] + squares_r[i]):
                if (squares_y[i] - squares_r[i] <= event.y) and (event.y <= squares_y[i] + squares_r[i]):
                    score += 2 #количество очков за квадратную мишень
                    screen.fill(BLACK)
                    new_square(i)
    pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

#рисование первых мишеней 
for i in range(0, balls_quantity):
    new_ball(i)
for i in range(0, squares_quantity):
    new_square(i)
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            print('Ваш счет:',score) #выводит счет игрока по окончании игры 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            
    #двигаем мишени
    for i in range(0, balls_quantity):
        ball_move(i)
    for i in range(0, squares_quantity):
        square_move(i)
        
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
