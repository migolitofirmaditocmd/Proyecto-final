# Quiz de Adivinanzas Interactivo

¡Bienvenido al desafío de ingenio! Este es un programa desarrollado en Python donde los usuarios pueden poner a prueba su lógica resolviendo adivinanzas categorizadas por niveles.

## Características
- **Múltiples categorías:** Elige tu nivel de dificultad.
- **Sistema de puntaje:** Acumula puntos y compite por el primer lugar.
- **Persistencia de datos:** Tus mejores resultados se guardan en un archivo local.
- **Feedback visual:** Animaciones simples para celebrar tus aciertos.

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

Tareas: Formateo de menús en consola, mensajes de victoria/derrota y animaciones con Turtle.

Archivo: interfaz_visual.py