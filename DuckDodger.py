import pygame
import sys
from Sprites import *
import random                                                                                         #importing the necessary libraries

from Settings import *


def runDuckDodgers():
    import time
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)                                                       #initiating the pygame and pygame mixer(to play music)
    pygame.mixer.init()
    setting=Settings()
    theClock = pygame.time.Clock()
    centurion_group1 = Group()                                                                      #creating two groups for centurion going left and the one going right
    centurion_group2 = Group()
    Fps = 120
    music1 = pygame.mixer.music.load('space_music.mp3')
    pygame.mixer.music.set_volume(0.5)                                                              #playing the music endlessly with specific volume level
    pygame.mixer.music.play(-1, 0.0)
    flock=Group()                                                                                   #group for the duck sprite(a group of duck is called a flock)
    centurion_timer = pygame.time.get_ticks()                                                       #timer ticks
    win=pygame.display.set_mode((setting.screenWidth,setting.screenHeight))
    pygame.display.set_caption("Duck Dodger")                                                       #setting up the window
    duck=Duck(setting,win)
    flock.add(duck)                                                                                 #creating the duck sprite object
    bg=BackGround("space2.jpg",setting)                                                             #setting the background
    run=True
    start=time.time()                                                                               #starting the timer
    while run:

        theClock.tick(Fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                                                             #backspace and x icon to quit window and game
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            sys.exit()
        win.blit(bg.bg_image,(0,0))                                                                 #blitting the background

        centurion_group1.draw(win)                                                                  #drawing all the centurion thats in either group
        centurion_group2.draw(win)

        #win.blit(duck.image,(duck.playerX,duck.playerY))
        duck.blitme()                                                                               #blitting the user controlled sprite(duck)
        #pygame.draw.rect(win, (255,0,0), duck.rect, 2)
        duck.playerUpdate()
        pygame.display.update()                                                                     #update the duck position and image according to keyboard events
        if pygame.time.get_ticks() - centurion_timer >= 800:                                        #spawning the centurion at a random instances
            centurion = Centurion(win, 120, 100, random.randint(1,4)*6, 1920, (random.randint(1,56) * 20),"centurion.png")      #creating the centurion at random y coordinates with random speeds

            centurion_group1.add(centurion)
            centurion_timer = pygame.time.get_ticks()
            centurion = Centurion(win, 120, 100, random.randint(1,4)*6, 0, (random.randint(1,56) * 20),"centurion2.png")
            centurion_group2.add(centurion)
            centurion_timer = pygame.time.get_ticks()

        for centurion in centurion_group1:                                                          #moving some centurion to the left if they spawned on the right
            centurion.movementleft()
            if centurion.rect.right <= 0:
                centurion_group1.remove(centurion)
            if groupcollide(flock,centurion_group1,False,True):

                #continue
                end=time.time()
                score=(end-start)                                                                   #if the user collide with the centurion the game will end and print out the score (how long the user lasted)
                if score<0.001:
                    print("%.3f"%(score*1000),"ms")
                else:
                    print("%.3f"%(score),"seconds")
                run=False
        for centurion in centurion_group2:
            centurion.movementright()
            if centurion.rect.left <= 0:
                centurion_group2.remove(centurion)                                              #the same as the one above but this group goes from the left to the right
            if groupcollide(flock,centurion_group2,False,True):

                #continue
                end=time.time()
                score=(end-start)
                if score<0.001:
                    print("%.3f"%(score*1000),"ms")
                else:
                    print("%.3f"%(score),"seconds")
                run=False
    duckpoint=[score]                                                                   #storing the score
    music4 = pygame.mixer.music.load('Daft Punk - Derezzed.mp3')
    return duckpoint
#
# runDuckDodgers()
