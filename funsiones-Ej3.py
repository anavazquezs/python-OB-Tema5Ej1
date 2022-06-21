def anoBisiesto():
    anio = int(input("Ingrese el año para saber si es bisiesto: "))
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print("El año ingresado es bisiesto")
    else:
        print("El año ingresado no es bisiesto")

anoBisiesto()