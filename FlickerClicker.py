import pygame
from Sprites import *
import sys                                                      #importing all the necessary libraries
import time
from Settings import *
import random

bg=BackGround("controlPanel.jpg",setting)
setting=Settings()                                              #creating Settings and BackGround objects
def runReaction():
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)                   #initializing the pygame and the pygame.mixer (to play music)
    pygame.mixer.init()

    win=pygame.display.set_mode((setting.screenWidth,setting.screenHeight))
    pygame.display.set_caption("Reaction Click")
    Fps =120                                                                    #setting the game window,Fps rate, loading the music and sound effect
    music2 = pygame.mixer.music.load('Elevator-music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)
    beep = pygame.mixer.Sound("beep.wav")
    theClock = pygame.time.Clock()
    buttons=Group()                                                             #making a sprite group to detect collision for the buttons
    buttonPos=((200,125),(200,475),(750,125),(750,475),(1300,125),(1300,475))  #a tupple of button positions
    for i in range(0,len(buttonPos)):
            NoButton=Button("RedButton.png",buttonPos[i][0],buttonPos[i][1])            #creating the 6 red buttons
            buttons.add(NoButton)
    green=True
    run=True
    new_butt=False                                                             #variables to keep track of the flashing points
    new_buttons=Group()                                                        #button group to store the green button
    count=0
    reactTime=[]                                                               #a list for the 5 reaction time
    round=0                                                                    # variable to keep track of the rounds

    while run:
        if round>=5:                                                           #this conditional stops the game after 5 rounds

            run=False
        theClock.tick(Fps)                                                      #setting the Fps
        win.blit(bg.bg_image,(0,0))                                             #blitting the background image
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if YesButton.rect.collidepoint(pygame.mouse.get_pos()):        #collision detection  between mouse click position and the green button to stop the timer after it spawned
                    beep.play()
                    end=time.time()
                    react=(end-start)*1000
                    print("%.3f" %(react),"ms")
                    green=True
                    new_butt=False
                    count=0
                    reactTime.append(react)
                    round+=1

        keys=pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:                                            #backspace to quit the window
            sys.exit()
        if green==True:
            buttons.draw(win)                                                   #if the green var is True then the green button hasnt spawn
        elif green==False and new_butt==False:
            for k in range(0,len(buttonPos)):                                           #blitting the other 5 buttons
                if k !=j:
                    NoButton=Button("RedButton.png",buttonPos[k][0],buttonPos[k][1])
                    new_buttons.add(NoButton)
            new_butt=True
            new_buttons.draw(win)
        else:
            new_buttons.draw(win)
        i=random.randint(0,100)                                             #i variable used to randomly generate a number between 0-100 at every loop
        if green==True:
            j=random.randint(0,len(buttonPos)-1)                            #j determines the green button position randomly
        if i==2 or i==10:
            green=False
            YesButton=Button("GreenButton.png",buttonPos[j][0],buttonPos[j][1])
            new_buttons.add(YesButton)
            win.blit(YesButton.image,YesButton.rect)                                #if the i var landed on 2 or 10 the green button will spawn at the j-determined coordinate
            if green==False and count<1:
                start=time.time()
                count+=1


        pygame.display.update()
    print("The average is: %.3f"% (sum(reactTime)/len(reactTime)),"ms")
    clickpoint=[sum(reactTime)/len(reactTime)]                                     #calculating, printing,and storing the final score
    music4 = pygame.mixer.music.load('Daft Punk - Derezzed.mp3')
    return clickpoint

#
# runReaction()
