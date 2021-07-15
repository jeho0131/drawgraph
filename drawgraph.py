import pygame, sys
from pygame.locals import *

pygame.init()
screen.pygame.display.set_mode((500,500))
color = (255,255,255)
fps = pygame.time.clock()

px = -50
x = -49
py = px ** 2 + 2 * px + 3
y = x ** 2 + 2 * x + 3

def makeGraph():
    global px,x,py,y

    for i in range(100):
        px += 1
        x += 1
        py = px ** 2 + 2 * px + 3
        y = x ** 2 + 2 * x + 3
        pygame.draw.line(screen, (0,0,0), (px + 50,py), (x + 50,y), 5)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    makeGraph()
    pygame.display.update()
    fps.tick(20)
