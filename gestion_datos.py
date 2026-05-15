import random

# ==========================================
# SECCIÓN 1: BANCO DE PREGUNTAS (Estructura de Datos)
# ==========================================

preguntas_db = [
    # ================= NIVEL FÁCIL =================
    {
        "pregunta": "Tengo agujas y no sé coser, tengo números y no sé leer. ¿Qué soy?",
        "opciones": ["Una brujula", "Una jeringa", "Un reloj", "Una maquina de coser"],
        "correcta": "Un reloj",
        "nivel": "fácil"
    },
    {
        "pregunta": "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera. ¿Qué soy?",
        "opciones": ["Aguacate", "Pera", "Sandía", "Melón"],
        "correcta": "Pera",
        "nivel": "fácil"
    },
    {
        "pregunta": "Mientras más me quitas más crezco. ¿Qué soy?",
        "opciones": ["Un hoyo", "Una deuda", "Un espacio", "El cabello"],
        "correcta": "Un hoyo",
        "nivel": "fácil"
    },
    {
        "pregunta": "Llevo mi casa al hombro, camino sin prisa y dejo un rastro de baba. ¿Qué soy?",
        "opciones": ["Una tortuga", "Un caracol", "Una babosa", "Un mochilero"],
        "correcta": "Un caracol",
        "nivel": "fácil"
    },
    {
        "pregunta": "Tengo agujeros, pero simpre retengo el agua. ¿Qué soy?",
        "opciones": ["Una nube", "Una toalla", "Un colador", "Una esponja"],
        "correcta": "Una esponja",
        "nivel": "fácil"
    },
    {
        "pregunta": "Cuanto más seco, más mojada me quedo. ¿Qué soy?",
        "opciones": ["Un trapeador", "El hielo", "La lluvia", "Una toalla"],
        "correcta": "Una toalla",
        "nivel": "fácil"
    },
    {
        "pregunta": "Siempre subo, pero nunca bajo. ¿Qué soy?",
        "opciones": ["El humo", "La edad", "Un globo", "El sol"],
        "correcta": "La edad",
        "nivel": "fácil"
    },
    {
        "pregunta": "Cuanto más le quitas, más grande se hace. ¿Qué soy?",
        "opciones": ["Un agujero", "Una montaña", "Una nube", "Un camino"],
        "correcta": "Un agujero",
        "nivel": "fácil"
    },
    {
        "pregunta": "Te pertenece a ti, pero los demás lo usan mucho más que tú. ¿Qué soy?",
        "opciones": ["Tu dinero", "Tu casa", "Tu nombre", "Tu ropa"],
        "correcta": "Tu nombre",
        "nivel": "fácil"
    },
    {
        "pregunta": "Tengo dientes pero no muerdo. ¿Qué soy?",
        "opciones": ["Un cierre", "Un peine", "Un tenedor", "Una sierra"],
        "correcta": "Un peine",
        "nivel": "fácil"
    },

    # ================= NIVEL MEDIO =================
    {
        "pregunta": "No tengo pies, pero voy de aquí para allá y nunca me ire. ¿Qué soy?",
        "opciones": ["Sombra", "El camino", "El tiempo", "El zapato"],
        "correcta": "Sombra",
        "nivel": "medio"
    },
    {
        "pregunta": "Lleno estoy de agujeros, pero soy muy resistente; si me usas en la cocina, el agua se me escapa siempre. ¿Qué soy?",
        "opciones": ["Un colador", "Una esponja", "Un rallador de queso", "Una red de pescar"],
        "correcta": "Un colador",
        "nivel": "medio"
    },
    {
        "pregunta": "No tengo cuerpo ni voz, empujo barcos y muevo molinos, a veces susurro y otras grito. ¿Qué soy?",
        "opciones": ["Viento", "El motor", "El pensamiento", "El agua"],
        "correcta": "Viento",
        "nivel": "medio"
    },
    {
        "pregunta": "Sin mí no hay sol ni sombrero. ¿Qué soy?",
        "opciones": ["La letra S", "Lentes de sol", "El verano", "La luz"],
        "correcta": "La letra S",
        "nivel": "medio"
    },
    {
        "pregunta": "Si me tienes, quieres compartirme; si me compartes, ya no me tienes. ¿Qué soy?",
        "opciones": ["Un secreto", "Tu nombre", "Un caramelo", "Un bostezo"],
        "correcta": "Un secreto",
        "nivel": "medio"
    },
    {
        "pregunta": "Cuanto más hay, menos ves. ¿Qué es?",
        "opciones": ["La oscuridad", "La niebla", "El humo", "El sueño"],
        "correcta": "La oscuridad",
        "nivel": "medio"
    },
    {
        "pregunta": "Vuelo sin alas, lloro sin ojos. ¿Qué soy?",
        "opciones": ["Una nube", "Una cebolla", "El humo", "El viento"],
        "correcta": "Una nube",
        "nivel": "medio"
    },
    {
        "pregunta": "Tengo hojas y no soy árbol, tengo lomo y no soy animal; si me abres, te cuento muchas cosas sin hablar. ¿Qué soy?",
        "opciones": ["Un libro", "Una carta", "Un cuaderno", "Un cuchillo"],
        "correcta": "Un libro",
        "nivel": "medio"
    },
    {
        "pregunta": "Soy de madera, tengo cuerdas y una caja de resonancia; si me tocas con cariño, lleno el aire de elegancia. ¿Qué soy?",
        "opciones": ["Una guitarra", "Un violín", "Un arpa", "Una marioneta"],
        "correcta": "Una guitarra",
        "nivel": "medio"
    },
    {
        "pregunta": "Me parezco a una piscina pero soy minúscula; me llenas para relajarte, pero si te quedas mucho tiempo, te arrugas como una pasa. ¿Qué soy?",
        "opciones": ["Una tina de baño", "Una taza de té", "Un jacuzzi", "El mar"],
        "correcta": "Una tina de baño",
        "nivel": "medio"
    },

    # ================= NIVEL DIFÍCIL (Adivinanzas que pediste) =================
    {
        "pregunta": "Hablo sin boca y oigo sin oídos. No tengo cuerpo, pero cobro vida con el viento. ¿Qué soy?",
        "opciones": ["El eco", "Una nube", "Un molino de viento", "Un silbato"],
        "correcta": "El eco",
        "nivel": "difícil"
    },
    {
        "pregunta": "Silbo sin labios, corro sin pies, te pego en la espalda y aún no me ves. ¿Qué soy?",
        "opciones": ["El viento", "El eco", "La sombra", "Un silbato"],
        "correcta": "El viento",
        "nivel": "difícil"
    },
    {
        "pregunta": "Tengo dos cuerpos unidos en uno; cuanto más me quedo quieto, más rápido corro. Si me volteas, sigo mi camino, pero si me detienes, el tiempo muere conmigo. ¿Qué soy?",
        "opciones": ["Un reloj de arena", "Una brújula", "Un río", "Una carretera"],
        "correcta": "Un reloj de arena",
        "nivel": "difícil"
    },
    {
        "pregunta": "Tengo un pulgar y cuatro dedos, pero no tengo carne ni hueso. ¿Qué soy?",
        "opciones": ["Un guante", "Una mano de esqueleto", "La sombra", "Un dibujo"],
        "correcta": "Un guante",
        "nivel": "difícil"
    },
    {
        "pregunta": "Tengo patas pero no puedo andar, y aunque tengo comida, nunca la puedo probar. ¿Qué soy?",
        "opciones": ["Una mesa", "Una silla", "Una nevera", "Un perro de peluche"],
        "correcta": "Una mesa",
        "nivel": "difícil"
    },
    {
        "pregunta": "Te acompaño en la oscuridad, pero si hay mucha luz, me apago. Tengo mecha pero no soy una bomba. ¿Qué soy?",
        "opciones": ["La vela", "Una linterna", "Un encendedor", "Un cohete"],
        "correcta": "La vela",
        "nivel": "difícil"
    },
    {
        "pregunta": "Vivo en el techo o en la pared, parezco un ojo que todo lo ve. No parpadeo, pero guardo en mi memoria todo lo que pasa frente a mí. ¿Qué soy?",
        "opciones": ["Una cámara de seguridad", "Un retrato", "Un espejo", "Un televisor"],
        "correcta": "Una cámara de seguridad",
        "nivel": "difícil"
    },
    {
        "pregunta": "Me meto en tus oídos pero no soy un bicho, te canto al oído y te cuento secretos, pero si me desconectas, el silencio es absoluto. ¿Qué soy?",
        "opciones": ["Unos audífonos", "Un susurro", "Una bocina", "Un tapón"],
        "correcta": "Unos audífonos",
        "nivel": "difícil"
    },
    {
        "pregunta": "Tengo palancas y botones, pero no soy un avión; me sostienes con dos manos para ganar la misión. ¿Qué soy?",
        "opciones": ["El control de consola", "Un volante de carreras", "Una carretilla", "Control de TV"],
        "correcta": "El control de consola",
        "nivel": "difícil"
    },
    {
        "pregunta": "Soy una red invisible que cruza el aire, no me puedes ver ni tocar, pero si te falto cinco minutos... ¡Te vas a desesperar! ¿Qué soy?",
        "opciones": ["El Wi-Fi", "El oxígeno", "El amor", "Señal de radio"],
        "correcta": "El Wi-Fi",
        "nivel": "difícil"
    }
]

