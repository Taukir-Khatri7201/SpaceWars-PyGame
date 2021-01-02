import pygame
import random

from pygame import mixer

# inititalization for pygame
pygame.init()

# setting up a window
win = pygame.display.set_mode((800, 600))

# naming our game
pygame.display.set_caption("Space Wars")

# x and y are cooridantes
x, y = 50, 50

# width and height are for rectangel
width, height = 40, 60
val = 10

game_icon=pygame.image.load("icon.png")
pygame.display.set_icon(game_icon)

player_image = pygame.image.load("spaceship1.png")
player_x = 350
player_y = 500

def player(player_image, x, y):
    win.blit(player_image,(x,y))

enemy_image=[]
enemy_x = []
enemy_y = []

enemy_flag = []
total_enemies = 5

for i in range(total_enemies):
    enemy_image.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0,800))
    enemy_y.append(random.randint(50,70))
    enemy_flag.append(0)

def enemy(image,x,y):
    win.blit(image,(x,y))

# ready : bullet not moving
# fire  : bullet is moving now

bullet_image=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=500
bullet_change=30
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    win.blit(bullet_image,(x+16,y-32))

# x for enemy , y for bullet

def hitting(x1,y1,x2,y2):
    x_dif=x2-x1
    y_dif=y2-y1
    x_dif*=x_dif
    y_dif*=y_dif
    d=(x_dif+y_dif)**0.5
    if d<27:
        return True
    else:
        return False

f = True

background=pygame.image.load("background.png")
mixer.music.load("background.wav")
mixer.music.play(-1)

score = 0
font = pygame.font.Font('freesansbold.ttf',32)
large_font = pygame.font.Font('freesansbold.ttf', 64)
text_x = 10
text_y = 10

def show_score(x,y):
    s=font.render("Score : "+str(score), True, (255,255,255))
    win.blit(s,(x,y))

def gameover():
    s1=large_font.render("Game Over", True, (250,60,150))
    s2=large_font.render("Your Score : "+str(score), True, (255,255,255))
    win.blit(background, (0,0))
    win.blit(s1,(220,226))
    win.blit(s2,(180,310))

flag=0 # for ending explosion sound
while f:
    pygame.time.delay(40)
    win.blit(background, (0, 0))

    show_score(text_x,text_y)
    # all events for the window are available in pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > val:
        player_x -= val
    if keys[pygame.K_RIGHT] and player_x < 800-val-64:
        player_x += val
    if keys[pygame.K_UP] and player_y > val:
        player_y -= val
    if keys[pygame.K_DOWN] and player_y < 600-val-64:
        player_y += val
    if keys[pygame.K_SPACE]:
        if bullet_state=="ready":
            bullet_sound=mixer.Sound("fire_sound.wav")
            bullet_sound.play()
            bullet_x=player_x
            bullet_y=player_y
            fire_bullet(bullet_x,bullet_y)

    player(player_image,player_x,player_y)
    
    for i in range(total_enemies):
        enemy(enemy_image[i],enemy_x[i],enemy_y[i])

        if enemy_y[i] >= 600-val-64:
            flag=1
            gameover()
            # f=0
            break
        
        if hitting(enemy_x[i],enemy_y[i],player_x,player_y):
            flag=1
            gameover()
            # f=0
            break

        if enemy_flag[i] == 0:
            enemy_x[i] += 10

            if enemy_x[i] >= 800-val-64:
                enemy_x[i] = 800-val-64
                enemy_y[i] += 30
                enemy_flag[i] = 1
        else:
            enemy_x[i] -= 10

            if enemy_x[i] <= 0:
                enemy_x[i] = 0
                enemy_y[i] += 30
                enemy_flag[i] = 0
        
        ishitting = hitting(enemy_x[i], enemy_y[i], bullet_x, bullet_y)

        if ishitting == True:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bullet_y = player_y
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 800)
            enemy_y[i] = random.randint(50, 70)

    if bullet_state=="fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_change

    if bullet_y<=32:
        bullet_state="ready"
        bullet_y=player_y
    if flag==1:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        flag=0

    pygame.display.update()

pygame.quit()
