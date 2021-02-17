n1 = float(input("deme un numero\n"))
n2 = float(input("deme otro numero\n"))
respuesta =0
operacion = str(input("que operacion desea hacer:\n1.Suma\n2.Resta\n3.Multipliacion\n4.Division\n"))
if operacion.lower() == "suma" or int(operacion) == 1:
    respuesta = n1 + n2
elif operacion.lower() == "resta" or int(operacion) == 2:
    respuesta = n1 - n2
elif operacion.lower() == "multiplicacion" or int(operacion) == 3:
    respuesta = n1 * n2
elif operacion.lower() == "division" or int(operacion) == 4:
    respuesta = n1 / n2
else:
    print("la opcion elegida no esta en la lista")

print(f"la respuesta es {respuesta}")