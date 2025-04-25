def leap_year() :
    age = int(input("Ingrese un año:"))
    if age % 100 == 0 and age % 400 != 0:
        print("El año " + str(age) + " no es bisiesto")
    elif age % 4 != 0:
        print("El año " + str(age) + " no es bisiesto")
    else:
        print("El año " + str(age) + " es bisiesto")
