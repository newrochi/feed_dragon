import  pygame

#initialize pygame
pygame.init()
#create display surface
DISPLAY_WIDTH=600
DISPLAY_HEIGHT=600
display_surface=pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('Sound effects in pygame')

#load sound effects
sound_1=pygame.mixer.Sound('./assets/sound_1.wav')
sound_2=pygame.mixer.Sound('./assets/sound_2.wav')
#play sound effects
sound_1.play()
pygame.time.delay(2000)
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(0.2)
sound_2.play()
#load background music
pygame.mixer.music.load('./assets/music.wav')
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

#create game loop
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


pygame.quit()