
def limpiar_texto(texto):
    """Convierte a minúsculas y quita espacios extra a los lados"""
    if texto is None:
        return ""
    return str(texto).strip().lower()


def validar_respuesta(respuesta_usuario, respuesta_correcta):
    """Compara ambas cadenas de texto limpias y retorna True o False"""
    usuario_limpio = limpiar_texto(respuesta_usuario)
    correcta_limpia = limpiar_texto(respuesta_correcta)

    return usuario_limpio == correcta_limpia

def calcular_puntos_ganados(nivel):
    """Retorna los puntos fijos asignados a cada dificultad"""
    nivel_limpio = nivel.strip().lower()

    if nivel_limpio == "fácil":
        return 10
    elif nivel_limpio == "medio":
        return 15
    elif nivel_limpio == "difícil":
        return 25
    else:
        return 0

