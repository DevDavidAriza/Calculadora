from tkinter import  Tk, Entry, Grid, mainloop, Button, Label
from tkinter.ttk import Combobox  # para agregar los de combobox

def click():
    #se deben poner aca dentro de la funcion para que no den error de conversion entre flat y text
    v1 = n1.get()
    v2 = n2.get()
    if operaciones.get() == "+":
        result.config(text=float(v1)+float(v2))
    if operaciones.get() == "-":
        result.config(text=float(v1)-float(v2))
    if operaciones.get() == "x":
        result.config(text=float(v1)*float(v2))
    if operaciones.get() == u"\u00F7":
        result.config(text=float(v1)/float(v2))
    if operaciones.get() == "%":
        result.config(text=float(v1)%float(v2))

window = Tk()
# titulo de la ventana
window.title("calculadora v4")

#titulo del frame
label = Label(window, text="Esta es mi primera Calculadora")
label.grid(columnspan=2, row=0)

# entrada de numeros
n1 = Entry(window, width=30)
n2 = Entry(window, width=20)
#ubicacion de numeros
n1.grid(column=1, row=1)
n2.grid(column=1, row=2)

#eleccion de operacion
operaciones = Combobox(window, width=5)
operaciones["values"] = ("+", "-", "x",u"\u00F7","%")
operaciones.current(0)
#ubicacion de operaciones
operaciones.grid(column=0, row=2)

#resultados
result = Label(window)
result.grid(column=1, row=3)

boton = Button(window, text="Resultado", command=click)
boton.grid(column=0, row=3)

#ciclo de la ventana
window.mainloop()