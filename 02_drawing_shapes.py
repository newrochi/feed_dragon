import pygame

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH=600
WINDOW_HEIGHT=600
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('drawing stuff')

#define rgb colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)

#give a background color to the surface
display_surface.fill(RED)

#draw shapes in pygame
#line
pygame.draw.line(display_surface,BLUE,(0,0),(200,200),5)
#circle
pygame.draw.circle(display_surface,GREEN,(80,80),60,6)
#rect
pygame.draw.rect(display_surface,CYAN,(200,200,150,60))

#the main game loop
running=True
while running:
    #loop through a list of event objects that have occurred
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()

#end the game
pygame.quit()