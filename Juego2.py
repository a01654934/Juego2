"""
Snake — versión con comida móvil y colores aleatorios (sin rojo).

Cambios:
1) La comida se mueve aleatoriamente 1 paso (10 px) por tick, sin salirse.
2) Cada vez que corre el juego, serpiente y comida tienen colores distintos,
   elegidos al azar de 5 colores (excluyendo rojo).
"""

from random import randrange, choice, sample
from turtle import *
from freegames import square, vector

# --- Estado del juego ---
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Colores permitidos (sin 'red'):
COLOR_POOL = ['black', 'blue', 'green', 'purple', 'orange']
snake_color, food_color = sample(COLOR_POOL, 2)  # dos colores distintos

def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def inside(p):
    """Regresa True si el vector p está dentro de los límites del tablero."""
    return -200 < p.x < 190 and -200 < p.y < 190

def move_food():
    """Mueve la comida 1 paso al azar sin salirse de la ventana."""
    # Posibles pasos de 10 px en las 4 direcciones
    steps = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    valid = []
    for d in steps:
        candidate = food.copy()
        candidate.move(d)
        if inside(candidate):
            valid.append(d)
    if valid:
        food.move(choice(valid))
    # Si no hay válidos (extremadamente raro por los límites), no se mueve.

def move():
    """Avanza la serpiente un segmento y actualiza la pantalla."""
    head = snake[-1].copy()
    head.move(aim)

    # Colisión con pared o consigo misma
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # rojo solo para mostrar choque
        update()
        return

    snake.append(head)

    if head == food:
        # Come: crece y reubica comida en una celda aleatoria del grid
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Mover comida un paso aleatorio SIN salirse
    move_food()

    clear()

    # Dibujo de la serpiente con su color aleatorio
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujo de la comida con su color aleatorio (distinto al de la serpiente)
    square(food.x, food.y, 9, food_color)

    update()
    ontimer(move, 100)  # ajusta este valor para hacerla más rápida/lenta

# --- Configuración de Turtle ---
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Controles de dirección
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()

