import pygame,sys

pygame.init()

windowSize = (600,400)

window=pygame.display.set_mode(windowSize)

name=pygame.font.SysFont("Courier",25)

paint=name.render("Anil Singh Rajput",1,(255,0,200),(2,5,2))

while True:
    for x in pygame.event.get():
        #print(x)
        if x.type == pygame.QUIT:
            sys.exit()
    window.blit(paint,(150,50)) #paint the string
    pygame.display.update()