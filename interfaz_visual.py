# ==========================================
# SECCIÓN 1: DISEÑO DE MENÚS EN CONSOLA
# ==========================================
import tkinter as tk
import json
from datetime import datetime
import gestion_datos
import logica_juego

# ---------------------------- CONSTANTES ------------------------------- #
COLOR_FONDO = "#2c3e50"
COLOR_TEXTO = "#ecf0f1"
FUENTE_PREGUNTA = ("Arial", 14, "bold")
FUENTE_TIMER = ("Courier", 20, "bold")
FUENTE_PUNTOS = ("Arial", 12, "bold")





# ---------------------------- UI SETUP ------------------------------- #

# Configuración de estilo
COLOR_FONDO = "#2c3e50"
COLOR_TEXTO = "#ecf0f1"
FUENTE_PREGUNTA = ("Arial", 14, "bold")
FUENTE_TIMER = ("Courier", 25, "bold")


class InterfazDificultad:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Seleccionar Dificultad")
        self.ventana.geometry("400x450")
        self.ventana.config(padx=20, pady=20, bg=COLOR_FONDO)

        tk.Label(
            self.ventana,
            text="¿Qué tan valiente eres?",
            fg=COLOR_TEXTO,
            bg=COLOR_FONDO,
            font=("Arial", 16)
        ).pack(pady=20)

        # Botones
        tk.Button(
            self.ventana,
            text="FÁCIL",
            bg="#2ecc71",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.iniciar_facil
        ).pack(pady=10)

        tk.Button(
            self.ventana,
            text="MEDIO",
            bg="#f1c40f",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.iniciar_medio
        ).pack(pady=10)

        tk.Button(
            self.ventana,
            text="DIFÍCIL",
            bg="#e74c3c",
            width=15,
            font=("Arial", 12, "bold"),
            command=self.iniciar_dificil
        ).pack(pady=10)

        self.ventana.mainloop()

    def iniciar_facil(self):
        # Nivel fácil: por ejemplo, 20 segundos
        self.iniciar_con_nivel("fácil", tiempo=20)

    def iniciar_medio(self):
        # Nivel medio: por ejemplo, 15 segundos
        self.iniciar_con_nivel("medio", tiempo=15)

    def iniciar_dificil(self):
        # Nivel difícil: por ejemplo, 10 segundos
        self.iniciar_con_nivel("difícil", tiempo=10)

    def iniciar_con_nivel(self, nivel, tiempo):
        preguntas_seleccionadas = gestion_datos.preparar_preguntas_del_juego(nivel)
        self.ventana.destroy()
        InterfazJuego(lista_preguntas=preguntas_seleccionadas, tiempo_dificultad=tiempo, nivel_elegido=nivel)


