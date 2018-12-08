'''
Author: Austin Bearden
Date Created: 11.22.2018
Purpose: A high level game engine on top of pygame
Assignment: csci437-low-level-game
'''

# Import pygame library of functions
import sys, pygame

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
        self.mWScreen.fill((12, 0, 12))
        self.go = True

# sprite class
# parameters:
    #
class MiniThing(pygame.sprite.Sprite):
    # this will subclass Sprite

    def __init__(self, color, width, height):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()

    


def main():
    coolDude = MiniWorld(1000, 900)

    color = (255, 0, 0)
    '''
    Update loop:
    All content in this while loop is the game loop section
    Thanks to Pete Shinners to the code here: https://www.pygame.org/docs/tut/PygameIntro.html
    '''
    while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            '''
                ...empty game loop
            '''


            coolThing = MiniThing(color, 24, 24)
            coolGroup = pygame.sprite.Group(coolThing)

            coolGroup.draw(coolDude.mWScreen);
            
            coolDude.mWScreen.fill((240, 240, 255))
            pygame.display.flip()



if __name__ == "__main__":
    main()