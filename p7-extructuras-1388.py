# ==============================================================================
# EJERCICIOS DE PYTHON: CONDICIONALES Y BUCLES
# ==============================================================================
# David Barrera NC = 1388
# ------------------------------------------------------------------------------
# 1. PYTHON CONDITIONS (Condicionales básicas: if)
# Referencia: https://www.w3schools.com/python/python_conditions.asp
# ------------------------------------------------------------------------------
print("=== 1. PYTHON CONDITIONS ===")

# Ejemplo 1.1: Verificación de edad para conducir
edad = 20
if edad >= 18:
    print("Ejemplo 1.1: Eres mayor de edad, puedes obtener tu licencia.")

# Ejemplo 1.2: Control de temperatura
temperatura = 32
if temperatura > 30:
    print("Ejemplo 1.2: Hace calor afuera, recuerda tomar agua.")

print()  # Línea en blanco para separar secciones


# ------------------------------------------------------------------------------
# 2. PYTHON IF ... ELIF (Múltiples condiciones)
# Referencia: https://www.w3schools.com/python/python_if_elif.asp
# ------------------------------------------------------------------------------
print("=== 2. PYTHON IF ... ELIF ===")

# Ejemplo 2.1: Sistema de calificaciones escolares
nota = 85
if nota >= 90:
    print("Ejemplo 2.1: Calificación A")
elif nota >= 80:
    print("Ejemplo 2.1: Calificación B")
elif nota >= 70:
    print("Ejemplo 2.1: Calificación C")

# Ejemplo 2.2: Determinar la etapa del día según la hora (formato 24h)
hora = 14
if hora < 12:
    print("Ejemplo 2.2: Buenos días")
elif hora < 19:
    print("Ejemplo 2.2: Buenas tardes")

print()


# ------------------------------------------------------------------------------
# 3. PYTHON IF ... ELSE (Condición con alternativa)
# Referencia: https://www.w3schools.com/python/python_if_else.asp
# ------------------------------------------------------------------------------
print("=== 3. PYTHON IF ... ELSE ===")

# Ejemplo 3.1: Determinar si un número es par o impar
numero = 7
if numero % 2 == 0:
    print(f"Ejemplo 3.1: El número {numero} es Par.")
else:
    print(f"Ejemplo 3.1: El número {numero} es Impar.")

# Ejemplo 3.2: Autenticación de usuario
usuario_ingresado = "admin"
if usuario_ingresado == "admin":
    print("Ejemplo 3.2: Acceso concedido al sistema.")
else:
    print("Ejemplo 3.2: Acceso denegado.")

print()


# ------------------------------------------------------------------------------
# 4. PYTHON FOR LOOPS (Bucles for)
# Referencia: https://www.w3schools.com/python/python_for_loops.asp
# ------------------------------------------------------------------------------
print("=== 4. PYTHON FOR LOOPS ===")

# Ejemplo 4.1: Recorrer una lista de frutas
frutas = ["Manzana", "Plátano", "Naranja"]
print("Ejemplo 4.1: Lista de compras:")
for fruta in frutas:
    print(f" - Comprar {fruta}")

# Ejemplo 4.2: Uso de range() para iterar sobre un rango de números
print("Ejemplo 4.2: Tabla del 5 (del 1 al 5):")
for i in range(1, 6):
    print(f" 5 x {i} = {5 * i}")

print()


# ------------------------------------------------------------------------------
# 5. PYTHON WHILE LOOPS (Bucles while)
# Referencia: https://www.w3schools.com/python/python_while_loops.asp
# ------------------------------------------------------------------------------
print("=== 5. PYTHON WHILE LOOPS ===")

# Ejemplo 5.1: Contador regresivo
contador = 3
print("Ejemplo 5.1: Despegue en...")
while contador > 0:
    print(f" {contador}...")
    contador -= 1
print(" ¡Despegue!")

# Ejemplo 5.2: Bucle con sentencia break al encontrar una condición
print("Ejemplo 5.2: Buscando el valor clave:")
posicion = 1
while posicion <= 10:
    if posicion == 4:
        print(f" ¡Valor clave encontrado en la posición {posicion}! Deteniendo bucle.")
        break
    print(f" Revisando posición {posicion}...")
    posicion += 1

print("David Barrera NC = 1388")