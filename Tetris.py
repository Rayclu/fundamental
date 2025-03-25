import gamelib 
import tetrisC 
import dibujar
import persistencia
import time


#init gamelib window and waiting time:
espera = 8
screen=gamelib.resize(450, 500)
#----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------#
def pause(juego : list , end : bool):
    input=gamelib.input("\tPress 'q' to finish this play\n, 'r' to reset or 'p' to go back the game")
    if input=='r':
               return main(), end
    elif input=='q':
               end = True
               return juego, end
    else:
               time.sleep(1)
               return juego, end
    
#----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------#
def menu():
    input = gamelib.input("Press 'q' to quit the game or 'p' to play")
    game = tetrisC.crear_juego(pieza_inicial=tetrisC.generar_pieza())
    if input=='q':
                end = True
                return game, end
    elif input!='q':
                end = False
                return game, end

#----------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------#
def main(end=None): 
    #------------------------------------------
    # Finish function.#
    def finished():      
            input = gamelib.input("Do you want to play again?")
            if input=='no':
                return main(end=True)
            elif input!='q':
                  return main(end=False)    
    #----------------------------------------------------------------
    if end is None:
        juego, end = menu()     #Game state and flag
    else:
        juego = tetrisC.crear_juego(pieza_inicial=tetrisC.generar_pieza())
    
    pts=juego[2]
    #---------------------------------------------------------------------------------------------
    # Inicializar el estado del juego
    # Init game state:#
    
    pieza_sig = tetrisC.generar_pieza()
    cambiar_pieza = False 
    timer = 0    
    #--------------------------------------------------
    
    ranking = persistencia.ChargeScore()
   
    #-----------------------------------------------------------------------------------
#Union de las funciones del juego:    
    #Add Tetris soundtrack
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("Tetris_sound.mp3")
    pygame.mixer.music.play(loops=100000)
    import random
    while gamelib.loop(200) and end!=True:
        # Dibujar la pantalla con el estado del juego
        gamelib.draw_begin()
        #Draw backgrond:
        gamelib.draw_image("background_resized.gif",-40,-70)
        #---------------------------------------------------------
        # Draw game state:#
        dibujar.drawPTS(juego)
        dibujar.DrawGrill(juego)
        dibujar.pieza(tetrisC.pieza_actual(juego))
        dibujar.prx_pieza(pieza_sig)
        #---------------------------------------------------------------
        # Draw indicaton controls:#
        gamelib.draw_text("Press:\n \t-'a' to turn left.\n\t-'d' to right\n\t-'s' to down piece", 10, 400, fill="Black", anchor='nw')
        gamelib.draw_end()
    
        #Pausar:
        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress and event.key == 'p':
                juego, end = pause(juego, end)
                if end==True:
                    return
        # Actualizar el estado del juego segun corresponda:

        #Izquierda:

            if event.type == gamelib.EventType.KeyPress and event.key=='q':
                return end==True
            
            if event.type == gamelib.EventType.KeyPress and event.key == 'a':
                juego = tetrisC.mover(juego, tetrisC.IZQUIERDA)
        #Derecha:
            if event.type == gamelib.EventType.KeyPress and event.key == 'd':
                juego = tetrisC.mover(juego, tetrisC.DERECHA)
        #Empujar pieza hacia abajo:
            if event.type == gamelib.EventType.KeyPress and event.key == 's':
                juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
                if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()
        #Rotación:
            if event.type == gamelib.EventType.KeyPress and event.key == 'w':
                
                juego = (juego[0], tetrisC.RotPiece(juego), juego[2])
                print("se ha intentado rotar la pieza con exito")
        # Descenso de la pieza automatica
        timer += 1
        if timer == espera:
            juego, cambiar_pieza = tetrisC.avanzar(juego, pieza_sig)
            
            if cambiar_pieza:
                pts=juego[2]
            timer = 0
            

        if cambiar_pieza:
                    pieza_sig = tetrisC.generar_pieza()


        if tetrisC.terminado(juego):
        
            gamelib.draw_text(f"The final points are: {pts}", 10, 10, fill="Cyan", anchor='nw') 
            persistencia.saveScore(ranking, pts)
        
            return finished()
                  

gamelib.init(main)
