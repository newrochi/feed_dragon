import pygame

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

VELOCITY=5
#load image
dragon_image=pygame.image.load('./assets/dragon_right.png')
dragon_image_rect=dragon_image.get_rect()
dragon_image_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

#game loop
running=True



while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #get a list of the keys currently being pressed
    keys=pygame.key.get_pressed()

    #move continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_image_rect.left>0:
        dragon_image_rect.x-= VELOCITY
    if (keys[pygame.K_RIGHT]or keys[pygame.K_d]) and dragon_image_rect.right<WINDOW_WIDTH:
        dragon_image_rect.x+= VELOCITY
    if (keys[pygame.K_UP]or keys[pygame.K_w]) and dragon_image_rect.top>0:
        dragon_image_rect.y-= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_image_rect.bottom<WINDOW_HEIGHT:
        dragon_image_rect.y+= VELOCITY

    display_surface.fill((0,0,0))

    display_surface.blit(dragon_image,dragon_image_rect)

    pygame.display.update()

    #tick the clock
    clock.tick(FPS)
pygame.quit()