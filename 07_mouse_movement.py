import pygame

#initialize pygame
pygame.init()

#create the display surface
DISPLAY_WIDTH=600
DISPLAY_HEIGHT=600
display_surface=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('keyboard movement')
#set game values
VELOCITY=10

#load image
dragon_image=pygame.image.load('./assets/dragon_right.png')
dragon_image_rect=dragon_image.get_rect()
dragon_image_rect.centerx=DISPLAY_WIDTH//2
dragon_image_rect.bottom=DISPLAY_HEIGHT

#main game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # #check for discrete movement
        # if event.type==pygame.KEYDOWN:
        #    if event.key==pygame.K_LEFT:
        #        dragon_image_rect.x-=VELOCITY
        #    if event.key==pygame.K_RIGHT:
        #        dragon_image_rect.x+=VELOCITY
        #    if event.key==pygame.K_UP:
        #        dragon_image_rect.y-=VELOCITY
        #    if event.key==pygame.K_DOWN:
        #        dragon_image_rect.y+=VELOCITY
        #move based on mouse click
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x=event.pos[0]
            mouse_y=event.pos[1]
            dragon_image_rect.centerx=mouse_x
            dragon_image_rect.centery=mouse_y
        if event.type==pygame.MOUSEMOTION and event.buttons[0]==1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx=mouse_x
            dragon_image_rect.centery=mouse_y
    #fill the display surface to cover old images
    display_surface.fill((0,0,0))
    display_surface.blit(dragon_image,dragon_image_rect)
    pygame.display.update()
#quit pygame
pygame.quit()