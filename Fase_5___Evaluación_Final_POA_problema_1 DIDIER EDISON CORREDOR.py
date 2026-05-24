# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Estuduante: DIDIER EDISON CORREDOR HORTUA
# Problema 1: Evaluación de Compromiso de Clientes en Sesiones
# Enfoque: Estructurado y Modular
# =====================================================================
# Matriz de datos
sesiones = [
    ["C001", 250, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]

# Función para clasificar compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Generación del informe
print("INFORME DE COMPROMISO DE SESIONES\n")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente,
          "- Clasificación:", clasificacion)
