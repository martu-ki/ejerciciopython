
vb_cafe = 3500
vb_te = 2500
vb_sandwich = 4800

while True:
    print("Menú")
    print("1) Comprar Café")
    print("2) Comprar Te")
    print("3) Comprar Sandwich")
    print("4) Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        while True:
            es_estudiante = input("Es estudiante? (S/N)").upper()
            if es_estudiante == "S" or es_estudiante == "N":
                break
            else:
                print("El valor debe ser S o N.")
       
        print("Producto: Café")
        print(f"Valor base: ${vb_cafe}")
        if es_estudiante == "S":
            descuento =vb_cafe*0.2
        else:
            descuento = 0
        print(f"Descuento a pagar: ${descuento}")
        total = vb_cafe-descuento
        print(F"Total a pagar: ${total}")

    elif opcion == 2:
        es_estudiante = input("Es estudiante? (S/N)")
        print("Producto: Té")
        print(f"Valor base: ${vb_te}")
    elif opcion == 3:
        es_estudiante = input("Es estudiante? (S/N)")
        print("Producto: Sandwich")
        print(f"Valor base: ${vb_sandwich}")
    elif opcion == 4:
        print("Gracias por usar el sistema")
        break
    else:
        print("Opcion no valida")
    