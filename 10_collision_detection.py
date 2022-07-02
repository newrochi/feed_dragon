import pygame,random

#initialize
pygame.init()

#create display surface
WINDOW_WIDTH=600
WINDOW_HEIGHT=600
display_surface=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Restricted movement')

#set fps and clock
FPS=60
clock=pygame.time.Clock()

VELOCITY=8

#load images
dragon_image=pygame.image.load('./assets/dragon_right.png')
dragon_rect=dragon_image.get_rect()
dragon_rect.topleft=(25,25)
coin_image=pygame.image.load('./assets/coin.png')
coin_rect=coin_image.get_rect()
coin_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)



running=True



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dragon_rect.left>0:
        dragon_rect.left-=VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right<WINDOW_WIDTH:
        dragon_rect.right+=VELOCITY
    if keys[pygame.K_UP] and dragon_rect.top>0:
        dragon_rect.top-=VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom<WINDOW_HEIGHT:
        dragon_rect.bottom+=VELOCITY
    display_surface.fill((0,0,0))

    #check for collision
    if dragon_rect.colliderect(coin_rect):

        coin_rect.x=random.randint(0,WINDOW_WIDTH-32)
        coin_rect.y=random.randint(0,WINDOW_HEIGHT-32)

    #draw rectangles to represent rect's of each object
    #pygame.draw.rect(display_surface,(255,0,0),dragon_rect,1)
    #pygame.draw.rect(display_surface,(0,255,0),coin_rect,1)
    #blit images
    display_surface.blit(dragon_image,dragon_rect)
    display_surface.blit(coin_image,coin_rect)

    pygame.display.update()

    #tick the clock
    clock.tick(FPS)
pygame.quit()