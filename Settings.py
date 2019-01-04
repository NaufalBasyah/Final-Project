import pygame
import sys                                      #importing the necessary libraries
import os
#Sourced and modified from https://github.com/StevePaget/Pygame_Functions/blob/master/pygame_functions.py
textboxGroup = pygame.sprite.OrderedUpdates()                                       #sprite groups for the textbox
screenRefresh = True
background = None
keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0}                                                                     #key dictionany of pygame designation and their symbols
screen = ""
suface=""
def screenSize(sizex, sizey, xpos=None, ypos=None, fullscreen=False):                               #a method to create game window
    global screen
    global background
    global surface
    if xpos != None and ypos != None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (xpos, ypos + 50)
    else:
        windowInfo = pygame.display.Info()
        monitorWidth = windowInfo.current_w
        monitorHeight = windowInfo.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % ((monitorWidth - sizex) / 2, (monitorHeight - sizey) / 2)       #window sizes with option to use full screen depending on the users computer screen resolution
    if fullscreen:
        screen = pygame.display.set_mode([sizex, sizey], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([sizex, sizey])
    screen.fill((0,0,0))
    pygame.display.set_caption("Graphics Window")
    surface = screen.copy()
    pygame.display.update()
    return screen

def updateDisplay(surface):                                                         #update the screen with any text or textbox that is added to the group
    global background
    textboxRects = textboxGroup.draw(screen)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    textboxGroup.clear(screen, surface)

class newTextBox(pygame.sprite.Sprite):
    global surface
    def __init__(self, text, xpos, ypos, width, case, maxLength, fontSize):                                         #a method to create textbox with specific coordinates,length,and text size
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.width = width
        self.initialText = text
        self.case = case
        self.maxLength = maxLength
        self.boxSize = int(fontSize * 1.7)
        self.image = pygame.Surface((width, self.boxSize))
        self.image.fill((0,0,0))
        pygame.draw.rect(self.image, (0,0,0), [0, 0, width - 1, self.boxSize - 1], 2)
        self.rect = self.image.get_rect()
        self.fontColour = pygame.Color("green")
        self.initialColour = (10,10,10)
        self.font = pygame.font.SysFont("Arial", fontSize-10,True)
        self.rect.topleft = [xpos, ypos]
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
    def update(self, keyevent):                                                                             #update the content of the text box with the character thats inputted into throught the keyboard events
        key = keyevent.key
        unicode = keyevent.unicode
        if key > 31 and key < 127 and (
                self.maxLength == 0 or len(self.text) < self.maxLength):  # only printable characters
            if keyevent.mod in (1, 2) and self.case == 1 and key >= 97 and key <= 122:
                # force lowercase letters
                self.text += chr(key)
            elif keyevent.mod == 0 and self.case == 2 and key >= 97 and key <= 122:
                self.text += chr(key - 32)
            else:
                # use the unicode char
                self.text += unicode

        elif key == 8:
            # backspace. repeat until clear
            keys = pygame.key.get_pressed()
            nexttime = pygame.time.get_ticks() + 200
            deleting = True
            while deleting:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE]:
                    thistime = pygame.time.get_ticks()
                    if thistime > nexttime:
                        self.text = self.text[0:len(self.text) - 1]
                        self.image.fill((0,0,0))
                        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
                        newSurface = self.font.render(self.text, True, self.fontColour)
                        self.image.blit(newSurface, [10, 5])
                        updateDisplay(surface)
                        nexttime = thistime + 50
                        pygame.event.clear()
                else:
                    deleting = False

        self.image.fill((0,0,0))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.text, True, self.fontColour)
        self.image.blit(newSurface, [10, 5])
        if screenRefresh:
            updateDisplay(surface)
    def clear(self):
        self.image.fill((0,0,0))                                                                        #clearing the text box for new input
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, self.width - 1, self.boxSize - 1], 2)
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])
        if screenRefresh:
            updateDisplay(surface)


def showTextBox(box):
    textboxGroup.add(box)                               #showing the text box on screen
    if screenRefresh:
        updateDisplay(surface)
def textBoxInput(textbox, functionToCall=None, args=[]):
    # starts grabbing key inputs, putting into textbox until enter pressed
    global keydict
    textbox.text = ""
    returnVal = None
    while True:
        updateDisplay(surface)
        if functionToCall:
            returnVal = functionToCall(*args)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textbox.clear()
                    if returnVal:
                        return textbox.text, returnVal
                    else:
                        return textbox.text
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    textbox.update(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



class Settings():
    def __init__(self):
        self.screenWidth=1920
        self.screenHeight=900                                           #setting object to store screenheight,screenwidth,centurion size and speed
        self.bg_color= (0,0,0)
        self.vel=30
        self.x=self.screenWidth/2
        self.y=self.screenHeight/2
        self.width=200
        self.height=200
class BackGround():
    def __init__(self,image,setting):                                       #background object to easily grab image and scale it to rge setting's screen size
        self.bg_image=pygame.image.load(image)
        self.bg_image=pygame.transform.scale(self.bg_image, (setting.screenWidth, setting.screenHeight))

duckScore=[]
clickScore=[]
typeScore=[]                                                    #Lists to store scores
