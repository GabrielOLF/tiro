import pygame
enemy_life = 500

        
class Player:
    def __init__(self):
        self.x_pos = 400
        self.y_pos = 300
    def update_pos(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                x_change = 5
                y_change = 0
                self.x_pos += x_change
                self.y_pos += y_change
        if pygame.key.get_pressed()[pygame.K_UP]:
                x_change = 0
                y_change = -5
                self.x_pos += x_change
                self.y_pos += y_change
        if pygame.key.get_pressed()[pygame.K_DOWN]:
                x_change = 0
                y_change = 5
                self.x_pos += x_change
                self.y_pos += y_change
        if pygame.key.get_pressed()[pygame.K_LEFT]:
                x_change = -5
                y_change = 0
                self.x_pos += x_change
                self.y_pos += y_change  
        return [self.x_pos, self.y_pos]

class Enemy:
    def __init__(self, x_ball_pos, y_ball_pos):
        self.x_ball_pos = x_ball_pos
        self.y_ball_pos = y_ball_pos
        
    def enemy_draw(self):
        enemy =  pygame.draw.rect(dis,black,[self.x_ball_pos, self.y_ball_pos,20,30])
        return enemy

        

        

# Colors
blue = (0,0,255)
red = (255,0,0)
black = (0, 0, 0)
white = (255, 255, 255)



bullet_list = []

pygame.init()
player = Player()
class Bullet:
    def __init__(self):
        self.x_pos = player.update_pos()[0]
        self.y_pos = player.update_pos()[1]
    def update_bullet(self):
        self.y_pos -= 7
        return pygame.draw.rect(dis,black,[self.x_pos, self.y_pos,2,5])
enemy_1 = Enemy(50, 10)
enemy_2 = Enemy(100, 10)
enemy_3 = Enemy(150, 10)
enemy_4 = Enemy(200, 10)
enemy_5 = Enemy(250, 10)
enemy_6 = Enemy(300, 10)
enemy_7 = Enemy(350, 10)
enemy_list = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7]
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Mouse Game')
run = True
clock = pygame.time.Clock()
inimigo_list = []
# FPS
FPS_TICK = 60
while run:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
                run = False
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            bullet = Bullet()
            bullet_list.append(bullet)
         
    dis.fill(white)

    for i in enemy_list:
        inimigo = i.enemy_draw()

    for i in bullet_list: 
        if i.y_pos <= 0:
            bullet_list.remove(i)
        i.update_bullet()
        if pygame.Rect.colliderect(i.update_bullet(), inimigo) == True:
                enemy_life -= 1
                bullet_list.remove(i)
                print('acerto')
        
    
    
    pygame.draw.rect(dis,black,[player.update_pos()[0], player.update_pos()[1],10,10])


    
    pygame.display.update()
    clock.tick(FPS_TICK)


pygame.quit()
quit()
