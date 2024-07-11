import random
import csv
from statistics import geometric_mean

####gracias profe alex

# Menu
def main():
    empleados = ["Juan Pérez", "María García", "Pedro Soto", "Isabel Gómez", "Miguel Sánchez", "Ana López", "Luis Fernández", "Carmen Ruiz", "Raúl González", "Laura Martínez"]
    sueldos = []

    while True:
        print("\n******** Gestión de Sueldos ********")
        print("===================================")
        print("[1] Asignar sueldos aleatorios")
        print("[2] Clasificar sueldos")
        print("[3] Ver estadísticas")
        print("[4] Reporte de sueldos")
        print("[5] Salir del programa")

        try:
            opcion = int(input("Ingrese su opción: "))
        except ValueError:
            print("La opción ingresada debe ser un número entero!! ")
            continue

        if opcion == 1:
            sueldos = gen_sueldos()
            print("Los 10 sueldos han sido asignados")
        elif opcion == 2:
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios")
                continue
            clasificacion = clasificar_sueldos(sueldos, empleados)
            mostrar_clasificacion(clasificacion)
        elif opcion == 3:
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios")
                continue
            ver_estadisticas(sueldos)
        elif opcion == 4:
            if not sueldos:
                print("Primero debe asignar sueldos aleatorios")
                continue
            detalles = calcular_sueldo_liquido(sueldos, empleados)
            for detalle in detalles:
                print(f"{detalle[0]}: Sueldo Base: ${detalle[1]}, Descuento Salud: ${detalle[2]}, Descuento AFP: ${detalle[3]}, Sueldo Líquido: ${detalle[4]}")
            exportar_a_csv(detalles)
        elif opcion == 5:
            print("Finalizando programa...")
            print("Desarrollado por Andru Alarcon")
            print("RUT 21353824-1")
            break
        else:
            print("La opción ingresada debe ser entre 1 y 5 solamente!!!!")

# esto genera los sueldos al azar
def gen_sueldos():
    sueldos = [random.randint(400000, 3000000) for _ in range(10)]
    return sueldos

# esto clasifica los sueldos
def clasificar_sueldos(sueldos, empleados):
    clasificacion = {
        'menores_800': [],
        'entre_800_y_2000': [],
        'mayores_2000': []
    }

    for sueldo, empleado in zip(sueldos, empleados):
        if sueldo < 800000:
            clasificacion['menores_800'].append((empleado, sueldo))
        elif 800000 <= sueldo <= 2000000:
            clasificacion['entre_800_y_2000'].append((empleado, sueldo))
        else:
            clasificacion['mayores_2000'].append((empleado, sueldo))
    
    return clasificacion

# esto muestra la clasificacion de los sueldos
def mostrar_clasificacion(clasificacion):
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(clasificacion['menores_800'])}")
    for empleado, sueldo in clasificacion['menores_800']:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(clasificacion['entre_800_y_2000'])}")
    for empleado, sueldo in clasificacion['entre_800_y_2000']:
        print(f"{empleado}: ${sueldo}")

    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(clasificacion['mayores_2000'])}")
    for empleado, sueldo in clasificacion['mayores_2000']:
        print(f"{empleado}: ${sueldo}")

    total_sueldos = sum(sueldo for clasif in clasificacion.values() for _, sueldo in clasif)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

# esto muestra las estadisticas
def ver_estadisticas(sueldos):
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = geometric_mean(sueldos)

    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica: ${media_geometrica:.2f}")

# esto calcula los sueldos y el sueldo loquido
def calcular_sueldo_liquido(sueldos, empleados):
    detalles = []
    for sueldo, empleado in zip(sueldos, empleados):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        detalles.append((empleado, sueldo, descuento_salud, descuento_afp, sueldo_liquido))
    
    return detalles

# exto exporta los sueldos a csv
def exportar_a_csv(detalles):
    with open('sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for detalle in detalles:
            writer.writerow(detalle)
    print("Datos exportados a sueldos.csv")

main()




