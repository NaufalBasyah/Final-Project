import pygame
from Settings import *
import sys                                                          #importing the necessary libraries
from TextFunctionality import *
import time

setting=Settings()                                                  #intializing the background and setting objects
bg=BackGround("OldScreen2.jpg",setting)
textlist=[]
textinput=[]
textlistwords=[]                                                     #containers to store words and lines of words
textinputwords=[]
count=0

def inputBox():
    global count


    text= newTextBox("Enter text here",setting.screenWidth*.05+25,setting.screenHeight/2-10,setting.screenWidth*.43,0,0,35)
    showTextBox(text)                                                                                                      #a method to create a text input box that will store the words type in it in a list
    entry=textBoxInput(text)
    words=entry.split()
    for x in words:
        textinputwords.append(x)
    textinput.append(entry)
    #print(len(dic))
    count+=1
def runKeyboardWarrior():
    global textlist
    global textinput
    global textlistwords
    global textinputwords
    pygame.init()
    pygame.mixer.pre_init(44100, 16, 2, 4096)                                                   #initiliazing the pygame and pygame.mixer (to play music)
    pygame.mixer.init()
    music3=pygame.mixer.music.load('Ocean-Technology.mp3')
    pygame.mixer.music.set_volume(0.5)                                                          #playing the music with set volume
    pygame.mixer.music.play(-1, 0.0)
    pygame.font.init()
    screen=screenSize(setting.screenWidth,setting.screenHeight)
    myFont = pygame.font.SysFont("Courier",30,True)                                                 #font setting for the instruction text and printed paragraph from the text file
    myFont2 = pygame.font.SysFont("Courier",50,True)
    theClock = pygame.time.Clock()
    Fps=120                                                                                     #setting the Fps
    num=""

    start=None
    run=True



    theClock.tick(Fps)
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                                                         #x icon to quit the window and game
                run=False
        screen.blit(bg.bg_image,(0,0))
        instruction1=myFont2.render("ENTER THE TEXT LINE BY LINE",False,(120,120,120))
        instruction2=myFont2.render("FOLLOWED BY AN ENTER.",False,(120,120,120))                         #blitting the background and instruction text
        screen.blit(instruction1,(110,300))
        screen.blit(instruction2,(110,360))
        if count==0:
            num=randomText(textlist,textlistwords)                                                #choosing at random which file to use and starting the timer
            start=time.time()
        elif len(textinput)==len(textlist)-2:
            rights=0                                                                            #stopping the game when the user has inputed the same a mount of line as the text file paragraph
            total=len(textlistwords)
            for i in range(0,len(textinputwords)):
                if textinputwords[i]==textlistwords[i]:
                    rights+=1
            accuracy=(rights/total)                                                             #printing the result score of accuracy and time
            print("You were",accuracy*100,"% accurate")
            end=time.time()
            print("It took you %.2f seconds"%(end-start))
            print(textlistwords,textinputwords)
            print(len(textinput),len(textlist))
            typepoint=[accuracy*100,(end-start),num]                                        #storing the score value
            run=False

        for line in textlist:
            text=myFont.render(line,False,(0,180,0))                                                    #blitting the text file paragraph
            screen.blit(text,((setting.screenWidth/2)+80,(200+(textlist.index(line)*40))))
        inputBox()                                                                              #creating the input box
    music4 = pygame.mixer.music.load('Daft Punk - Derezzed.mp3')
    return typepoint
# runKeyboardWarrior()


