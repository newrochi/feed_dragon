import pygame

pygame.init()

#display surface
DISPLAY_WIDTH=600
DISPLAY_HEIGHT=600
display_surface=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption("blitting text")

#set colors
GREEN=(0,255,0)
RED=(255,0,0)
BLACK=(0,0,0)

#get a list of the fonts available
fonts=pygame.font.get_fonts()
#load fonts
system_font=pygame.font.SysFont('calibri',64)
custom_font=pygame.font.Font('./assets/AttackGraffiti.ttf',32)

#define text
system_text=system_font.render('Dragon cream!',True,GREEN,RED)
system_text_rect=system_text.get_rect()
system_text_rect.topleft=(50,50)

custom_text=custom_font.render('Living La Vida Loca!',20,RED)
custom_text_rect=custom_text.get_rect()
custom_text_rect.topleft=(60,350)


#game loop
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    display_surface.blit(system_text,system_text_rect)
    display_surface.blit(custom_text,custom_text_rect)
    pygame.display.update()

pygame.quit()