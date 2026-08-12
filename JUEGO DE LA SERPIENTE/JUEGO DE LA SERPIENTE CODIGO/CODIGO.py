# =========================================================
# ASIGNATURA: Lógica de Programación
# PROYECTO: Juego de la Serpiente (Snake) 
# =========================================================

import random 

# Salida de datos e instrucciones por consola
print("========================================")
print("       JUEGO DE LA SERPIENTE (SNAKE)    ")
print("========================================\n")

# Entrada de los datos por el teclado
nombre = input("Ingresa tu nombre de jugador: ")

# Declaración de variables básicas (números enteros y booleanos)
ancho = 10
alto = 10
puntuacion = 0
juego_activo = True

# Lista para el cuerpo de la serpiente: cada elemento es [x, y]
# La posición [0] es la cabeza y las siguientes son el cuerpo
serpiente = [[5, 5], [5, 4]]

# Generación de la comida en posición aleatoria
comida_x = random.randint(1, 8)
comida_y = random.randint(1, 8)

print(f"\Hola {nombre}! El juego ha iniciado.")
print("Controles: W (Arriba), S (Abajo), A (Izquierda), D (Derecha) o Q (Salir).\n")

# Estructura repetitiva: Bucle principal mientras el juego esté activo
while juego_activo:
    # Mostramos el estado actual 
    cabeza = serpiente[0]
    print(f"Jugador: {nombre} | Puntos: {puntuacion}")
    print(f"Cabeza en: ({cabeza[0]}, {cabeza[1]}) | Comida en: ({comida_x}, {comida_y})")
    
    # Entrada por teclado del movimiento
    movimiento = input("¿A dónde te mueves? (W/A/S/D o Q para salir): ").upper()
    
    # Variables para calcular la nueva posición de la cabeza
    nueva_x = cabeza[0]
    nueva_y = cabeza[1]
    
    # Estructuras condicionales para cambiar las coordenadas según la opción ingresada
    if movimiento == "W":
        nueva_y = nueva_y + 1
    elif movimiento == "S":
        nueva_y = nueva_y - 1
    elif movimiento == "A":
        nueva_x = nueva_x - 1
    elif movimiento == "D":
        nueva_x = nueva_x + 1
    elif movimiento == "Q":
        print("\nHas decidido salir del juego.")
        juego_activo = False
        continue
    else:
        print("\nTecla no válida. Usa W, A, S, D o Q.\n")
        continue

    nueva_cabeza = [nueva_x, nueva_y]

    # Comentario explicativo: Esta condición sirve para verificar si la serpiente choca contra las paredes
    if nueva_x <= 0 or nueva_x >= ancho or nueva_y <= 0 or nueva_y >= alto:
        print("\n¡GAME OVER! Has chocado contra la pared.")
        juego_activo = False
        break

    # Comentario explicativo: Esta condición sirve para verificar si la serpiente choca contra su propio cuerpo
    if nueva_cabeza in serpiente:
        print("\n¡GAME OVER! Te has chocado contra tu propio cuerpo.")
        juego_activo = False
        break

    # Colocamos la nueva cabeza al inicio de la lista
    serpiente.insert(0, nueva_cabeza)

    # Comentario: Esta condición sirve para validar si la serpiente se come la fruta
    if nueva_x == comida_x and nueva_y == comida_y:
        puntuacion = puntuacion + 10
        print(f"\n¡Te comiste la fruta! Puntuación actual: {puntuacion}\n")
        # Se genera una nueva coordenada aleatoria para la fruta
        comida_x = random.randint(1, 8)
        comida_y = random.randint(1, 8)
    else:
        # Si no comió la fruta, se borra la ultima parte para mantener la longitud
        serpiente.pop()
