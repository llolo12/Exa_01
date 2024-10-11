import random

# Función para inicializar el cubo con restricciones
def iniCubo(cb, num_empleados, semanas):
    for fil in range(num_empleados):
        for col in range(6):  # 6 días de la semana
            for pro in range(semanas):
                horas = random.randint(0, 12)  # Horas aleatorias entre 0 y 12
                cb[fil][col][pro] = horas

# Función para imprimir el cubo
def impCubo(cb, empleados, semanas):
    print("Datos", end=" ")
    for pro in range(semanas):
        print(f"S {pro + 1}", end=" ")
    print()

    # Encabezado de días
    dias = ['L', 'K', 'M', 'J', 'V', 'S']
    for dia in dias:
        print(dia, end=" ")
    print()

    for fil in range(len(empleados)):
        print(empleados[fil], end=" ")
        for pro in range(semanas):
            for col in range(6):
                print(f"{cb[fil][col][pro]:>2}", end=" ")
        print()

# Función para calcular salarios
def calcular_salarios(cb, empleados, montos_por_hora, semanas):
    print("\nDatos Horas Normales Horas Extras Salario")
    print("Cantidad Valor Monto ¢ Cantidad Valor Monto ¢ Bruto")

    total_bruto = 0
    total_horas_normales = 0
    total_horas_extras = 0

    for fil in range(len(empleados)):
        horas_normales = 0
        horas_extras = 0
        for pro in range(semanas):
            for col in range(6):
                horas = cb[fil][col][pro]
                if horas > 8:
                    horas_normales += 8
                    horas_extras += horas - 8
                else:
                    horas_normales += horas

        salario_normal = horas_normales * montos_por_hora[fil]
        salario_extra = horas_extras * (montos_por_hora[fil] * 1.5)
        total = salario_normal + salario_extra

        print(f"{empleados[fil]:<10} {horas_normales:<7} {montos_por_hora[fil]:<5} {salario_normal:>10,.0f} {horas_extras:<10} {montos_por_hora[fil] * 1.5:<5} {salario_extra:>10,.0f} {total:>10,.0f}")
        
        total_bruto += total
        total_horas_normales += horas_normales
        total_horas_extras += horas_extras

    print(f"Sub Totales: {total_horas_normales:>10} {total_horas_extras:>10} {total_bruto:>10,.0f}")

# Entrada de datos
num_empleados = int(input("Ingrese la cantidad de empleados: "))
empleados = [input(f"Ingrese el nombre del empleado {i + 1}: ") for i in range(num_empleados)]
montos_por_hora = [float(input(f"Ingrese el monto por hora para {empleados[i]}: ")) for i in range(num_empleados)]
semanas = int(input("Ingrese la cantidad de semanas en el mes (4 o 5): "))

# Declarar el cubo de registro de horas
cubo = [[[0 for _ in range(semanas)] for _ in range(6)] for _ in range(num_empleados)]

# Llamar funciones
iniCubo(cubo, num_empleados, semanas)
impCubo(cubo, empleados, semanas)
calcular_salarios(cubo, empleados, montos_por_hora, semanas)
