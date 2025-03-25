import gamelib
def main():
    end =False
    while gamelib.loop(fps=30) and end==False:
        if event.type == gamelib.EventType.KeyPress and event.key=='q':
                 return end==True    
        
gamelib.init(main)
      