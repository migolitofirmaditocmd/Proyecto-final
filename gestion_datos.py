# ==========================================
# SECCIÓN 1: BANCO DE PREGUNTAS (Estructura de Datos)
# ==========================================
# El diccionario de preguntas ahora DEBE incluir un campo 'nivel'.
# Ejemplo de lógica interna:
# {
#   "pregunta": "¿Qué tiene llaves pero no abre cerraduras?",
#   "respuesta": "piano",
#   "dificultad": "fácil"
# }
# {
#   "pregunta": "Soy alto cuando soy joven y corto cuando soy viejo. ¿Qué soy?",
#   "respuesta": "vela",
#   "dificultad": "difícil"
# }

# ==========================================
# SECCIÓN 2: ESCRITURA DE RESULTADOS (Actualizada)
# ==========================================
# Función 'guardar_puntaje_final':
# - Recibe: nombre_jugador, puntaje_total, dificultad_jugada.
# - Guarda en 'resultados.txt' una línea como: "Jugador: Juan | Puntos: 50 | Nivel: Difícil".
# - Asegurar que cada registro quede en una línea nueva.

# ==========================================
# SECCIÓN 3: LECTURA Y RANKING
# ==========================================
# Función que abre 'resultados.txt' en modo lectura (r):
# - Extrae los datos y los organiza (quizás en una lista).
# - Opcional: Ordenar los puntajes de mayor a menor para el Top 5.

# ==========================================
# SECCIÓN 4: SELECCIÓN ALEATORIA
# ==========================================
# (Opcional) Función que utiliza el módulo 'random' para 
# mezclar las preguntas y que el quiz no sea siempre igual.