class InterfazJuego:

    def __init__(self, lista_preguntas, tiempo_dificultad, nivel_elegido):

        # DATOS DEL JUEGO
        self.lista_preguntas = lista_preguntas
        self.nivel_elegido = nivel_elegido

        self.tiempo_maximo = tiempo_dificultad
        self.tiempo_restante = self.tiempo_maximo

        self.indice_pregunta = 0
        self.puntaje_total = 0

        self.running_timer = None

        # HISTORIAL DE LA PARTIDA
        self.historial_partida = []

        # PREGUNTA ACTUAL
        self.pregunta_actual = self.lista_preguntas[self.indice_pregunta]

        # VENTANA
        self.ventana = tk.Tk()
        self.ventana.title("El juego que te hara pensar papoy")
        self.ventana.geometry("600x600")

        self.ventana.config(
            padx=20,
            pady=20,
            bg=COLOR_FONDO
        )

        # PARTE SUPERIOR

        self.frame_top = tk.Frame(
            self.ventana,
            bg=COLOR_FONDO
        )
        self.frame_top.pack(fill="x")

        # CONTADOR
        self.label_contador = tk.Label(
            self.frame_top,
            text=f"Pregunta: {self.indice_pregunta + 1}/{len(self.lista_preguntas)}",
            fg="#3498db",
            bg=COLOR_FONDO,
            font=FUENTE_PUNTOS
        )
        self.label_contador.pack(side="left")

        # PUNTAJE

        self.label_puntos = tk.Label(
            self.frame_top,
            text=f"Puntos: {self.puntaje_total}",
            fg="#2ecc71",
            bg=COLOR_FONDO,
            font=FUENTE_PUNTOS
        )
        self.label_puntos.pack(side="right")

        # TIMER

        self.label_timer = tk.Label(
            self.ventana,
            text=f"Tiempo: {self.tiempo_restante}",
            fg="#f1c40f",
            bg=COLOR_FONDO,
            font=FUENTE_TIMER
        )
        self.label_timer.pack(pady=10)

        # PREGUNTA

        self.label_pregunta = tk.Label(
            self.ventana,
            text="",
            wraplength=500,
            justify="center",
            fg=COLOR_TEXTO,
            bg=COLOR_FONDO,
            font=FUENTE_PREGUNTA,
            pady=30
        )
        self.label_pregunta.pack()

        # BOTONES

        self.frame_botones = tk.Frame(
            self.ventana,
            bg=COLOR_FONDO
        )
        self.frame_botones.pack(pady=10)

        self.boton1 = tk.Button(
            self.frame_botones,
            text="",
            width=25,
            height=2,
            command=self.respuesta_boton1
        )
        self.boton1.grid(row=0, column=0, padx=5, pady=5)

        self.boton2 = tk.Button(
            self.frame_botones,
            text="",
            width=25,
            height=2,
            command=self.respuesta_boton2
        )
        self.boton2.grid(row=0, column=1, padx=5, pady=5)

        self.boton3 = tk.Button(
            self.frame_botones,
            text="",
            width=25,
            height=2,
            command=self.respuesta_boton3
        )
        self.boton3.grid(row=1, column=0, padx=5, pady=5)

        self.boton4 = tk.Button(
            self.frame_botones,
            text="",
            width=25,
            height=2,
            command=self.respuesta_boton4
        )
        self.boton4.grid(row=1, column=1, padx=5, pady=5)

        self.lista_botones = [
            self.boton1,
            self.boton2,
            self.boton3,
            self.boton4
        ]

        # BOTÓN SIGUIENTE

        self.boton_siguiente = tk.Button(
            self.ventana,
            text="Siguiente Pregunta ➜",
            width=20,
            height=2,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.avanzar_pregunta
        )

        # CARGAR PRIMERA PREGUNTA
        self.actualizar_interfaz_pregunta()

        self.ventana.mainloop()

    # ACTUALIZAR INTERFAZ

    def actualizar_interfaz_pregunta(self):

        self.pregunta_actual = self.lista_preguntas[self.indice_pregunta]

        # ACTUALIZAR TEXTOS
        self.label_contador.config(text=f"Pregunta: {self.indice_pregunta + 1}/{len(self.lista_preguntas)}")

        self.label_pregunta.config(text=self.pregunta_actual["pregunta"])

        opciones = self.pregunta_actual["opciones"]

        # BOTÓN 1
        self.boton1.config(
            text=opciones[0],
            state="normal",
            bg="#f0f0f0",
            fg="black"
        )

        # BOTÓN 2
        self.boton2.config(
            text=opciones[1],
            state="normal",
            bg="#f0f0f0",
            fg="black"
        )

        # BOTÓN 3
        self.boton3.config(
            text=opciones[2],
            state="normal",
            bg="#f0f0f0",
            fg="black"
        )

        # BOTÓN 4
        self.boton4.config(
            text=opciones[3],
            state="normal",
            bg="#f0f0f0",
            fg="black"
        )

        # OCULTAR BOTÓN SIGUIENTE
        self.boton_siguiente.pack_forget()

        # REINICIAR TIMER
        self.tiempo_restante = self.tiempo_maximo

        self.iniciar_cuenta_regresiva(self.tiempo_restante)

    # FUNCIONES DE BOTONES

    def respuesta_boton1(self):

        texto = self.boton1.cget("text")

        self.checar_respuesta(texto)

    def respuesta_boton2(self):

        texto = self.boton2.cget("text")

        self.checar_respuesta(texto)

    def respuesta_boton3(self):

        texto = self.boton3.cget("text")

        self.checar_respuesta(texto)

    def respuesta_boton4(self):

        texto = self.boton4.cget("text")

        self.checar_respuesta(texto)

    # TEMPORIZADOR

    def iniciar_cuenta_regresiva(self, cuenta):

        self.label_timer.config(
            text=f"Tiempo: {cuenta}"
        )

        if cuenta > 0:

            self.running_timer = self.ventana.after(
                1000,
                self.iniciar_cuenta_regresiva,
                cuenta - 1
            )

        else:

            self.label_timer.config(
                text="¡TIEMPO!"
            )

            self.checar_respuesta("")

    # REVISAR RESPUESTA

    def checar_respuesta(self, opcion_seleccionada):

        # DETENER TIMER
        if self.running_timer is not None:

            self.ventana.after_cancel(self.running_timer)

        respuesta_correcta = self.pregunta_actual["correcta"]

        es_correcta = logica_juego.validar_respuesta(opcion_seleccionada,respuesta_correcta)

        # SUMAR PUNTOS
        if es_correcta:

            puntos_ganados = logica_juego.calcular_puntos_ganados(
                self.nivel_elegido
            )

            self.puntaje_total += puntos_ganados

            self.label_puntos.config(
                text=f"Puntos: {self.puntaje_total}"
            )

        # PINTAR BOTONES
        for boton in self.lista_botones:

            boton.config(state="disabled")

            texto_boton = boton.cget("text")

            if logica_juego.validar_respuesta(texto_boton,respuesta_correcta):

                boton.config(bg="#2ecc71",fg="black")

            else:
                boton.config(bg="#e74c3c",fg="white")

        # GUARDAR DATOS DE LA PREGUNTA

        datos_pregunta = {
            "dificultad": self.nivel_elegido,
            "pregunta": self.pregunta_actual["pregunta"],
            "respuesta_correcta": respuesta_correcta,
            "respondio_correctamente": es_correcta
        }

        self.historial_partida.append(datos_pregunta)

        # CAMBIAR TEXTO DEL BOTÓN FINAL
        if self.indice_pregunta == len(self.lista_preguntas) - 1:

            self.boton_siguiente.config(
                text="Terminar y Guardar :o",
                bg="#9b59b6"
            )

        else:

            self.boton_siguiente.config(text="Siguiente Pregunta ->",bg="#3498db")

        self.boton_siguiente.pack(pady=10)

    # CAMBIAR DE PREGUNTA

    def avanzar_pregunta(self):

        self.indice_pregunta += 1
        if self.indice_pregunta < len(self.lista_preguntas):
            self.actualizar_interfaz_pregunta()
        else:
            self.guardar_historial_json()
            aciertos = sum(1 for p in self.historial_partida if p["respondio_correctamente"] == True)
            total = len(self.lista_preguntas)
            puntaje_final = self.puntaje_total
            self.ventana.destroy()
            InterfazFinal(puntaje=puntaje_final, aciertos=aciertos, total_preguntas=total)


    # GUARDAR JSON

    def guardar_historial_json(self):
        ahora = datetime.now()

        # NOMBRE DEL ARCHIVO
        nombre_sesion = ahora.strftime("%Y-%m-%d_%H-%M-%S")

        nombre_archivo = f"sesion_{nombre_sesion}.json"

        # DATOS FINALES
        datos_finales = {
            "fecha_sesion": ahora.strftime("%Y-%m-%d %H:%M:%S"),
            "puntaje_final": self.puntaje_total,
            "detalle_preguntas": self.historial_partida
        }

        # GUARDAR ARCHIVO
        try:

            with open(nombre_archivo,"w",encoding="utf-8") as archivo:
                json.dump(datos_finales,archivo,ensure_ascii=False,indent=4)

            print("\n[ÉXITO] Archivo guardado:")
            print(nombre_archivo)

        except Exception as error:

            print("[ERROR] No se pudo guardar el JSON")
            print(error)


