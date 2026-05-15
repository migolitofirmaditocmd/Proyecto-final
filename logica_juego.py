"""

Responsabilidad: El 'cerebro' del juego y las reglas matemáticas.
"""

def limpiar_texto(texto):
    """Limpia el texto para una comparación justa (Sección 3.3 del flujo)"""
    return texto.strip().lower()

def validar_respuesta(entrada_usuario, respuesta_correcta):
    """Compara la respuesta procesada"""
    return limpiar_texto(entrada_usuario) == limpiar_texto(respuesta_correcta)

def gestionar_intentos(intentos_actuales):
    """Resta intentos si el usuario falla (Sección 3.4 del flujo)"""
    return intentos_actuales - 1

def calcular_puntos(intentos_restantes, dificultad):
    """
    Sistema de cálculo de puntos: 
    Más puntos por dificultad difícil y por acertar al primer intento.
    """
    base = 20 if dificultad.lower() == 'difícil' else 10
    # Bonus por eficiencia (opcional, basado en tu descripción de lógica)
    return base * (intentos_restantes + 1)



