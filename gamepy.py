import pygame
import random

from sqlalchemy import true

pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Platform Game')

# Colors
blue = (0,0,255)
red = (255,0,0)
black = (0, 0, 0)
white = (255, 255, 255)
x_pos = 400
y_pos = 300
x1_change = 0
y1_change = 0
# FPS
FPS_TICK = 60
clock = pygame.time.Clock()
gravity = 5
run = True
while run:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
                run = False
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
                gravity_f = False
        else:
            gravity_f = True
        if pygame.key.get_pressed()[pygame.K_DOWN]:
                x1_change = 0
                y1_change = 5
        
    dis.fill(white)
    x_pos += x1_change
    y_pos += y1_change
    player = pygame.draw.rect(dis,black,[x_pos, y_pos,15,15])
    platform = pygame.draw.rect(dis, red, [500, 400, 100, 10])
    if pygame.Rect.colliderect(player, platform) == False and gravity_f != False:
        y_pos += gravity
    elif pygame.Rect.colliderect(player, platform) == True:
        y_pos -= y1_change




    pygame.display.update()
    clock.tick(FPS_TICK)


pygame.quit()
quit()