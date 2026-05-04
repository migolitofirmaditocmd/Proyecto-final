## ==========================================
# SECCIÓN 1: IMPORTACIÓN DE MÓDULOS
# ==========================================
# Aquí se deben importar las funciones de:
# - logica_juego.py (para procesar jugadas)
# - gestion_datos.py (para cargar/guardar datos)
# - interfaz_visual.py (para mostrar menús y Turtle)

# ==========================================
# SECCIÓN 2: CONFIGURACIÓN INICIAL (Actualizada)
# ==========================================
# - Variable 'puntaje_total': Inicia en 0 al empezar cada partida.
# - Variable 'nombre_usuario': Capturar el nombre para el registro final.

# ==========================================
# SECCIÓN 3: BUCLE DE PREGUNTAS (Lógica de Sesión)
# ==========================================
# Por cada pregunta en la lista filtrada:
# 1. Mostrar la pregunta al usuario.
# 2. Iniciar bucle de intentos (según la dificultad).
# 3. Si acierta: Llamar a la función de puntos y sumarlos a 'puntaje_total'.
# 4. Si falla todos los intentos: Mostrar la respuesta correcta y continuar.

# ==========================================
# SECCIÓN 4: CONTROLADOR DE OPCIONES (Actualizado)
# ==========================================
# - Opción 'Jugar': 
#   1. Llamar a la interfaz de selección de dificultad.
#   2. Guardar la elección del usuario ('fácil' o 'difícil').
#   3. Solicitar a 'logica_juego' el mazo de preguntas filtrado.
#   4. Iniciar el bucle de preguntas basado en esa selección.

# ==========================================
# SECCIÓN 5: EJECUCIÓN SEGURA
# ==========================================
# Bloque 'if __name__ == "__main__":' para asegurar que el script
# solo se ejecute si es el archivo principal.


class Padre:
    def __init__(self):
        self.__x = 10

class SensorBase:
    def __init__(self):
        self.__calibracion = 1.0

    def factor(self):
        return self.__calibracion
    

Hola = SensorBase().factor() + 10

print(int(Hola))