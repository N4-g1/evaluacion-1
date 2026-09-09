# Prompts utilizados para apoyo de IA

## 1) Prompt para maquetación HTML/Bootstrap

Prompt exacto:

"Diseña una plantilla HTML con Bootstrap para un sistema de gestión académica. Debe incluir un menú de navegación principal, un título principal y tres tarjetas con información de docentes, asignaturas y estudiantes. Usa colores suaves, estilo moderno y responsive. La estructura debe ser clara y profesional para una aplicación Django."

Respuesta generada por IA:

"Se propone una estructura base con navbar, cards de resumen y un layout limpio. Se recomienda usar Bootstrap 5, contenedores responsivos y `card` para cada área funcional. La paleta puede ser azul, verde y amarillo suaves para diferenciar las secciones. Todo el diseño debe mantenerse simple, legible y compatible con Django templates."

## 2) Prompt para generación de JSON de prueba

Prompt exacto:

"Genera un archivo JSON para un sistema académico con entidades Teacher, Course, Student y StudentCourse. Incluye 3 docentes, 3 asignaturas, 4 estudiantes y 4 inscripciones. Cada curso debe estar asociado a un docente. Cada inscripción debe relacionar un estudiante con un curso. El formato debe adaptarse a Django fixtures JSON del modelo `{model: 'academic.teacher', pk: ..., fields: {...}}` y ser válido para cargar con `manage.py loaddata`."

Respuesta generada por IA:

"Se entrega una estructura de fixtures lista para Django. Debe incluir alumnos con nombres y apellidos, cursos con nombres y `teacher`, y una tabla intermedia `StudentCourse` para registrar las matrículas. El resultado es un JSON válido que puede ser precargado en SQLite mediante loaddata para pruebas iniciales del backend."
