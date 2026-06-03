
while True:
    try:
        cantidad_participantes = int(input("Ingrese la cantidad de participantes: "))
        if cantidad_participantes <= 0:
            print("¡Cantidad invalida! debe ingresar un numero entero positivo")
        else:
            print("Se han agredado",cantidad_participantes, "participantes.")
            break
    except:
        print("¡cantidad invalida! Debe ingresar un numero entero positivo.")


for i in range(cantidad_participantes):
    print("Ingresando el participante", (i+1))
    while True:
        alias = input("Ingrese su alias (min. 5 caracteres, sin espacios): ").strip()

        if (len(alias) < 5) or (" " in alias):
            print("El alias debe de tener al menos 5 caracteres y no tener espacios en blanco")
        else:
            break
        