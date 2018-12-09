'''
Author: Austin Bearden
Created: 12.08.18
Purpose: To demonstrate using the miniworldengine in a simple game
Assignment: csci437-low-level-game
'''
import sys
import pygame
import miniworldengine


'''
    Update loop:
    All content in this while loop is the game loop section
    Thanks to Pete Shinners for the code at this address: https://www.pygame.org/docs/tut/PygameIntro.html
'''

def main():
    world = miniworldengine.MiniWorld(1000, 900)
    red_color = (255, 0, 0)
    world.activate()
    thing = miniworldengine.MiniThing(world,red_color, 24, 24)
    thing.setSpeed(34)

    while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            '''
                ...was empty game loop
            '''
    
            thing.update(event)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()




