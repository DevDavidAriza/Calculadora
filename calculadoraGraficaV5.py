# se cambia la lista desplegable por botones de radio
from tkinter import  Tk, Entry, Grid, mainloop, Button, Label, IntVar
from tkinter2.ttk import Radiobutton  # para agregar los de combobox

def click():
    v1 = n1.get()
    v2 = n2.get()
    if seleccion.get() == 1:
        result.config(text=float(v1)+float(v2))
    if seleccion.get() == 2:
        result.config(text=float(v1)-float(v2))
    if seleccion.get() == 3:
        result.config(text=float(v1)*float(v2))
    if seleccion.get() == 4:
        result.config(text=float(v1)/float(v2))

window = Tk()
# titulo de la ventana
window.title("calculadora v4")

#titulo del frame
label = Label(window, text="Calculadora v4")
label.grid(columnspan=2, row=0)

# entrada de numeros
n1 = Entry(window, width=10)
n2 = Entry(window, width=10)
#ubicacion de numeros
n1.grid(column=1, row=1)
n2.grid(column=1, row=2)

#eleccion de operacion
#"operaciones = Combobox(window, width=5)
#"operaciones["values"] = ("+", "-", "x",u"\u00F7")
#"operaciones.current(0)
#"#ubicacion de operaciones
#operaciones.grid(column=0, row=2)

#eleccion de operaciones
seleccion = IntVar()
seleccion.set(1)
radio1 = Radiobutton(window,text="+", variable=seleccion, value=1)
radio1.grid(column=3, row=0)
radio2=Radiobutton(window,text="-", variable=seleccion, value=2)
radio2.grid(column=3, row=1)
radio3=Radiobutton(window,text="x", variable=seleccion, value=3)
radio3.grid(column=3, row=2)
radio4=Radiobutton(window,text=u"\u00F7", variable=seleccion, value=4)
radio4.grid(column=3, row=3)

#resultados
result = Label(window)
result.grid(column=1, row=3)

boton = Button(window, text="Resultado", command=click)
boton.grid(column=0, row=3)

#ciclo de la ventana
window.mainloop()
