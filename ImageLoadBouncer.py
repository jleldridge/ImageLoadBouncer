'''Demonstrates reading in images from files.'''

import pygame, sys, random
from pygame.locals import *

def main():
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 600
    
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    FOODSIZE = 20
    NEWFOOD = 40
    
    #movement booleans
    mLeft = False
    mRight = False
    mUp = False
    mDown = False

    #set up the game
    pygame.init()
    mainClock = pygame.time.Clock()
    
    #create game window
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Interactive THE GAME")
    
    #loads and changes the picture into a better format for pygame
    image = pygame.image.load('Bouncer.jpg').convert()
    
    bouncer = {'rect': pygame.Rect(300, 80, 100, 100), 'xspeed': 5, 'yspeed': 5,
                'color':GREEN, 
                'image': pygame.transform.scale(image, (100, 100))}
    foodCounter = 0
    foods = []
    
    #loads and changes the picture into a better format for pygame
    image = pygame.image.load('Food.jpg').convert()
    for i in range(20):
        foods.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE),
                        random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE,FOODSIZE),
                        'xspeed': 8, 'yspeed': 8, 'color':WHITE,
                        'image': pygame.transform.scale(image, (FOODSIZE, FOODSIZE))})
    
    nomsound = pygame.mixer.Sound('nom.ogg')
    nomsound.set_volume(0.1)
    channel = nomsound.play()
    
    while True:
        #check for the QUIT event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    mLeft = True
                    mRight = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    mLeft = False
                    mRight = True
                if event.key == K_UP or event.key == ord('w'):
                    mUp = True
                    mDown = False
                if event.key == K_DOWN or event.key == ord('s'):
                    mUp = False
                    mDown = True
            
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == ord('a'):
                    mLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    mRight = False
                if event.key == K_UP or event.key == ord('w'):
                    mUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    mDown = False
        
        #add new food every now and then
        foodCounter += 1
        if foodCounter >= NEWFOOD:
            foodCounter = 0
            foods.append({'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-FOODSIZE),
                        random.randint(0, WINDOWHEIGHT-FOODSIZE), FOODSIZE,FOODSIZE),
                        'xspeed': 8, 'yspeed': 8, 'color':WHITE,
                        'image': pygame.transform.scale(image, (FOODSIZE, FOODSIZE))})
            
        #draw black background
        window.fill(BLACK)
        
        #move the bouncer if a button is pressed
        if mLeft:
            bouncer['rect'].right -= bouncer['xspeed']
        if mRight:
            bouncer['rect'].right += bouncer['xspeed']
        if mUp:
            bouncer['rect'].bottom -= bouncer['yspeed']
        if mDown:
            bouncer['rect'].bottom += bouncer['yspeed']
        
        #draw the bouncer
        window.blit(bouncer['image'], bouncer['rect'])
        
        #foods[:] returns a copy of the foods list, which allows us to iterate
        #over a copy of the list while removing things from the actual list
        for food in foods[:]:
            #remove food if it's intersecting the bouncer
            if bouncer['rect'].colliderect(food['rect']):
                foods.remove(food)
                channel.play(nomsound)
            
        for food in foods:
            #move the food
            food['rect'].right += food['xspeed']
            food['rect'].bottom += food['yspeed']
            #check if it has moved out of window
            if food['rect'].right >= WINDOWWIDTH or food['rect'].left <= 0:
                food['xspeed'] *= -1
            if food['rect'].bottom >= WINDOWHEIGHT or food['rect'].top <= 0:
                food['yspeed'] *= -1
            #draw the food
            window.blit(food['image'], food['rect'])
        
        #draw the window onto the screen
        pygame.display.update()
        #checks if we have iterated through the game loop more than n times
        #in the last second, and sleeps the program for a short time if so.
        #this effectively sets the render speed at n fps, drawing and updating
        #are being done in the same loop, it also causes n updates per second
        mainClock.tick(40)
            

if __name__ == '__main__':
    main()
