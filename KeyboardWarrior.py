import pygame
from Settings import *
import sys
import random
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
setting=Settings()
theClock = pygame.time.Clock()

Fps = 120
bg_image=pygame.image.load("space.jpg")
bg_image=pygame.transform.scale(bg_image, (setting.screenWidth, setting.screenHeight))
win=pygame.display.set_mode((setting.screenWidth,setting.screenHeight))
pygame.display.set_caption("KeyboardWarrior")
myfont = pygame.font.SysFont("monospace", 300)
chars=[]
text=""
alphaCom=[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z]
alphab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

label = myfont.render(text, 1, (255,255,0))
while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        sys.exit()
    for i in range(0,len(alphaCom)):
        if keys[alphaCom[i]]:
            chars.append(alphab[i])

    for i in range(0,len(chars)):
        text=text+chars[i]
    win.blit(bg_image,(0,0))
    win.blit(label, (100, 100))
    pygame.display.update()

pygame.mixer.quit()
pygame.quit()
