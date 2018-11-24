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

    def __init__(self, width, height):
        pygame.init()
        self.inputWidth = width
        self.inputHeight = height
        self.mWScreen = pygame.display.set_mode((self.inputWidth, self.inputHeight))
        self.mWScreen.fill((12, 0, 12))
        self.go = True;

    # def setSize(self, width, height):
    #     # how do I change the size of the screen ?
    #     print("Oh yeah!")

    # def setColor(self, red, yellow, blue):
    #     color = red, yellow, blue
    #     self.mWScreen.fill(color)

    def update(self):
        # Update everything that needs to be updated
        print("Update method")

    # start game play method
    def start(self):
        self.mWScreen = pygame.display.set_mode((self.inputWidth, self.inputHeight))
        self.mWScreen.fill((12, 0, 12))



    # end game play method
    def end(self):
        self.go = False

        

    # change/set color
    # change size

# end of MiniWorld class (basically the scene for the engine)

# # class for sprite
# class MiniThing(pygame.sprite.Sprite, image):
#     def __init__(self):
#         # initiate a pygame sprite



#     # change sprite's image
#     def setImage(image):
#         # content of setImage() method

#     # set sprite's angle
#     def setAngle(angleDegrees):
#         # content of setAngle() method

#     # change sprite's angle by specified amount
#     def changeAngle(angleDegrees):
#         # content of changeAngle() method

#     # set sprite's color + dimension (this only works if no image loaded)
#     def setDimensionColor(color, width, height):
#         # content of setDimensionColor() method

#     # change the sprite's speed
#     def setSpeed(speed):
#         # content of setSpeed() method

#     # set the sprite's position
#     def setPosition(x, y):
#         # content of setPosition() method

    
#     # change the sprite's position by certain x and certain y
#     def changePosition(x, y):
#         # content of changePosition() method


        


# end of MiniThing class (basically the sprite class for the engine)
    

def main():
    coolDude = MiniWorld(1000, 900)
    while(coolDude.go):
        coolDude.start()
        i = 0
        while(i < 30000000):
            i = i + 1
            print("hey man")
            print("hey Jeremy")
        
        coolDude.end()





if __name__ == "__main__":
    main()