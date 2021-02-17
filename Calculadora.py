#se separan las funciones del core
#from calculadoraFuncionesv3 import *
#import funciones.calculadoraFuncionesv3
import CalculadoraFunciones
repetir = "si"
while repetir.lower() == "si":
    n1 = float(input("deme un numero\n"))
    n2 = float(input("deme otro numero\n"))
    operacion = str(input("que operacion desea hacer:\n1.Suma\n2.Resta\n3.Multipliacion\n4.Division\n"))
    if operacion.lower == "suma" or int(operacion) == 1:
        respuesta = funciones.CalculadoraFunciones.sumar(n1,n2)# no va a funcionar sino esta es una carpeta llamada funciones
    elif operacion.lower == "resta" or int(operacion) == 2:
        respuesta = CalculadoraFunciones.restar(n1, n2)
    elif operacion.lower == "multiplicacion" or int(operacion) == 3:
        respuesta = multiplicar(n1,n2)
    elif operacion.lower == "division" or int(operacion) == 4:
        respuesta = dividir(n1,n2)
    else:
        print("la opcion elegida no esta en la lista")
    print("la respuesta es {}".format(respuesta))
    repetir = str(input("desea hacer otra operacion\n"))