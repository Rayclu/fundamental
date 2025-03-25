import sqlite3 as sq
import gamelib as gb
def ChargePiece():

    archivo = open("piezas.txt", 'r')
    piezas = []

    for linea in archivo:
        
        linea = linea.rstrip().split()
        for _ in range(2):
            linea.pop()

        for i in range(len(linea)):
            linea[i] = linea[i].split(';')
            
            for j in range(len(linea[i])):
                linea[i][j] = linea[i][j].split(',')
                linea[i][j] = (int(linea[i][j][0]), int(linea[i][j][1]))    
            
            linea[i].sort()
        #print("La linea que se agregará es:",linea)       
        piezas.append(linea)
    archivo.close()
    #print(f"---------------------------------------\n {piezas[0][0][0]}\n--------------------------------")
    return piezas
print(ChargePiece())
def ChargeScore() -> list:
    
    #Argumento=>Null
    #----------------
    #cargar data del archivo csv.
    #-----------------------------------
    #lista de tuplas [(name, score), ...]
    #
    
    conn = sq.connect("Scores.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS points (nickname,rank)")
    cur.execute("SELECT * FROM points ORDER BY rank DESC")
    ranking = cur.fetchall()
    conn.commit()
    conn.close()
   
    return ranking
    
    """ file = open("points.csv", "r")

    ranking=[]
    for line in file:
        ClearLine=line.rstrip(f"\n").split("|")
        ClearLine[1]=int(ClearLine[1])
        ranking.append(tuple(ClearLine))

    file.close()

    ranking = _order(ranking)

    file = open("points.csv", 'w')
    for user in ranking:
            file.write(f"{user[0]}|{user[1]} \n")
    file.close()

    return ranking"""



        

def saveScore(ranking:list,pts : int):
    #For example, the scores value and names are printed#
    #A modo de ejemplo, se indican los valores de score y name.
    #ranking = [(str(player1), int(1000)),(str(player2, int(1))),(...)]
            # player => Iterable for the var ranking
            #player (String(playerX), Integer(Rank))
            # 
            # New_Ranked_Player => Is a substitute from player if his score <= rank #
 #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """if len(ranking)==0:
        nickname = gb.input("Add your name, congratulations, you are in the top ten🥳:")
        player=(f"{nickname}", pts)
        ranking.append(player)
        
        with open("points.csv", 'w') as file:

                file.write(f"{nickname}|{pts} \n")
        return"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """rankeos=[ranking[i][1] for i in range(len(ranking))]
    
    if pts > min(rankeos) or len(ranking)<=12:
        if len(ranking)==12:
            ranking.pop()
        nickname = gb.input("agree your name, congratulations, you are into the top ten🥳:")
        player=(f"{nickname}", pts)
        ranking.append(player)
        ranking=_order(ranking)

        with open("points.csv", 'w') as file:
            for usrs in ranking:
                file.write(f"{usrs[0]}|{usrs[1]} \n")
    else:
        return gb.draw_text("You are a noob, nigger 🫵🏼!", 50, 50, fill="Cyan", anchor='nw')"""
    """
    players=[]
    for player in range(len(ranking)):
            if ranking[player][1] <= rank or len(ranking)<12:
                nickname=gb.draw_text(gb.input("agree your name, congratulations, you are into the top ten🥳:"), 50, 50, fill="blue", anchor = 'nw' )
                player = (f"{nickname}|{rank}\n")
                players.append(player)
        
    for _ in players:
        with open("points.csv", 'a') as file:
            file.write(_)
        file.close()
    """
    

    nickname = gb.input("add your name, congratulations, you are into the top ten🥳:")
    player=(str(nickname), int(pts))
        

    database = sq.connect("Scores.db")
    cur = database.cursor()
    cur.execute("SELECT nickname,rank FROM points ORDER BY rank DESC LIMIT 10")
    ranking = cur.fetchall()
    
    ranking_cleaned = []

    for rnk in range(10):
        ranking_cleaned.append(ranking[rnk][1])
    print(ranking_cleaned, ranking)
    
    cur.execute("CREATE TABLE IF NOT EXISTS points(nickname, rank)")
    #----------------------------------------
    #----------------------------------------
    if len(ranking_cleaned) < 11 or pts >min(ranking_cleaned):
        cur.execute(f"INSERT INTO points(nickname, rank) VALUES (?, ?)", (player[0], player[1]))
        database.commit()
        database.close()
        ranking.append(player)
        ranking=_order(ranking)
        return
    else:
        database.commit()
        database.close()
        
        return gb.draw_text("You are a noob, nigger 🫵🏼!", 50, 50, fill="Cyan", anchor='nw')
    
    

    

def _order(ranking: list):

    if len(ranking)<2:
        return ranking
    
    pivote = ranking.pop()

    menor=[]
    mayor=[]

    for play in ranking:
        if pivote == play:
            continue
        if play[1]<pivote[1]:
            menor.append(play)
        else:
            mayor.append(play)
    menor=_order(menor)
    mayor=_order(mayor)

    return mayor+[pivote]+menor
    
