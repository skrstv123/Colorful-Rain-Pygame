import pygame 
import time 
import random

pygame.init()

pygame.display.set_caption("MY COLORFUL RAIN")
screen=pygame.display.set_mode((900,500))
timer=pygame.time.Clock()


red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
black=(0,0,0)
grey=(180,180,180)
pink=(230,230,250)
purple=(138,43,226)

cols=[red,blue,green,black,grey,purple,(0,70,0)]

	


def colPicker():
	return random.choice(cols)
	
def rvel():
	return random.randrange(1,6)
	
def rectDraw(tup):
	x,vel=tup[0],tup[1]
	y=tup[2]
	ht,col=110,tup[3]
	ht*=(vel/6)
	
	
	pygame.draw.rect(screen,col,[x,y,2,ht])
	
	y+=vel
def ranht():
	return -random.randrange(300,1000)
			
def lt():
	return random.randrange(25,128)

def purprain():
	xes=[[r,rvel(),ranht(),colPicker()] for r in range(0,900,2)]
	
	
	valid=True
	while valid:
		for ev in pygame.event.get():
			if ev.type==pygame.QUIT:
				pygame.quit()
				quit()
		screen.fill((200,0,255))
		for x in xes:
			rectDraw(x)
		for z in xes:
			z[2]+=z[1]
			if z[2]>600:
				z[2]=ranht()
		
		
		pygame.display.update()
		
		timer.tick(60)


purprain()















