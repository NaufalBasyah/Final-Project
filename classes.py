from pygame import *
from pygame.sprite import *

class Jet(Sprite):
    """initialize the jet"""

    def __init__(self, screen):
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png")
        self.image = pygame.transform.scale(self.image, (90, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 50
        self.screen = screen
        self.move_speed = 6
        """bullet"""
        self.firerates = 2

    def moveleft(self):
        self.rect.x -= self.move_speed
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed
        display.flip()





class Star_bg:
    #resourse of the backgound setting
    def __init__(self,background):
        self.background=image.load(background)
        self.background=pygame.transform.scale(self.background,(800,600))
        self.background_size=self.background.get_size()
        self.background_rect=self.background.get_rect()
        self.width,self.height=self.background_size
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y))

class Bullet(Sprite):
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = 20

        self.image = pygame.image.load("bullets.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen
    def movement(self):
        #self.screen.blit(self.image,[self.startx,self.starty])
        self.rect.left += self.speedx

class Asteroid(Sprite):
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx
        self.starty = starty

        self.speedx = speedx

        self.image = pygame.image.load("meteor.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left = startx
        self.rect.top = starty
        self.screen = screen

    def movement(self):
        """method to move the Asteoid"""
        self.rect.left -= self.speedx


class Button(Sprite):
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button=pygame.image.load(image)
        self.button=pygame.transform.scale(self.button,(300,150))
