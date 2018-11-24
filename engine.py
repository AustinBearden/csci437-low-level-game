'''
Author: Austin Bearden
Date Created: 11.22.2018
Purpose: A high level game engine on top of pygame
Assignment: csci437-low-level-game
'''

# Import pygame library of functions
import sys, pygame

# input params to MiniWorld instance:
    # width, height
    # color : rgb for now, but later will be able to take standard color names like CSS can
class MiniWorld():

    def __init__(self):
        pygame.init()
        self.mWScreen = pygame.display.set_mode((200, 100))
        self.mWScreen.fill((12, 0, 12))

    def setSize(self, width, height):
        # how do I change the size of the screen ?
        print("Oh yeah!")

    def setColor(self, red, yellow, blue):
        color = red, yellow, blue
        self.mWScreen.fill(color)

    def update(self):
        # Update everything that needs to be updated
        pygame.display.flip()

    # change/set color
    # change size

# end of MiniWorld class (basically the scene for the engine)

# class for sprite
class MiniThing(pygame.sprite.Sprite, image):
    def __init__(self):
        # initiate a pygame sprite


    # change sprite's image
    def setImage(image):


    # set sprite's angle
    def setAngle(angleDegrees):


    # set sprite's color + dimension (this only works if no image loaded)
    def setDimensionColor(color, width, height):


    # 
        
        


# end of MiniThing class (basically the sprite class for the engine)
    

def main():
    coolDude = MiniWorld()
    i = 0
    while(True):
        coolDude.setSize(300, 500)
        coolDude.setColor(0, 0, 0)
        coolDude.update()

if __name__ == "__main__":
    main()