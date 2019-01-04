from pygame.sprite import *
import time                                                                                     #importing all the necessary libraries
from Settings import *
setting=Settings()                                                                              #creating a Settings object
class Duck(Sprite):
    def __init__(self,setting,win):                                                                  #creating and defining the constructor for the Duck Sprite Class
        Sprite.__init__(self)
        self.win=win
        self.s=setting
        self.image=pygame.image.load("duckDodger.png")
        self.image=pygame.transform.scale(self.image, (self.s.width, self.s.height))                 #load the images for the sprites and scaling it according to the setting
        self.image2=pygame.image.load("duckDodger2.png")
        self.image2=pygame.transform.scale(self.image2, (self.s.width, self.s.height))
        self.rect = self.image.get_rect()
        self.rect=self.rect.inflate(-130,-95)                                                        #creating and adjusting the Duck Sprite Rect
        self.playerX=self.s.x
        self.playerY=self.s.y
        self.win_rect=win.get_rect()
        self.rect.centerx= self.win_rect.centerx
        self.rect.bottom = self.win_rect.bottom
        self.center =float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)
        self.moving_right=False                                                                     #indicator of where the sprite is facing
        self.moving_left=False
    def blitme(self):                                                                               #method to draw and switch images for the sprite
        if self.moving_left==True:
            self.win.blit(self.image2,self.rect.move(-75,-40))
        elif self.moving_right==True:
            self.win.blit(self.image,self.rect.move(-60,-40))
        else:
            self.win.blit(self.image,self.rect.move(-60,-40))
    def playerUpdate(self):                                                                         #method to detect the keyboard input and turning it into movement
        keys=pygame.key.get_pressed()                                                               #and limitting it to the edges of the window
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.right < self.win_rect.right:
            #self.playerX-=setting.vel
            self.center-=setting.vel
            self.moving_left=True
            self.moving_rigth=False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.left>0:
            #self.playerX+=setting.vel
            self.center+=setting.vel
            self.moving_left=False
            self.moving_rigth=True
        elif (keys[pygame.K_UP] or keys[pygame.K_w]):
            #self.playerY-=setting.vel
            self.bottom-=setting.vel
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom <self.win_rect.bottom:
            #self.playerY+=setting.vel
            self.bottom+=setting.vel
        self.rect.centerx=self.center
        self.rect.bottom=self.bottom

class Centurion(Sprite):                                                                        #creating and defining the constructor for the Centurion Sprite Class
    def __init__(self, win, width, height, speedx, startx, starty,image):                       #individual sprite would be created in a specific coordinates
        Sprite.__init__(self)
        self.image = pygame.image.load(image)                                                   #loading and scaling the image for the sprite
        self.image = pygame.transform.scale(self.image, (width, height))
        self.startx = startx
        self.starty = starty
        self.rect=self.image.get_rect()
        self.rect=self.rect.inflate(0,-50).move(0,20)                                           #creating and scaling the Centurion Sprite Rect
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.speedx = speedx
        self.rect.left = startx
        self.rect.top = starty
        self.win = win
        self.win_rect=win.get_rect()


    def movementleft(self):
        self.rect.left -= self.speedx                                                           #method to move them to the left
    def movementright(self):
        self.rect.left += self.speedx                                                           #method to move them to the right

class Button(Sprite):                                                                           #creating and defining the constructor for the Button Sprite Class
    def __init__(self,image,startx,starty):
        Sprite.__init__(Button)
        self.image=pygame.image.load(image)                                                     #loading the image for the sprite
        self.startx = startx
        self.starty = starty
        self.rect=self.image.get_rect()                                                         #creating the Rect from the size of the image
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.rect.left = startx
        self.rect.top = starty
class HitBox(Sprite):                                                                           #creating and defining the constructor for the HitBox Sprite Class
    def __init__(self,startx,starty,width,height):                                              #making the rect to detect collisions
        Sprite.__init__(HitBox)
        self.rect=pygame.Rect(startx,starty,width,height)
