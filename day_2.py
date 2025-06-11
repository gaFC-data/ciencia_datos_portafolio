# Día 2: Entrada de datos y condicionales
# Autor: Guillermo Andrés Florez Castro

# Pedir el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")

# Pedir la nota y convertirla a número decimal
nota = float(input("¿Cuál fue tu nota final? "))

# Evaluar la nota
if nota >= 3.0:
    print(f"¡Felicitaciones, {nombre}! Aprobaste con una nota de {nota}.")
elif nota >= 2.0:
    print(f"{nombre}, estuviste cerca. Tu nota fue {nota}, pero no aprobaste.")
else:
    print(f"{nombre}, tu nota fue {nota}. Necesitas mejorar para la próxima.")
