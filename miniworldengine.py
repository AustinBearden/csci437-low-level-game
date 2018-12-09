'''
Author: Austin Bearden
Date Created: 11.22.2018
Purpose: A high level game engine on top of pygame
Assignment: csci437-low-level-game
Last modified: 12.08.2018
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

    def update(self):
        self.mWScreen.fill((240, 240, 255))

    # helper methods
    def getScreenWidth(self):
        return self.inputWidth

    def getScreenHeight(self):
        return self.inputHeight

# End of MiniWorld class
        

# sprite class
class MiniThing(MiniWorld, pygame.sprite.Sprite):
    # this will subclass Sprite

    def __init__(self, MiniWorld, color, width, height):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.speed = 0
        self.willCheck = False
        self.theSurface = MiniWorld.mWScreen
        self.world = MiniWorld
       
        
    # end of constructor method

    # begining of helper and action methods
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getSpeed(self):
        return self.speed

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def setSpeed(self, speed):
        self.speed = speed

    def changeXby(self, x):
        self.x += x

    def changeYby(self, y):
        self.y += y

    def changeSpeedBy(self, speedBy):
        self.speed += speedBy

    def setWillCheck(self, willCheck):
        self.boolVal = willCheck

    def getWillCheck(self):
        return self.boolVal
    
    # end of helper and action methods


    # check and respond to key actions
    #   change argument is to define amount changed for each key-press
    # event is the event passed in
    def keyActions(self, event, change):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.changeXby(-change)
            if event.key == pygame.K_RIGHT:
                self.changeXby(change)
            if event.key == pygame.K_UP:
                self.changeYby(-change)
            if event.key == pygame.K_DOWN:
                self.changeYby(change)
    

    # bounds checking
    # check is a boolean for deciding whether we should check bounds or not
    def applyBounds(self):
        if self.getWillCheck():
            width = self.world.getScreenWidth()
            height = self.world.getScreenHeight()
            if self.x >= width:
                self.setX(width - self.width)
            if self.x <= 0:
                self.setX(0)
            if self.y <= 0:
                self.setY(0)
            if self.y >= height:
                self.setY(height - self.height)
        
        
    # Update method
    def update(self, event):
        self.keyActions(event, self.speed)
        self.applyBounds()
        self.theSurface.blit(self.image, (self.x, self.y))
        

## end of MiniThing class