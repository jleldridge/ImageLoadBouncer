import pygame, sys, time
from pygame.locals import *

def main():
	#set up pygame
	pygame.init()
	
	WINDOWWIDTH = 800
	WINDOWHEIGHT = 600
	
	#set up the window
	window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption("THE GAME")

	#directions
	DOWNLEFT = 1
	DOWNRIGHT = 3
	UPLEFT = 7
	UPRIGHT = 9

	MOVESPEED = 4

	#colors
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)

	#some block shape that will move
	block1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED,
			'xspeed':5, 'yspeed':5}
	block2 = {'rect':pygame.Rect(100, 70, 100, 70), 'color':BLACK,
			'xspeed':8, 'yspeed':10}
	block3 = {'rect':pygame.Rect(80, 300, 80, 30), 'color':GREEN,
			'xspeed':7, 'yspeed':3}
	
	blocks = (block1, block2, block3)

	#draw the window onto the screen
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		#fill whole window with this bluish color
		window.fill(BLUE)
		for b in blocks:
			#move the block
			b['rect'].right += b['xspeed']
			b['rect'].bottom += b['yspeed']
			
			if b['rect'].right >= WINDOWWIDTH or b['rect'].left <= 0:
				b['xspeed'] = -1*b['xspeed']
			if b['rect'].bottom >= WINDOWHEIGHT or b['rect'].top <= 0:
				b['yspeed'] = -1*b['yspeed']
			
			#draw the block onto the surface
			pygame.draw.rect(window, b['color'], b['rect'])
		
		#draw the window onto the screen
		pygame.display.update()
		#need to import time for this function
		time.sleep(0.02)

if __name__ == '__main__':
	main()
