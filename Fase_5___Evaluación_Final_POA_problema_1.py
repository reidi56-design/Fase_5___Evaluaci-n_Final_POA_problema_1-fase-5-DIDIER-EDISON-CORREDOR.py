# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Estuduante: DIDIER EDISON CORREDOR HORTUA
# Problema 1: Evaluación de Compromiso de Clientes en Sesiones
# Enfoque: Estructurado y Modular
# =====================================================================
# Matriz de datos
# ==========================================
# PROGRAMA: CLASIFICACIÓN DE COMPROMISO
# ==========================================

# Lista para almacenar las sesiones
sesiones = []

# ------------------------------------------
# FUNCIÓN PARA CLASIFICAR EL COMPROMISO
# ------------------------------------------
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# ------------------------------------------
# FUNCIÓN PARA AGREGAR SESIONES
# ------------------------------------------
def agregar_sesion():

    id_cliente = input("Ingrese el ID del cliente: ")

    duracion = int(input("Ingrese la duración de la sesión (segundos): "))

    clics = int(input("Ingrese la cantidad de clics: "))

    sesiones.append([id_cliente, duracion, clics])

    print("\nSesión agregada correctamente.\n")


# ------------------------------------------
# FUNCIÓN PARA MOSTRAR INFORME
# ------------------------------------------
def mostrar_informe():

    if len(sesiones) == 0:
        print("\nNo hay sesiones registradas.\n")
        return

    print("\n========== INFORME FINAL ==========\n")

    for sesion in sesiones:

        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)

        print(f"Cliente: {id_cliente}")
        print(f"Duración: {duracion} segundos")
        print(f"Clics: {clics}")
        print(f"Clasificación: {clasificacion}")
        print("-----------------------------------")


# ------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------
while True:

    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar sesión")
    print("2. Mostrar informe")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_sesion()

    elif opcion == "2":
        mostrar_informe()

    elif opcion == "3":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida.")