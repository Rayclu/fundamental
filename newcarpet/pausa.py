import pygame
import gamelib
import tetrisC
import newcarpet.representacion as representacion
import persistencia



def DetectCom():
    pass

def DetecTec():
    pass

def pause():
    
    """    paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False
        pygame.display.flip()
    """
    paused=True
    while paused:
        for event in gamelib.get_events:
            if event.type == gamelib.EventType.KeyPress and event.key=='q':
                 return
            if event.type==gamelib.EventType.KeyPress and event.key=='p':
                paused=True
            
def exit(running):
    pass
    """
    if pause(paused) == true:
        for envent.type in pygame.event.get():
            if event.type==pygame.keydown and event.key == pygame.k_esc:
                running=false
                return running
    """

def reset():
    pass
    """
    
    if pause(paused) == true:
        for envent.type in pygame.event.get():
            if event.type==pygame.keydown and event.key == pygame.k_r:
                
                
    """
    


def main():
    pass