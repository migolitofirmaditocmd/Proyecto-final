# ==========================================
# SECCIÓN 1: DISEÑO DE MENÚS EN CONSOLA
# ==========================================
import os

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_encabezado(titulo):
    print("=" * 50)
    print(f"{titulo.center(50)}")
    print("=" * 50)

def menu_principal():
    limpiar_pantalla()
    imprimir_encabezado("ADIVINANZAS PYTHON v1.0")
    print("\n[1] Comenzar Juego")
    print("[2] Ver Puntuaciones")
    print("[3] Salir")
    print("\n" + "-" * 50)

# ==========================================
# SECCIÓN 2: CONFIGURACIÓN DE TURTLE
# ==========================================
import turtle

def configurar_escenario():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("#2c3e50") # Un color oscuro elegante
    screen.title("Retroalimentación del Quiz")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0) # Velocidad máxima de dibujo
    return t, screen


# ==========================================
# SECCIÓN 3: ANIMACIONES DE RETROALIMENTACIÓN
# ==========================================
def dibujar_acierto(t):
    t.clear()
    t.pencolor("#2ecc71") # Verde esmeralda
    t.pensize(10)
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    # Dibujar una marca de "Check"
    t.setheading(-60)
    t.forward(40)
    t.setheading(45)
    t.forward(100)
    t.write("¡CORRECTO!", align="center", font=("Arial", 24, "bold"))

def dibujar_error(t):
    t.clear()
    t.pencolor("#e74c3c") # Rojo alizarina
    t.pensize(10)
    # Dibujar una X
    for i in range(2):
        t.penup()
        t.goto(-50, 50 if i == 0 else -50)
        t.pendown()
        t.setheading(-45 if i == 0 else 45)
        t.forward(140)
    t.penup()
    t.goto(0, -100)
    t.write("INCORRECTO", align="center", font=("Arial", 24, "bold"))

# ==========================================
# SECCIÓN 4: CELEBRACIÓN FINAL
# ==========================================
import random

def celebracion_final(t, screen):
    t.clear()
    screen.bgcolor("black")
    colores = ["yellow", "gold", "orange", "red", "white"]
    
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.write("¡PUNTAJE PERFECTO!", align="center", font=("Verdana", 30, "italic"))
    
    # Efecto de destellos
    for _ in range(20):
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.color(random.choice(colores))
        distancia = random.randint(20, 50)
        for _ in range(8):
            t.forward(distancia)
            t.backward(distancia)
            t.right(45)

    print("\n--- Haz clic en la ventana de Turtle para cerrar ---")
    screen.exitonclick()