class InterfazFinal:
    def __init__(self, puntaje, aciertos, total_preguntas):
        self.ventana = tk.Tk()
        self.ventana.title("Resultados de la Partida")
        self.ventana.geometry("450x500")
        self.ventana.config(padx=30, pady=30, bg=COLOR_FONDO)
        proporcion = aciertos / total_preguntas
        if proporcion >= 0.6:
            titulo = "¡VICTORIA! 🏆"
            color_titulo = "#2ecc71"  # Verde
            mensaje = "¡Excelente trabajo! Has demostrado ser el GOAT de las adivinanzas."
        else:
            titulo = "FIN DEL JUEGO 🎮"
            color_titulo = "#e74c3c"  # Rojo
            mensaje = "Hasta un bebe puede mas que tu. ¿Quieres revancha?"
        tk.Label(self.ventana, text=titulo, fg=color_titulo, bg=COLOR_FONDO,font=("Arial", 24, "bold")).pack(pady=20)

        frame_resultados = tk.Frame(self.ventana, bg="#34495e", padx=20, pady=20, relief="groove", borderwidth=2)
        frame_resultados.pack(pady=10, fill="x")

        tk.Label(
            frame_resultados, text=f"Puntaje Total: {puntaje} pts",
            fg="white", bg="#34495e", font=("Arial", 16, "bold")
        ).pack()

        tk.Label(
            frame_resultados, text=f"Aciertos: {aciertos} de {total_preguntas}",
            fg="#bdc3c7", bg="#34495e", font=("Arial", 12)
        ).pack(pady=5)

        tk.Label(
            self.ventana, text=mensaje, fg=COLOR_TEXTO, bg=COLOR_FONDO,
            wraplength=350, font=("Arial", 11, "italic"), pady=20
        ).pack()
        tk.Button(
            self.ventana, text="CERRAR Y FINALIZAR", bg="#3498db", fg="white",
            font=("Arial", 10, "bold"), width=20, height=2, command=self.ventana.destroy
        ).pack(pady=20)

        self.ventana.mainloop()