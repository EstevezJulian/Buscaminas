import tkinter as tk
import guardarEstadisticas as GE
import utils


matrizBotones = []
ventanaDeJuego = None

def click_izquierdo(boton, cordX, cordY):
    celda = utils.matriz[cordX][cordY]
    if celda['estado'] == 0:
        if utils.revelar(celda, boton):
            finalizar()
        print(f"Boton ({cordX},{cordY}) presionado")
        #revelarBoton(boton, celda)
        if utils.evaluarVictoria():
            finalizar()

def revelarBoton(boton, celda):
    color = "black"
    if celda['bombasAdyacentes'] == 1:
        color = "blue"
    elif celda['bombasAdyacentes'] == 2:
        color = "green"
    elif celda['bombasAdyacentes'] == 3:
        color == "red"
    elif celda['bombasAdyacentes'] == 4:
        color == "pink"
    elif celda['bombasAdyacentes'] == 5:
        color == "purple"
    elif celda['bombasAdyacentes'] == 6:
        color == "brown"
    boton.config(text=f"{celda['bombasAdyacentes']}", fg=color)
    

def click_derecho(boton, cordX, cordY):
    celda = utils.matriz[cordX][cordY]
    if celda['estado'] ==0:
        utils.marcar(celda)
        print(f"Boton ({cordX},{cordY}) presionado")
        boton.config(text="M", fg="blue")
        if utils.evaluarVictoria():
            finalizar()
    elif celda['estado'] == 2:
        utils.desmarcar(celda)
        print(f"Boton ({cordX},{cordY}) presionado")
        boton.config(text=" ", fg="blue")

def interfaz():
    root = tk.Tk()
    root.geometry(f"{60+30*utils.filas}x{60+30*utils.columnas}")
    root.title("Buscaminas")
    global ventanaDeJuego
    ventanaDeJuego = root
    global matrizBotones
    matrizBotones =[[None for _ in range(utils.columnas)] for _ in range(utils.filas)]
   

    for i in range(utils.filas):
        for j in range(utils.columnas):
            boton = tk.Button(root,text=" ")
            matrizBotones[i][j]=boton
            boton.bind("<Button-1>", lambda event,b=boton, x=i, y=j:  click_izquierdo(b, x, y))
            boton.bind("<Button-3>", lambda event,b=boton, x=i, y=j: click_derecho(b, x, y))
            #boton.config(command=lambda b=boton, x=i, y=j: click_izquierdo(b,x,y))
            boton.place(x=30*i+30, y=30*j+30, width=30, height=30)

    root.mainloop()

def finalizar():
    GE.Final()
    def cerrar_juego():
        exit()
    global ventana_final
    ventana_final = tk.Toplevel(ventanaDeJuego)  # Crear ventana secundaria
    ventana_final.title("Buscaminas")
    ventana_final.geometry("100x100")
    ventana_final.transient(ventanaDeJuego)  # Hace que la ventana principal quede detrás
    ventana_final.grab_set()  # Bloquea la interacción con la ventana principal
    etiqueta = tk.Label(ventana_final, text=f"{GE.resultado}")
    etiqueta.place( x = 10, y = 10)
    boton = tk.Button(ventana_final, text="Cerrar", command=cerrar_juego)
    boton.place(x=10, y= 50)