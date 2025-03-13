import random
import copy
import interfazJuego as IG
import guardarEstadisticas as GE

columnas = 10
filas = 9
bombas = 4
cordenadasBombas= []

#estado 0 = oculto, 1 = revelado, 2 = marcado
plantillaCelda= {'estado': 0, 'bomba': False, 'bombasAdyacentes':0, 'celdasAdyacentes':[]}

matriz = []

#revela un celda y, si es una bomba, termina el juego
def revelar(celda, boton):
    if celda['estado'] == 0:
        if celda['bomba']:
            print("CABOOOOM!!! Perdiste")
            GE.definirResultado("Derrota")
            return True
        IG.revelarBoton(boton, celda)
        celda['estado'] = 1
        if celda['bombasAdyacentes'] == 0:
            revelarAdyacentes(celda)
        GE.incrementarCasillasExacbadas()
    return False
def marcar(celda):
    celda['estado'] = 2
    if celda['bomba']:
        GE.incrementarBombasMarcadas()
    
def desmarcar(celda):
    if celda['estado'] == 2:
        celda['estado'] = 0

def ponerBomba(celda):
    celda['bomba'] = True
    avisarAdyacentes(celda)

#muestra el tablero en la consola    
def mostrarTablero():
    global matriz

    for fila in matriz:
        if matriz.index(fila) == 0:
            print("/", end = " ")
            for i in range(columnas):
                print(f"{i}", end = " ")
            print("")
        for celda in fila:
            if fila.index(celda) == 0:
                print(f"{matriz.index(fila)}", end= " ")
            if celda['estado'] == 0:
                print("x", end = " ")
            if celda['estado'] == 1:
                print(f"{celda['bombasAdyacentes']}" , end = " ")
            if celda['estado'] == 2:
                print("m", end = " ")
        print("")

#pensado para usar junto a "mostrar interfaz" para jugar en la consola sin interfaz grafica
def interpretarAccion (accion):
    global matriz
    partes = accion.split()
    print(partes)
    cordenadas = partes[1].split("x")
    x = int(cordenadas[0])
    y = int(cordenadas[1])
    #print(cordenadas)
    if partes[0] == "excabar":
        revelar(matriz[x][y])
    if partes[0] == "marcar":
        marcar(matriz[x][y])
    if partes[0] == "desmarcar":
        desmarcar(matriz[x][y])

#planta las bombas en celdas al azar    
def plantarBombas():
    global matriz
    bombasPlantadas = 0
    while bombasPlantadas < bombas:
        x = random.randint(0, filas-1)
        y = random.randint(0, columnas-1)
        if not matriz[x][y]['bomba']:
            ponerBomba(matriz[x][y])
            cordenadasBombas.append([x,y])
            #print(f"{x}, {y}")
            bombasPlantadas += 1


#busca y anota los adyacentes a cada celda
def buscardAdyacentes():
    global matriz
    matriz = [[copy.deepcopy(plantillaCelda) for _ in range(columnas)] for _ in range(filas)]
    
    for x in range(filas):
        for y in range(columnas):
            for adX, adY in [[x+1, y], [x, y+1], [x+1, y+1],[x-1, y], [x, y-1],  [x-1, y-1],[x+1, y-1],[x-1, y+1]]:
                #print(f"{adX, adY}")
                if adX>=0 and adY>=0 and adX<filas and adY<columnas:
                    
                    matriz[x][y]['celdasAdyacentes'].append([adX, adY])
                    
                    
                    #matriz[x][y]['celdasAdyacentes'].append([adX, adY])
            #print(f"Celda {x}x{y}, adyacentes: {matriz[x][y]['celdasAdyacentes']}")

def avisarAdyacentes(celda):
    global matriz
    for x,y in celda['celdasAdyacentes']:
        matriz[x][y]['bombasAdyacentes'] += 1
        
def revelarAdyacentes(celda):
    global matriz
    for x, y in celda['celdasAdyacentes']:
        revelar(matriz[x][y], IG.matrizBotones[x][y])

#evalua si cumple condicon de vitorio y, en caso de hacerlo, da por terminado el juego
def evaluarVictoria():
    global cordenadasBombas
    global matriz
    for x, y in cordenadasBombas:
        if matriz[x][y]['estado'] !=2 and matriz[x][y]['bomba']:
            return False
    print("Felicidades encontraste todas las bombas!")
    GE.definirResultado("Victoria")
    return True
    
def establecerDimensiones(cantColumnas, cantFilas, cantBombas):
    global columnas
    global filas
    global bombas
    columnas = cantColumnas
    filas = cantFilas
    bombas = cantBombas
    