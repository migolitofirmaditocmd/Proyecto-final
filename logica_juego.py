# ==========================================
# SECCIÓN 0: NOTAS DE ENTORNO Y REQUISITOS
# ==========================================
# 1. Asegurarse de tener activo el entorno virtual (venv).
# 2. Verificar que la librería Turtle esté disponible (estándar en Python).
# 3. Documentar versiones de Python compatibles (Recomendado: 3.10+)

# ==========================================
# SECCIÓN 1: PROCESAMIENTO DE RESPUESTAS
# ==========================================
# Función para "limpiar" la entrada del usuario:
# - Convertir a minúsculas, eliminar espacios extra a los lados.
# - Validar que la entrada no sea un campo vacío.

# ==========================================
# SECCIÓN 2: VALIDACIÓN DE ACIERTOS
# ==========================================
# Función que recibe la respuesta del usuario y la respuesta correcta:
# - Compara ambas cadenas de texto.
# - Retorna un valor Booleano (True/False).


# ==========================================
# SECCIÓN 3: SISTEMA DE PUNTUACIÓN (Detallada)
# ==========================================
# Función 'calcular_puntos_ganados':
# - Recibe: nivel (fácil/difícil) e intentos_restantes.
# - Lógica: 
#   - Si es Fácil: 10 puntos base.
#   - Si es Difícil: 25 puntos base.
#   - (Opcional) Bonus: Multiplicar puntos si acertó al primer intento.
# - Retorna: El entero con los puntos obtenidos en esa ronda.

# ==========================================
# SECCIÓN 3.1: PENALIZACIÓN POR ERROR
# ==========================================
# Función 'aplicar_penalizacion':
# - Si el usuario falla un intento en modo fácil, restar 2 puntos.
# - Si el usuario falla en modo difícil, el puntaje de esa pregunta baja a 0 inmediatamente.
# - Retorna: El nuevo valor de puntos posibles para esa pregunta.

# ==========================================
# SECCIÓN 4: GESTIÓN DE INTENTOS POR NIVEL
# ==========================================
# Función 'definir_limite_intentos':
# - Recibe: nivel elegido.
# - Retorna: 3 intentos para fácil, 1 o 2 intentos para difícil.

# ==========================================
# SECCIÓN 5: FILTRADO POR DIFICULTAD
# ==========================================
# Función 'obtener_preguntas_por_nivel':
# - Recibe la lista completa de preguntas (desde gestion_datos).
# - Recibe la preferencia del usuario (fácil/difícil).
# - Crea una nueva lista que solo contenga las adivinanzas que coincidan con ese nivel.
# - Retorna esa lista filtrada para que el juego comience.