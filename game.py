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
    Thanks to Pete Shinners for direction for the game loop: https://www.pygame.org/docs/tut/PygameIntro.html
    Also, much thanks to the tutorial by Harrison at: https://pythonprogramming.net/pygame-python-3-part-1-intro/
'''

def main():
    world = miniworldengine.MiniWorld(1000, 900) # initiate a MinitWorld scene object
    red_color = (255, 0, 0) # defining a color based on rgb values (the only way we can do things in this engine)
    world.activate() # activate this MiniWorld object so that is can be updated
    redblock = miniworldengine.MiniThing(world,red_color, 24, 24) ## initiating a sprite (MiniWorld object, color rgb value, width, heigth)
    redblock.setWillCheck(True)
    redblock.setSpeed(34) ## change set or change the speed

    sky = miniworldengine.MiniThing(world,(151, 149, 201), world.getScreenWidth(), 400)
    sky.setWillCheck(False)
    sky.setSpeed(0)
    sky.setX(0)
    sky.setY(0)

    grass = miniworldengine.MiniThing(world, (34, 139, 34), world.getScreenWidth(), 500)
    grass.setWillCheck(False)
    grass.setSpeed(0)
    grass.setX(0)
    grass.setY(400)


    while 1: # inifinite loop to run game until game window is exited out of
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            # Put more game logic here
            world.update() # update MiniWorld object
            sky.update(event) # update MiniThing object
            grass.update(event) # update MiniThing object
            redblock.update(event) # update scene and sprite location # contains a method that checks for key presses
            
            pygame.display.flip() # update screen

    pygame.quit() # quit game when while loop is broken

if __name__ == "__main__":
    main()




