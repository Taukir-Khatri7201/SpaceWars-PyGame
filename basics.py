import pygame

# inititalization for pygame
pygame.init() 

# setting up a window
win = pygame.display.set_mode((500, 500))

# naming our game
pygame.display.set_caption("First Game")

# x and y are cooridantes
x,y=50,50

# width and height are for rectangel
width,height=40,60
val=5

f=True
while f:
    pygame.time.delay(50)
    
    # all events for the window are available in pygame.event.get()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            f=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>val:
        x-=val
    if keys[pygame.K_RIGHT] and x<500-width-val:
        x+=val
    if keys[pygame.K_UP] and y>val:
        y-=val
    if keys[pygame.K_DOWN] and y<500-height-val:
        y+=val
    
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # pygame.draw.line(3, 3, 3, 497)
    # pygame.draw.line(497, 3, 497, 497)
    pygame.display.update()
pygame.quit()
