from datetime import datetime
import csv

fecha=None
horaDeIncio=None
horaDeFinal=None
dimensiones = None
cantidadBombas = None
bombasMarcadas = 0
casillasExcabadas = 0
resultado = None

def Inicio():
    global fecha
    global horaDeIncio
    fecha = datetime.today().date()
    horaDeIncio = datetime.now().strftime("%H:%M:%S")

def juego(columnas, filas, bombas):
    global dimensiones
    global cantidadBombas
    dimensiones = f"{columnas}x{filas}"
    cantidadBombas = bombas
    

def Final():
    global horaDeFinal
    horaDeFinal = datetime.now().strftime("%H:%M:%S")
    nuevos_datos = [fecha, horaDeIncio, horaDeFinal, resultado, dimensiones, cantidadBombas, bombasMarcadas, casillasExcabadas]
    with open("estadisticas.csv",mode ="a", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(nuevos_datos)

def incrementarBombasMarcadas():
    global bombasMarcadas
    bombasMarcadas += 1

def incrementarCasillasExacbadas():
    global casillasExcabadas
    casillasExcabadas +=1
    
def definirResultado(resultadoDelJuego):
    global resultado
    resultado = resultadoDelJuego