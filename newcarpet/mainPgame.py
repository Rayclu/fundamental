import pygame
import pygame.draw_py
from pygame.locals import *
import tetrisC
import dibujar
w, h = (360, 400)
size = w, h 

running = True

screen = pygame.display.set_mode((600, 600))
screen.fill("gray")
pygame.display.set_caption("Tetris")

pygame.display.update()

pygame.init()
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    pygame.draw.rect(
        screen,
        "black",
        (w/2, 0, )
    )

    

pygame.quit()