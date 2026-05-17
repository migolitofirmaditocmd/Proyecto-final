import gestion_datos
import interfaz_visual

def ejecutar_juego():
    print("\nIniciando configuración de partida...")
    # Ahora llamamos primero a la pantalla de dificultad
    ventana_dificultad = interfaz_visual.InterfazDificultad()
    return ventana_dificultad

def mostrar_ranking():
    print("RANKING DE LAS 5 MEJORES SESIONES")

    top_5 = gestion_datos.obtener_top_5_rankings()

    # Si no hay partidas jugadas todavía
    if not top_5:
        print("\n   Aún no hay registros de partidas guardadas.")
        print("   ¡Juega una partida para inaugurar el podio!")
    else:

        posicion = 1

        for jugador in top_5:

            fecha = jugador["fecha"]
            puntaje = jugador["puntaje"]

            print(f"\n#{posicion}")

            print("Fecha:")
            print(fecha)

            print("Puntaje:")
            print(f"{puntaje} puntos")

            print("----------------------")

            posicion += 1

    print("==============================\n")

if __name__ == "__main__":
    ejecutar_juego()
    mostrar_ranking()