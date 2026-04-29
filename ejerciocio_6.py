numero_1 = int(input("ingrese un numero:"))
operacion = input("Ingresa la operacion matematica (+,-,*,/):")
numero_2 = int(input("ingrese su segundo numero que sea distinto de 0:"))

if operacion == "+":
    suma = numero_1+numero_2
    print("la suma es:",suma)
elif operacion == "-":
    resta = numero_1-numero_2
    print("la resta es:",resta)
elif operacion == "*":
    multiplicacion = numero_1*numero_2
    print("la multiplicacion es:",multiplicacion)
elif operacion == "/":
    division = numero_1/numero_2
    print("la division es:",division)
else:
    print("la operacion no coincide")