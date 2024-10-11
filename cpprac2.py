import random

# Function to initialize the cube with constraints
def iniCubo(cb, num_empleados, semanas):
    for fil in range(num_empleados):
        for col in range(6):  # 6 days of the week
            for pro in range(semanas):
                horas = random.randint(0, 12)  # Random hours between 0 and 12
                cb[fil][col][pro] = horas

# Function to print the cube
def impCubo(cb, empleados, semanas):
    print("Datos", end=" ")
    for pro in range(semanas):
        print(f"S {pro + 1}", end=" ")
    print()

    # Days Header
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

# Function to calculate salaries
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

# Predefined data
empleados = ["Juan", "María", "Pedro"]
montos_por_hora = [15.0, 20.0, 18.0]  # Example hourly rates
semanas = 4  # Fixed to 4 weeks

# Declare the time recording bucket
num_empleados = len(empleados)
cubo = [[[0 for _ in range(semanas)] for _ in range(6)] for _ in range(num_empleados)]

# Calling functions
iniCubo(cubo, num_empleados, semanas)
impCubo(cubo, empleados, semanas)
calcular_salarios(cubo, empleados, montos_por_hora, semanas)
