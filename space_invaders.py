import pygame
import random

pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Space Invaders')
game_over=False
blue=(0,0,255)
red=(255,0,0)
first_enemy =(150, 50)
second_enemy = (200, 50)
third_enemy = (250, 50)

class Bullet():
    def __init__()

points = 0
x1 = 200
y1 = 150 
x1_change = 0       
y1_change = 0
bullet_x_change = 0
bullet_y_change = 0
enemy_list = [first_enemy, second_enemy, third_enemy]
FPS_TICK = 60
clock = pygame.time.Clock()
white = (255, 255, 255)
bullet_x = x1
bullet_y = y1
space = False
def update(bullet_y):
    bullet_y -= 5
    return bullet_y
bullet_list = []
bullet = 0
inimigos_list = []
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game_over = True
        if event.type == pygame.KEYUP:
                x1_change = 0
                y1_change = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
                x1_change = -5
                y1_change = 0
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                x1_change = 5
                y1_change = 0
        if pygame.key.get_pressed()[pygame.K_UP]:
                x1_change = 0
                y1_change = -5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
                x1_change = 0
                y1_change = 5
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            bullet_y_change = -5
            bullet_x_change = 0
            space = True
            
    dis.fill(white)
    
    for enemies in enemy_list:
        enemy = pygame.draw.rect(dis,red,[enemies[0], enemies[1],10,10])
        inimigos_list.append(enemies)
    pygame.draw.rect(dis,blue,[x1, y1,10,10])
    if x1 >= 400:
        x1 -= 400
    if x1 <= 0:
        x1 += 400
    if y1 >= 300:
        y1 -= 300
    if y1 <= 0:
        y1 += 300
    x1 += x1_change
    y1 += y1_change
    player_position = [x1, y1]
    bullet_x += bullet_x_change
    bullet_y += bullet_y_change
    if space == True:
        pygame.draw.rect(dis,red,[bullet_x+3, bullet_y, 3, 6])
    if bullet_y <= 0:
        bullet_y = y1
        bullet_x = x1
        space = False
              
    pygame.display.update()
    clock.tick(FPS_TICK)

pygame.quit()
quit()