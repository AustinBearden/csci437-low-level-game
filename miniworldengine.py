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
        self.go = True;

    

def main():
    coolDude = MiniWorld(1000, 900)
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
            
            coolDude.mWScreen.fill((240, 240, 255))
            pygame.display.flip()



if __name__ == "__main__":
    main()