print("Semana No.12: Ejercicio1")
print("a.Sumatorias")
print("b.Factorial")
print("c.Tablas de multiplicar")
print("d.Número perfecto")

opcion=input("Elije una opción a calcular:")

match(opcion):
    case "a":
        n=0
        while n<=0:
         n=int(input("Ingrese un número entero positivo:"))
        if n <=0:
            print("El número igresado debe ser entero positivo.")
        Sumatoria=0
        for cont in  range(1,n+1):
            Sumatoria+=cont #sumatoria= sumatoria + cont
        print("La sumatoria es:", Sumatoria)
    case "a":
        print("Elija una opción válida")

    case "b":
        n= 0
        while n<=0:
            n= int(input("Ingrese un número entero positivo:"))
            if  n<=0:
                print("El numero ingresado debe ser entero positivo.")
        Factorial=1
        for cont in range(1,n+1):
            Factorial*=cont #factorial=factorial*cont
        print("La factorial es:", Factorial)

    case "c":
        for i in range(1,11):
            for j in range(1,11):
                print(i*j,"\t",end='')
            print()

    case "d":
        n=0
        while n<=0:
         n=int(input("Ingrese un númeroo entero positivo:"))
        if n <=0:
            print("El número igresado debe ser entero positivo.")
        acumulado=0
        for i in  range(1,n):
            acumulado+=i #sumatoria= sumatoria + cont
        if n==acumulado:
            print("Es perfecto")
        else:
            print("No es perfecto")
