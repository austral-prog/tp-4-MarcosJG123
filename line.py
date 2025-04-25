def line():
    coeficienteA = input("Ingrese el coeficienteA :") 
    coeficienteB = input("Ingrese el coeficienteB :")
    coeficienteX1 = input("Ingrese el coeficienteX1 :")
    coeficienteX2 = input("Ingrese el coeficienteX2 :")
    coeficienteA = float(coeficienteA)
    coeficienteB = float(coeficienteB)
    coeficienteX1 = float(coeficienteX1)
    coeficienteX2 = float(coeficienteX2)
    Y1 = coeficienteA * coeficienteX1 + coeficienteB
    Y2 = coeficienteA * coeficienteX2 + coeficienteB
    P1 = f"({coeficienteX1}, {Y1})"
    P2 = f"({coeficienteX2}, {Y2})"
    distancia = ((coeficienteX1 - coeficienteX2)**2 + (Y1 - Y2)**2)**(1/2)

    print(f"El coeficiente A de su ecuación de la recta es: {str(coeficienteA)}")
    print(f"El coeficiente B de su ecuación de la recta es: {str(coeficienteB)}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {str(coeficienteX1)}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {str(coeficienteX2)}")
    print(f"""\nPara la siguiente ecuación:
\tY = {coeficienteA}X + {coeficienteB}""")
    print(f"""\nDados los siguientes puntos:
\tP1 {P1}
\tP2 {P2}""")
    print(f"\nLa distancia entre ellos es: {distancia}")
