'''
Author: Austin Bearden
Date Created: 11.22.2018
Purpose: A high level game engine on top of pygame
Assignment: csci437-low-level-game
Last modified: 12.8.2018
'''

# Import pygame library of functions
import sys
import pygame

# MiniWorld is the screen inn pygame
# input params to MiniWorld instance:
    # width, height
    # color : rgb for now, but later will be able to take standard color names like CSS can
class MiniWorld():

    def __init__(self, width, height):
        pygame.init()
        self.inputWidth = width
        self.inputHeight = height
        self.mWScreen = pygame.display.set_mode((self.inputWidth, self.inputHeight))
        pygame.display.set_caption('MiniWorld')
        self.mWScreen.fill((12, 0, 12))
        self.go = True
        self.clock = pygame.time.Clock()

    def activate(self):
        self.mWScreen.fill((240, 240, 255))
        

# sprite class
# parameters:
    #
class MiniThing(MiniWorld, pygame.sprite.Sprite):
    # this will subclass Sprite

    def __init__(self, MiniWorld, color, width, height):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.theSurface = MiniWorld.mWScreen
       
        
    # end of constructor method

    # begining of helper and action methods
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getDX(self):
        return self.dx

    def getDY(self):
        return self.dy

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def setDX(self, dx):
        self.dx = dx
    
    def setDY(self, dy):
        self.dy = dy

    def changeXby(self, x):
        self.x += x

    def changeYby(self, y):
        self.y += y

    def changeDXby(self, dx):
        self.dx += dx

    def changeDYby(self, dy):
        self.dy += dy
    
    # end of helper and action methods


    # check and respond to key actions
    #   change argument is to define amount changed for each key-press
    # event is the event passed in
    def keyActions(self, event, change):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left", change)
                self.changeXby(-change)
            if event.key == pygame.K_RIGHT:
                print("Right", change)
                self.changeXby(change)
            if event.key == pygame.K_UP:
                print("Up", change)
                self.changeYby(-change)
            if event.key == pygame.K_DOWN:
                print("Down", change)
                self.changeYby(change)
        
        
    # Update method
    def update(self):
        self.theSurface.fill((240, 240, 255))
        self.theSurface.blit(self.image, (self.x, self.y))

## end of MiniThing class

    

'''
    Update loop:
    All content in this while loop is the game loop section
    Thanks to Pete Shinners for the code at this address: https://www.pygame.org/docs/tut/PygameIntro.html
    '''

def main():
    coolDude = MiniWorld(1000, 900)
    red_color = (255, 0, 0)
    coolDude.activate()
    coolThing = MiniThing(coolDude,red_color, 24, 24)

    while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            '''
                ...was empty game loop
            '''
    
            coolThing.keyActions(event, 10)
            coolThing.update()
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()