#se divide en funciones para mejorar la carga del programa

def sumar(x,y):
    respuesta = x + y
    return respuesta

def restar(x,y):
    respuesta = x - y
    return respuesta

def multiplicar(x,y):
    respuesta = x * y
    return respuesta

def dividir(x,y):
    respuesta = x / y
    return respuesta


repetir = "si"
while repetir.lower() == "si":
    n1 = float(input("deme un numero\n"))
    n2 = float(input("deme otro numero\n"))
    operacion = str(input("que operacion desea hacer:\n1.Suma\n2.Resta\n3.Multipliacion\n4.Division\n"))
    respuesta = 0
    if operacion.lower() == "suma" or int(operacion) == 1:
        respuesta = sumar(n1,n2)
    elif operacion.lower() == "resta" or int(operacion) == 2:
        respuesta = restar(n1, n2)
    elif operacion.lower() == "multiplicacion" or int(operacion) == 3:
        respuesta = multiplicar(n1,n2)
    elif operacion.lower() == "division" or int(operacion) == 4:
        respuesta = dividir(n1,n2)
    else:
        print("la opcion elegida no esta en la lista")
    print("la respuesta es {}".format(respuesta))
    repetir = str(input("desea hacer otra operacion\n"))