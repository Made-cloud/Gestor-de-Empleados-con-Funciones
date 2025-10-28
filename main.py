salario =int(input("ingresar salario "))

desempeño = 

def calcular_bono(salario, desempeño): 
    if desempeño >= 90:
        bono = salario * 0.2
    elif desempeño >= 70:
        bono = salario * 0.1
    elif desempeño >= 50:
        bono = salario * 0.05
    else: 
        bono = 0
    return bono

print(f"El bono es: ${calcular_bono(salario, desempeno)}")