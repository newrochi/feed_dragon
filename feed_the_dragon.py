import pygame
import random


pygame.init()

#display surface
WINDOWS_WIDTH=800
WINDOWS_HEIGHT=600
display_surface=pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
pygame.display.set_caption('Feed the Dragon!!!')
#game colors
WHITE=(255,255,255)
GREEN=(0,255,0)
#fps and clock
FPS=60
clock=pygame.time.Clock()

#------hud
game_font=pygame.font.Font('./assets/AttackGraffiti.ttf',22)
#score
score=0
game_score=game_font.render('Score: '+str(score),True,GREEN,(0,100,0))
game_score_rect=game_score.get_rect()
game_score_rect.center=(80,30)
#game title
game_title=game_font.render('Feed The Dragon', True, GREEN, WHITE)
game_text_rect=game_title.get_rect()
game_text_rect.center=(WINDOWS_WIDTH//2,30)
#gameover text
gameover_text = game_font.render('Game Over: ', True, GREEN, (0, 100, 0))
gameover_text_rect = game_score.get_rect()
gameover_text_rect.center = (WINDOWS_WIDTH//2, WINDOWS_HEIGHT//2)
#lives
STARTING_LIVES=3
lives=1
player_lives=game_font.render('Lives: '+str(lives),True,GREEN,(0,100,0))
player_lives_rect=game_score.get_rect()
player_lives_rect.center=(WINDOWS_WIDTH-80,30)


#------game sounds
game_music=pygame.mixer.music.load('./assets/music.wav')
pygame.mixer.music.play(-1,0,0)
coin_eat_sound=pygame.mixer.Sound('./assets/sound_1.wav')
coin_miss_sound=pygame.mixer.Sound('./assets/sound_2.wav')

#------gameplay
#dragon
dragon=pygame.image.load('./assets/dragon_right.png')
dragon_rect=dragon.get_rect()
dragon_rect.left=30
dragon_rect.top=50
Dragon_VELOCITY=8
#coin
coin=pygame.image.load('./assets/coin.png')
coin_rect=coin.get_rect()
coin_rect.right=WINDOWS_WIDTH
coin_rect.top=random.randint(60,WINDOWS_HEIGHT)
COINT_STARTING_VELOCITY=5
COIN_VELOCITY=5

#game loop
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # if lives==0 and event.type==pygame.KEYDOWN:
        #     lives=3
    #conituous movement
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_rect.top>50:
        dragon_rect.top-=Dragon_VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom<WINDOWS_HEIGHT:
        dragon_rect.top+=Dragon_VELOCITY
    #dragon eats coin
    if dragon_rect.colliderect(coin_rect):
        coin_eat_sound.play()
        coin_rect.right=WINDOWS_WIDTH
        coin_rect.top=random.randint(60,WINDOWS_HEIGHT)
        score+=1
        game_score = game_font.render('Score: ' + str(score), True, GREEN, (0, 100, 0))
        COIN_VELOCITY+=1
    #move coin
    coin_rect.right-=COIN_VELOCITY
    #dragon misses coin
    if coin_rect.right==0 or coin_rect.right<0:
        coin_miss_sound.set_volume(0.1)
        coin_miss_sound.play()
        lives = lives - 1
        player_lives = game_font.render('Lives: ' + str(lives), True, GREEN, (0, 100, 0))
        coin_rect.right=WINDOWS_WIDTH
        coin_rect.top=random.randint(60,WINDOWS_HEIGHT-32)



    if lives==0:
        pygame.mixer.music.stop()
        display_surface.blit(gameover_text, gameover_text_rect)



    #refresh screen
    display_surface.fill((0,0,0))

        





    #show images on screen
    display_surface.blit(game_title, game_text_rect)
    display_surface.blit(game_score, game_score_rect)
    display_surface.blit(player_lives,player_lives_rect)
    display_surface.blit(dragon,dragon_rect)
    display_surface.blit(coin,coin_rect)



    pygame.draw.line(display_surface,WHITE,(0,50),(WINDOWS_WIDTH,50))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()