import gamelib
import tetrisC
import dibujar

ANCHO=tetrisC.ANCHO_JUEGO
ALTO=tetrisC.ALTO_JUEGO
TAMAÑO= dibujar.tamaño

def DrawGrill(ANCHO, TAMAÑO, ALTO):
    #draw line(x1,y1.x2.y2, fill"color")
    #(x,y)+tamaño
    #a modo cuadrados
#    cuadrado=TAMAÑO*TAMAÑO
    """
    for _ in range(0, ALTO*TAMAÑO, cuadrado):
        for j in range(_, ANCHO*TAMAÑO, cuadrado):
            gamelib.draw_rectangle( , fill="violet")
    """
    #format lines:    
    for i in range(ANCHO):
        gamelib.draw_line(i*TAMAÑO, 0, i*TAMAÑO, 360, fill="violet")
    for i in range(ALTO):
        gamelib.draw_line(0, i*TAMAÑO, 180, i*TAMAÑO,fill="violet")
