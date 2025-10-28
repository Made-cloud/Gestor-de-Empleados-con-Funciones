# 1. INGRESO DE DATOS --->

def ingresar_datos():
    print("Ingreso de Datos Empleado de PyCompany")

    nombre = str(input("Ingrese el nombre del empleado: "))
    edad = int(input("Ingrese la edad del empleado: "))  
    cargo = str(input("Ingrese el cargo del empleado: "))
    sueldo = int(input("Ingrese el sueldo base ($): "))
    porcentaje_bono = int(input("Ingrese el porcentaje de bono (%) -> Si es 10%, escriba 10: "))
    return {"nombre": nombre, "edad": edad, "cargo": cargo, "sueldo": sueldo, "porcentaje_bono": porcentaje_bono}

empleado = ingresar_datos()
print(empleado)

# 2. CALCULO DE SUELDO --->

def calcular_bono(sueldo, porcentaje):
    bono = sueldo * (porcentaje/100)
    total = sueldo + bono
    return total

sueldoliquido = calcular_bono(empleado("sueldo"), empleado()"porcentaje_bono")
print("Sueldo líquido con bono:", sueldoliquido)

# 3. RESUMEN ---->

def mostrar_resumen(empleado):
     return {"nombre": nombre, "edad": edad, "cargo": cargo, "sueldo": sueldo, "porcentaje_bono": porcentaje_bono}

empleado = ingresar_datos()
print(empleado)


# 4. MENSAJE DE DESPEDIDA ---->

empleado = ingresar_datos()
mostrar_resumen(empleado)


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




def menu():
    return

def mostrar_mensaje_despedida():
    return print("Su solicitud ha sido axitosa")