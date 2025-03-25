#Libraries:
from random import randint
from random import randrange
import persistencia
import gamelib
import inspect
#----------------------------------------------------------------------
#Constants:
ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
CUBO = 0

PDict={
    0:0,
    1:100,
    2:200,
    3:400,
    4:1000
}

Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6

PIEZAS = persistencia.ChargePiece()
#-------------------------------------------------------------------------------------------------------
def generar_pieza(pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que 
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """
    if pieza == None:
        ubi_pieza=randrange(0,len(PIEZAS))
        pieza_selected=randrange(0, len(PIEZAS[ubi_pieza]))
        pieza = PIEZAS[ubi_pieza][pieza_selected]    
     #   return pieza
    #return pieza
        return mover_a_grilla(pieza)
    return mover_a_grilla(pieza)
    
def mover_a_grilla(pieza):   
        """
        #
        # Bloque de codigo utilizado para debug al encontrar errores con las piezas en general.#
        stack = inspect.stack()
        funcion_llamadora = stack[1].function
        if funcion_llamadora == "_search_piece":
            print("Esta pieza llegó desde buscar: \n\t", pieza)"""
        
        _y = 0
        for i in range(len(pieza)):
            if pieza[i][1] < _y:
                _y = pieza[i][1]
        nueva_pieza=[]
        for i in range(len(pieza)):
            new_coord=(pieza[i][0],pieza[i][1]-_y)
            nueva_pieza.append(new_coord)
        return nueva_pieza
def trasladar_pieza(pieza, dx, dy):
    """
    Traslada la pieza de su posición actual a (posicion + (dx, dy)).

    La pieza está representada como una tupla de posiciones ocupadas,
    donde cada posición ocupada es una tupla (x, y). 
    Por ejemplo para la pieza ( (0, 0), (0, 1), (0, 2), (0, 3) ) y
    el desplazamiento dx=2, dy=3 se devolverá la pieza 
    ( (2, 3), (2, 4), (2, 5), (2, 6) ).
    """
    pieza_trasladada=[]
    
    for pos in pieza:
            traslado = (int(pos[0]) + dx, int(pos[1]) + dy)
            pieza_trasladada.append(traslado)
    pieza=pieza_trasladada
    return pieza
   
def crear_juego(pieza_inicial):
    """
    Crea un nuevo juego de Tetris.

    El parámetro pieza_inicial es una pieza obtenida mediante 
    generar_pieza(). Ver documentación de esa función para más información.

    El juego creado debe cumplir con lo siguiente:
    - La grilla está vacía: hay_superficie da False para todas las ubicaciones
    - La pieza actual está arriba de todo, en el centro de la pantalla.
    - El juego no está terminado: terminado(juego) da False

    Que la pieza actual esté arriba de todo significa que la coordenada Y de 
    sus posiciones superiores es 0 (cero).
    """
    puntos=int(0)
    pieza_inicial = trasladar_pieza(pieza_inicial, ANCHO_JUEGO // 2, 0) 
    grilla = []
    for _ in range(ALTO_JUEGO):
        fila=[]
    
        for _ in range(ANCHO_JUEGO):
            fila.append(0)  
    
        grilla.append(fila)

    return grilla, pieza_inicial, puntos
def dimensiones(juego):
    grilla = juego[0]

    return len(grilla[0]), len(grilla)


def pieza_actual(juego):
    """
    Devuelve una tupla de tuplas (x, y) con todas las posiciones de la
    grilla ocupadas por la pieza actual.

    Se entiende por pieza actual a la pieza que está cayendo y todavía no
    fue consolidada con la superficie.

    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """ 
    "return juego[1]"
    pieza_actual = juego[1]

    return pieza_actual


def hay_superficie(juego:tuple, x:int, y:int)->bool:
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.
    
    La coordenada (0, 0) se refiere a la posición que está en la esquina 
    superior izquierda de la grilla.
    """
    if juego[1]==[(0,0),(1,0),(1,1),(1,2)]:
        juego[1]=trasladar_pieza(juego[1], 0, 1)
    grilla = juego[0]
    try:
        if grilla[y][x]!=0:
            return True
        elif grilla[y][x]==1:
            return False     
    except IndexError:
        return False

    
def mover(juego, direccion)->tuple:
    
    """
    Mueve la pieza actual hacia la derecha o izquierda, si es posible.
    Devuelve un nuevo estado de juego con la pieza movida o el mismo estado 
    recibido si el movimiento no se puede realizar.

    El parámetro direccion debe ser una de las constantes DERECHA o IZQUIERDA.
   """

    pieza_aux = pieza_actual(juego)
    pieza_aux = trasladar_pieza(pieza_aux, direccion, 0)
    for i in range(0, len(pieza_aux)):
        
        if  not(-1 < pieza_aux[i][0] < ANCHO_JUEGO) or hay_superficie(juego, pieza_aux[i][0], pieza_aux[i][1]):
            return juego 
    
    return juego[0], pieza_aux, juego[2]

def consolidar_pieza(juego:tuple)->tuple:
    grilla=juego[0]
    for i in range(len(pieza_actual(juego))):
        coor=pieza_actual(juego)[i]
        grilla[coor[1]][coor[0]] = 1
    
    return grilla, pieza_actual(juego), juego[2]
    
def eliminar_fila(juego:tuple)->tuple:
   
    grilla = juego[0]
    puntos = juego[2]
    contador = 0

    for i in range(len(grilla)):

        if grilla[i].count(1) == ANCHO_JUEGO:
            
            grilla.pop(i)
            grilla.insert(0, [0 for _ in range(ANCHO_JUEGO)])
            contador+=1

    puntos += PDict.get(contador)

    return grilla, pieza_actual(juego), puntos

def cambiar_pieza_actual(juego:tuple, pieza:list)->tuple:
    return juego[0], trasladar_pieza(pieza, ANCHO_JUEGO//2, 0), juego[2]

def avanzar(juego:tuple, siguiente_pieza:list)->tuple:
    """
    Avanza al siguiente estado de juego a partir del estado actual.
    
    Devuelve una tupla (juego_nuevo, cambiar_pieza) donde el primer valor
    es el nuevo estado del juego y el segundo valor es un booleano que indica
    si se debe cambiar la siguiente_pieza (es decir, se consolidó la pieza
    actual con la superficie).
    
    Avanzar el estado del juego significa:
     - Descender una posición la pieza actual.
     - Si al descender la pieza no colisiona con la superficie, simplemente
       devolver el nuevo juego con la pieza en la nueva ubicación.
     - En caso contrario, se debe
       - Consolidar la pieza actual con la superficie.
       - Eliminar las líneas que se hayan completado.
       - Cambiar la pieza actual por siguiente_pieza.

    Si se debe agregar una nueva pieza, se utilizará la pieza indicada en
    el parámetro siguiente_pieza. El valor del parámetro es una pieza obtenida 
    llamando a generar_pieza().

    **NOTA:** Hay una simplificación respecto del Tetris real a tener en
    consideración en esta función: la próxima pieza a agregar debe entrar 
    completamente en la grilla para poder seguir jugando, si al intentar 
    incorporar la nueva pieza arriba de todo en el medio de la grilla se
    pisara la superficie, se considerará que el juego está terminado.

    Si el juego está terminado (no se pueden agregar más piezas), la funcion no hace nada, 
    se debe devolver el mismo juego que se recibió.
    """
    if terminado(juego):
        return juego, False
    
    #desciende la pieza actual en una posicion
    pieza=trasladar_pieza(pieza_actual(juego), 0, 1)
    
    for i in range(len(pieza)):

        coor=pieza[i]

        if coor[1]>= ALTO_JUEGO or hay_superficie(juego, coor[0], coor[1]):
            #- Consolidar la pieza actual con la superficie.
            juego = consolidar_pieza(juego)
            #- Eliminar las líneas que se hayan completado.
            juego=eliminar_fila(juego)
            #- Cambiar la pieza actual por siguiente_pieza.
            juego=cambiar_pieza_actual(juego, siguiente_pieza)

            return juego, True
    
    juego = juego[0], pieza, juego[2]+10
    return juego, False
 
def terminado(juego:tuple)->bool:

    """
    Devuelve True si el juego terminó, es decir no se pueden agregar
    nuevas piezas, o False si se puede seguir jugando.
    """
  
    for coords in juego[0][0]:
        if coords != 0:
            return True
    return False

def RotPiece(juego: tuple) -> list:

    """
    Recibe por parametro la pieza actual, a cada elemento de la tupla que conforma la pieza le resta el primer elemento
    para trasladar la pieza a la ubicación 0,0.
    Luego intercambia la pieza actual por una de sus rotaciones.
    Y finalmente recoloca a la pieza en las coordenadas originales.
    """
    pieza = list(juego[1])
    coord_aux = pieza[0]
    
    new_ubication=[]
    for pos in pieza:
        pos=(pos[0]-coord_aux[0], pos[1]-coord_aux[1])
        new_ubication.append(pos)
    #-----------------------------------------------------------------
    
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


    def _search_piece(pieza):
        """
        Recibe por parametro la pieza actual, e itera sobre todas las piezas de la constante piezas buscando la coincidente a la que se ha recibido, una vez encontrada intercambia la rotación por si siguente.
        En el caso de que la rotación recibida sea la que se encuentra en el ultimo elemento retornará la primer rotación de la pieza.
        """
        #
        #(pieza=>[(x,y)(x,y)...])<-Una sola pieza(parametro)
        # (PIEZAS=>[[pieza1(rot1,),(rot2)..], pieza2,........])<-Todas las piezas #       
        for i in range(0, len(PIEZAS)):
            for j in range(len(PIEZAS[i])):
                if pieza == PIEZAS[i][j]:
                    try:        
                        return PIEZAS[i][j+1][:]    
                    except IndexError:
                        return PIEZAS[i][0][:]
                    
        return pieza 
        """p_original = pieza
        for posible_pieza in range(len(PIEZAS)):
            for rotaciones in range(len(PIEZAS[posible_pieza])):

                if p_original == PIEZAS[posible_pieza][rotaciones]:
        """     #       return posible_pieza, rotaciones
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        """pieza_encontrada = []
        for posible_pieza in PIEZAS:
        
            for posible_rotacion in range(len(posible_pieza)):
                if p_original == posible_pieza[posible_rotacion]:
                    #print("Se ha encontrado la pieza")
                    try:
                        pieza_encontrada=posible_pieza[posible_rotacion+1][:]
                        return pieza_encontrada
                    except IndexError:
                        return posible_pieza[0]
        return pieza
        """

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #index = _search_piece(new_ubication)
    #rotacion=mover_a_grilla(PIEZAS[index[0]][index[1]][:])
    #----------------------------------------------------------------
    #example: rotacion=[(0, 0), (1, 0), (1, 1), (2, 1)]<-pieza 
    rotacion=_search_piece(new_ubication)

    _rotation=[]

    for pos in rotacion:
        pos=(pos[0]+coord_aux[0], pos[1]+coord_aux[1])#pos[0]==eje x | pos[1]==eje y
        _rotation.append(pos)


    def __verif(pieza: list) -> bool: 
        """
        Recibe por parametro la pieza ya rotada para verificar si la rotación se puede consolidar en
        su posición actual, funciona como un semaforo para las rotaciones.
        Si devuelve False fuerza a las otras funciones a devolver la pieza antes de ser alterada.
        Caso contrario la función permite la alteración.
"""
    
        for coord in pieza:
            if int(coord[0]) < 0 or int(coord[0]) >= ANCHO_JUEGO:
                return False 
            elif int(coord[1])< 0 or int(coord[1])>=ALTO_JUEGO:
                return False       

        return True    










    if __verif(mover_a_grilla(_rotation)):
        
        return  _rotation

    else:
       return pieza
    