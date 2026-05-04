# Quiz de Adivinanzas Interactivo

Juego de adivinanzas interactivo desarrollado en Python que desafía la lógica del usuario mediante un sistema de niveles y puntajes. El programa integra validación de respuestas, persistencia de datos en archivos locales y retroalimentación visual mediante animaciones con Turtle.


## Características
Flujo del Juego (User Journey):

El programa sigue un ciclo lineal con validaciones constantes para asegurar que la experiencia no se rompa, en el siguiente orden:

1. Inicio y Bienvenida: 
        
        1.1 El sistema carga el banco de preguntas desde gestion_datos
        1.2 Solicita el nombre del jugador.

2. Configuración de Partida: 

        2.1 El usuario elige entre dificultad Fácil o Difícil.

        2.2 El sistema filtra el mazo de preguntas y asigna los intentos permitidos (3 o 1).

3. Ciclo de Adivinanza: 

        3.1 Se muestra el acertijo.

        3.2 El usuario ingresa su respuesta.

        3.3 logica_juego limpia el texto y compara.

        3.4 Si falla, se restan intentos; si acierta, se activa la animación de interfaz_visual.

4. Actualización de Estado:

        Se suman los puntos al total acumulado tras cada acierto.

5. Cierre y Registro: 

        Al terminar todas las preguntas, se muestra el puntaje final y se guarda automáticamente en el archivo histórico.

## Requisitos
- Python 3.x
- Biblioteca `turtle` (incluida en la instalación estándar de Python).

## Equipo de Desarrollo
👥 División de Roles (Equipo de 4)
Para garantizar un flujo de trabajo eficiente con Git, hemos dividido el proyecto en los siguientes módulos de responsabilidad:

1. Arquitecto de Flujo (Líder de main.py)

Responsabilidad: Orquestación del programa y control de menús.

Tareas: Gestión del bucle principal, navegación entre secciones y conexión de todos los módulos.

Archivo: main.py

2. Ingeniero de Lógica y Validación (logica_juego.py)

Responsabilidad: El "cerebro" del juego y las reglas matemáticas.

Tareas: Procesamiento de respuestas, sistema de cálculo de puntos y validación de intentos restantes.

Archivo: logica_juego.py

3. Gestor de Datos y Persistencia (gestion_datos.py)

Responsabilidad: Manejo de la "memoria" del programa.

Tareas: Creación del banco de preguntas, lectura/escritura del archivo de ranking y filtrado de dificultades.

Archivo: gestion_datos.py

4. Diseñador de Interfaz y Experiencia (interfaz_visual.py)

Responsabilidad: Estética y feedback hacia el usuario.

Tareas: Menus, mensajes de victoria/derrota y animaciones con Turtle.

Archivo: interfaz_visual.py