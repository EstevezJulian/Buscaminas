import utils
import interfazJuego as IJ
import interfazDeInicio
import guardarEstadisticas as GE


interfazDeInicio.interfazIncio()

utils.buscardAdyacentes()
#cantidadBombas = input("Cuantas bombas quieres en esta partida?: ")
utils.plantarBombas()
#print(utils.cordenadasBombas)

GE.Inicio()
IJ.interfaz()
#while(True):
#    utils.mostrarTablero()
#    print("cordenadas en formato FilaxColumna")
#    accion = input("Ingrese accion: ")
#    utils.interpretarAccion(accion)
#    utils.evaluarVictoria()

