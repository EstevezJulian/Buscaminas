import tkinter as tk
import utils
import guardarEstadisticas as GE

    
def interfazIncio():
    def confirmarIngreso():
        cantColumnas = int(entradaColumnas.get())  # Obtener el texto del Entry
        cantFilas = int(entradaFilas.get())
        cantBombas = int(entradaBombas.get())
        utils.establecerDimensiones(cantColumnas, cantFilas, cantBombas)
        GE.juego(cantColumnas, cantFilas, cantBombas)
        root.destroy()
    
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Buscaminas")

    # Crear una etiqueta
    etiquetaColumnas = tk.Label(root, text="Cantida de Columnas")
    etiquetaColumnas.place(x=30, y= 30)

    etiquetaFilas = tk.Label(root, text="Cantida de Filas")
    etiquetaFilas.place(x=30, y= 60)
    
    etiquetaBombas = tk.Label(root, text="Cantida de Bombas")
    etiquetaBombas.place(x=30, y= 90)

    # Crear un campo de entrada
    entradaColumnas = tk.Entry(root)
    entradaColumnas.place(x=150, y= 30, width=30, height=20)

    entradaFilas = tk.Entry(root)
    entradaFilas.place(x=150, y= 60, width=30, height=20)
    
    entradaBombas = tk.Entry(root)
    entradaBombas.place(x=150, y= 90, width=30, height=20)


    # Crear un botón para capturar el texto
    boton = tk.Button(root, text="Aceptar", command=confirmarIngreso)
    boton.place(width=60, height=30, x= 170, y =120)


    root.mainloop()