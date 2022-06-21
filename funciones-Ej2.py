def esPrimo():
    numeroEntero = int(input("Introduce un numero entero: "))
    if numeroEntero < 1:
        print("El número ingresado no es primo")
        return False
    for i in range(2, numeroEntero):
        if (numeroEntero % i) == 0:
            print("El numero ingresado no es primo")
            return False
    print("El numero ingresado es primo")
    return True

esPrimo()






