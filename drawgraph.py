import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((500,500))
color = (255,255,255)
fps = pygame.time.Clock()

px = -50
x = -49
py = px ** 2 + 2 * px + 3
y = x ** 2 + 2 * x + 3

def makeGraph():
    global px,x,py,y

    px = -50
    x = -49
    py = px ** 2 + 2 * px + 3
    y = x ** 2 + 2 * x + 3

    for i in range(10000):
        px += 0.01
        x += 0.01
        py = 500 - (px ** 2 + 2 * px + 3)
        y = 500 - (x ** 2 + 2 * x + 3)
        pygame.draw.line(screen, (0,0,0), (px + 250,py), (x + 250,y), 5)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(color)
    makeGraph()
    pygame.display.update()
    fps.tick(20)
