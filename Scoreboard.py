from Settings import *                         #importing the necessary libraries
from Sprites import *
def showScoreboard(background,list1,list2,list3):                                   #a method to show score in a new score page
    pygame.init()
    setting=Settings()                                                                  #intiating pygame and setting object
    screen2=pygame.display.set_mode((setting.screenWidth,setting.screenHeight))
    myFont1 = pygame.font.SysFont("Courier",60,True)                                #setting up the window and the font set up for later use
    myFont = pygame.font.SysFont("Courier",40,True)

    pygame.display.set_caption("Score Board")

    back=HitBox(0,0,140,45)                                                     #back hitbox to quit scoreboard
    duck="%.3f Secs"%(list1[0])
    click="%.3f Ms"%(list2[0])
    type1="%.3f %s and %.3f Secs"%(list3[0][0],"%",list3[0][1])                                 #setting up all the score text with their font set ups
    type2="%.3f %s and %.3f Secs"%(list3[1][0],"%",list3[1][1])
    type3="%.3f %s and %.3f Secs"%(list3[2][0],"%",list3[2][1])
    a=myFont1.render(duck,False,(255,255,255))
    b=myFont1.render(click,False,(255,255,255))
    c=myFont.render(type1,False,(255,255,255))
    d=myFont.render(type2,False,(255,255,255))
    e=myFont.render(type3,False,(255,255,255))
    locList=[(200,290),(183,622),(1242,365),(1242,565),(1242,765)]                      #list of text locations
    while True:
        screen2.blit(background.bg_image,(0,0))                                     #blitting the background and the scores at their specific coordinates
        screen2.blit(a,locList[0])
        screen2.blit(b,locList[1])
        screen2.blit(c,locList[2])
        screen2.blit(d,locList[3])
        screen2.blit(e,locList[4])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                                     #x icon and backspace to quit window/scoreboard
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_BACKSPACE]:
            break
        if event.type==pygame.MOUSEBUTTONDOWN:
            if back.rect.collidepoint(pygame.mouse.get_pos()):
                break                                                           #detecting coliision on the back button(Hitbox)


