from KeyboardKadet import *
from FlickerClicker import *
from DuckDodger import *
from Scoreboard import *                                                                    #importing the necessary libraries

def duckCheck(a,list):
    if list[0]<a[0]:                                                                        #this method check if the duck dodger game score is higher than the high score and replaces it if it is
        list.pop()
        list.append(a[0])
def clickCheck(a,list):                                                            #this method check if the flicker clicker game score is higher than the high score and replaces it if it is
    if list[0]>a[0]:
        list.pop()
        list.append(a[0])
def typecheck(list1,list2):
    list3=[]                                                                    #this method check if the keyboard kadet game score is higher than the high score and replaces it if it is
    if list1[2]=="1" or list1[2]==1:
        if list1[0]==list2[0][0] and list1[1]<list2[0][1]:
            list1.pop(2)
            list3.append(list1)
            list3.append(list2[1])
            list3.append(list2[2])
        elif list1[0]>list2[0][0]:
            list1.pop(2)
            list3.append(list1)
            list3.append(list2[1])
            list3.append(list2[2])
        else:
            list1.pop(2)
            list3=list2
    elif list1[2]=="2" or list1[2]==2:
        if list1[0]==list2[1][0] and list1[1]<list2[1][1]:
            list1.pop(2)
            list3.append(list2[0])
            list3.append(list1)
            list3.append(list2[2])
        elif list1[0]>list2[1][0]:
            list1.pop(2)
            list3.append(list2[0])
            list3.append(list1)
            list3.append(list2[2])
        else:
            list1.pop(2)
            list3=list2

    elif list1[2]=="3" or list1[2]==3:
        if list1[0]==list2[2][0] and list1[1]<list2[2][1]:
            list1.pop(2)
            list3.append(list2[0])
            list3.append(list2[1])
            list3.append(list1)
        elif list1[0]>list2[2][0]:
            list1.pop(2)
            list3.append(list2[0])
            list3.append(list2[1])
            list3.append(list1)
        else:
            list1.pop(2)
            list3=list2
    print(typepoint)
    return list3
pygame.init()                                                                           #initiating the pygame and pygame.mixer(to play music)
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
music4 = pygame.mixer.music.load('Daft Punk - Derezzed.mp3')
pygame.mixer.music.set_volume(0.3)                                                      #looping the music with specific volume
pygame.mixer.music.play(-1, 0.0)
setting=Settings()
bg=BackGround("startPage.jpg",setting)
bg2=BackGround("scoreboard.jpg",setting)                                                    #making and storing all background needed
bg3=BackGround("scoreboard2.jpg",setting)
start=HitBox(519,594,339,90)
exit=HitBox(1211,603,265,83)
scoreboard=HitBox(0,850,400,70)
spaceship=HitBox(1721,205,190,60)                                                       #all the buttons are pict so the hitbox would serve as the invisible button on top of it
computer=HitBox(825,270,80,50)
controlpanel=HitBox(1266,332,65,50)
screen=pygame.display.set_mode((setting.screenWidth,setting.screenHeight))                      #setting the window
CheckScore(duckScore,clickScore,typeScore)                                                  #checking the highscores from a text file and storing it in the lists below it
duckpoint=[]
clickpoint=[]
typepoint=[]
while True:

    screen.blit(bg.bg_image,(0,0))                                                     #blitting one of the background image
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            writeScore(duckScore,clickScore,typeScore)
            sys.exit()                                                                  #x icon and backspace to quit window/game
        keys=pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            writeScore(duckScore,clickScore,typeScore)
            sys.exit()
    pygame.display.update()
    if event.type==pygame.MOUSEBUTTONDOWN:
        if start.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mixer.quit()
            duckpoint=runDuckDodgers()
            duckCheck(duckpoint,duckScore)
            clickpoint=runReaction()                                                            #if the user click the start the 3 games will play consecutively with no breaks
            clickCheck(clickpoint,clickScore)
            typepoint=runKeyboardWarrior()
            if typepoint[2]==1:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[tinyList,[0,0],[0,0]]
            elif typepoint[2]==2:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[[0,0],tinyList,[0,0]]
            elif typepoint[2]==3:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[[0,0],[0,0],tinyList]
            typeScore=typecheck(typepoint,typeScore)
            showScoreboard(bg3,duckpoint,clickpoint,typepoint2)
            pygame.mixer.music.play(-1, 0.0)
            print(duckpoint,clickpoint,typepoint)
            print(duckScore,clickScore,typeScore)
        elif exit.rect.collidepoint(pygame.mouse.get_pos()):                                    #write down the higscores back on a text file before exiting the window/game
            writeScore(duckScore,clickScore,typeScore)
            sys.exit()
        elif scoreboard.rect.collidepoint(pygame.mouse.get_pos()):                                  #highscore list of the highest scores ever gotten in each respective games
            showScoreboard(bg2,duckScore,clickScore,typeScore)

        elif spaceship.rect.collidepoint(pygame.mouse.get_pos()):                           #if user click the space ship on the start screen it will run the duck dodgers game
            pygame.mixer.quit()                                                             #turn off the start page music
            duckpoint=runDuckDodgers()
            duckCheck(duckpoint,duckScore)                                                  #run the game,store the score, and compare it to the highscore
            poin=[0]
            poin2=[[0,0],[0,0],[0,0]]
            showScoreboard(bg3,duckpoint,poin,poin2)                                        #show score board of the just-achieved score in the game
            pygame.mixer.music.play(-1, 0.0)
            print(duckpoint,clickpoint,typepoint)
            print(duckScore,clickScore,typeScore)
        elif computer.rect.collidepoint(pygame.mouse.get_pos()):                        #if user click the little computer on the start screen it will run the keyboard kadet game
            pygame.mixer.quit()
            poin=[0]
            poin2=[0]
            typepoint=runKeyboardWarrior()                                  #play the game and store the current score
            if typepoint[2]==1:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[tinyList,[0,0],[0,0]]
            elif typepoint[2]==2:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[[0,0],tinyList,[0,0]]
            elif typepoint[2]==3:
                tinyList=[typepoint[0],typepoint[1]]
                typepoint2=[[0,0],[0,0],tinyList]
            typeScore=typecheck(typepoint,typeScore)                        #compare it to the highscore
            showScoreboard(bg3,poin,poin2,typepoint2)                       #show score board of the just-achieved score in the game
            pygame.mixer.music.play(-1, 0.0)
            print(duckpoint,clickpoint,typepoint)
            print(duckScore,clickScore,typeScore)
        elif controlpanel.rect.collidepoint(pygame.mouse.get_pos()):                    #if user click the little control panel on the start screen it will run the flicker clicker game
            pygame.mixer.quit()
            clickpoint=runReaction()
            clickCheck(clickpoint,clickScore)
            poin=[0]                                                                    #run the game,store the score, and compare it to the highscore
            poin2=[[0,0],[0,0],[0,0]]
            showScoreboard(bg3,poin,clickpoint,poin2)                                  #show score board of the just-achieved score in the game
            pygame.mixer.music.play(-1, 0.0)
            print(duckpoint,clickpoint,typepoint)
            print(duckScore,clickScore,typeScore)
writeScore(duckScore,clickScore,typeScore)                              #write the updated score back in the text file
pygame.quit()
pygame.mixer.quit()
