import gamelib
import pygame
import tetrisC
#form: 50+x*10; 1+y*10....
pygame.init()
screen = pygame.display.set_mode((1280, 720))

eje_x , eje_y = list(pygame.display.get_window_size())

origen_x, origen_y=eje_x/3, eje_y

origen=(origen_x, origen_y)

tamaño=30

screen_sizes=list(pygame.display.get_window_size())

div=screen_sizes[0]/3
def paint_piece(pieza):
    pass
    for x,y in pieza:
        pygame.draw.rect(screen, "red", (screen_sizes[0]/3, screen_sizes[1],(origen, origen_x+x*tamaño, origen_y+y*tamaño,origen_x+x*tamaño+tamaño, origen_y+y*tamaño+tamaño))) 
        #(origen, origen_x+x*tamaño, origen_y+y*tamaño,origen_x+x*tamaño+tamaño, origen_y+y*tamaño+tamaño))
        #pygame.draw.rect(screen, "red", (origen_x+x*tamaño, origen_y+y*tamaño))   

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                return running
        
        screen.fill("black")

        pieza_cubo=tetrisC.generar_pieza(tetrisC.CUBO)

        
        paint_piece(pieza_cubo, screen)

        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
"""def PaintPiece():
    pass

def PaintTable():
    

def PaintPTS():
    pass

def PaintPiece():
    pass

def main():
    pass
"""