# ==========================================
# SECCIÓN 2: ESCRITURA DE RESULTADOS (Actualizada)
# ==========================================

def guardar_puntaje_final(nombre_jugador, puntaje_total, dificultad_jugada):
    try:
        with open("resultados.txt", "a", encoding="utf-8") as archivo:
            linea = f"Jugador: {nombre_jugador} | Puntos: {puntaje_total} | Nivel: {dificultad_jugada}\n"
            archivo.write(linea)
    except Exception as e:
        print(f"Error al guardar: {e}")

# ==========================================
# SECCIÓN 3: LECTURA Y RANKING
# ==========================================

def mostrar_ranking():
    ranking = []
    try:
        with open("resultados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                
                partes = linea.strip().split(" | ")
                if len(partes) == 3:
                    nombre = partes[0].replace("Jugador: ", "")
                    puntos = int(partes[1].replace("Puntos: ", ""))
                    ranking.append({"nombre": nombre, "puntos": puntos})
        
        
        ranking_ordenado = sorted(ranking, key=lambda x: x["puntos"], reverse=True)
        
        print("\n--- TOP 5 PUNTAJES ---")
        for i, jugador in enumerate(ranking_ordenado[:5], 1):
            print(f"{i}. {jugador['nombre']} - {jugador['puntos']} pts")
            
    except FileNotFoundError:
        print("Aún no hay récords registrados.")

# ==========================================
# SECCIÓN 4: SELECCIÓN ALEATORIA Y MEZCLA
# ==========================================

def preparar_preguntas_del_juego(nivel_elegido):
    
    preguntas_filtradas = [p for p in preguntas_db if p["nivel"] == nivel_elegido]
    
    random.shuffle(preguntas_filtradas)
    
    for p in preguntas_filtradas:
        random.shuffle(p["opciones"])
        
    return preguntas_filtradas[:10]