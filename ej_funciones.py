def ingresar_numeros():
    numeros = input("Ingrese numeros enteros separados por un espacio")
    lista_numeros = numeros.split(" ")

    for num in lista_numeros:
        print(num)

    validar_lista(lista_numeros)

def validar_lista(lista):
    for numero in lista:
        if numero.isdigit():
            print("Es numero",numero)
        else:
            print("No es numero",numero)

ingresar_numeros()