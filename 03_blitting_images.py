import pygame

pygame.init()

#display surface
WINDOWS_WIDTH=600
WINDOW_HEIGHT=600
display_surface=pygame.display.set_mode((WINDOWS_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('blitting images')

#create images
dragon_left_image=pygame.image.load('assets/dragon_left.png')
dragon_left_rect=dragon_left_image.get_rect()
dragon_left_rect.topleft=(0,0)

dragon_right_image=pygame.image.load('assets/dragon_right.png')
dragon_right_rect=dragon_right_image.get_rect()
dragon_right_rect.topright=(WINDOWS_WIDTH,0)


#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #blit images
    display_surface.blit(dragon_left_image,dragon_left_rect)
    display_surface.blit(dragon_right_image,dragon_right_rect)

    pygame.draw.line(display_surface,(255,255,255),(0,80),(WINDOWS_WIDTH,80),3)
    pygame.display.update()


pygame.quit()