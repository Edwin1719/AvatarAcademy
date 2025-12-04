# 🤖 AI Video Tutor

Un proyecto de tutoría impulsado por IA que utiliza avatares de video generados en tiempo real para crear experiencias de aprendizaje interactivas y personalizadas. Este repositorio contiene dos implementaciones: un tutor de video basado en scripts y un tutor de conversación en vivo.

## ✨ Características Principales

- **Tutor Basado en Scripts (`simple.py`):**
  - Haz una pregunta en lenguaje natural.
  - El sistema utiliza `GPT-4o` para generar una respuesta de tutoría detallada.
  - La respuesta se convierte en un video de un avatar digital que explica el concepto.
- **Tutor en Vivo (`live.py`):**
  - Inicia una videollamada interactiva en tiempo real con un tutor de IA.
  - Proporciona un contexto inicial a la conversación (por ejemplo, "Estamos estudiando ecuaciones cuadráticas").
  - El avatar de IA conversará contigo, recordando el contexto de la sesión actual.

---

## 🛠️ Arquitectura y Pila Tecnológica

Este proyecto integra un backend de Python con APIs de vanguardia para la generación de contenido y video.

- **Backend:** **Python** con el micro-framework **Flask**.
- **APIs Externas:**
  - **OpenAI API:** Se utiliza el modelo `gpt-4o` para la generación de respuestas inteligentes y guiones de tutoría.
  - **Tavus API:** Se utiliza para la generación de los avatares de video.
    - En `simple.py`, para crear videos a partir de un script.
    - En `live.py`, para alojar las conversaciones de video interactivas en tiempo real.
- **Frontend:** HTML simple renderizado directamente desde Flask con `render_template_string`.
- **Manejo de Dependencias:** `pip` y `requirements.txt`.
- **Configuración:** Variables de entorno gestionadas con `python-dotenv` (`.env`).

---

## ⚙️ Instalación y Configuración Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

**1. Clona el Repositorio**
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
```

**2. Crea y Activa un Entorno Virtual**
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instala las Dependencias**
```bash
pip install -r requirements.txt
```

**4. Configura tus Variables de Entorno**

Crea un archivo llamado `.env` en la raíz del proyecto y añade las siguientes claves. Reemplaza los valores de ejemplo con tus credenciales reales.

```env
TAVUS_API_KEY=tu_clave_de_api_de_tavus
OPENAI_API_KEY=tu_clave_de_api_de_openai
PERSONA_ID=tu_id_de_persona_de_tavus
REPLICA_ID=tu_id_de_replica_de_tavus

Para crear tus propios Persona ID y Replica ID (Clones y Avatares) en Tavus, puedes seguir este video tutorial:
[Tutorial de Tavus: Crear Clones y Avatares](https://www.youtube.com/watch?v=IcEs212oHRA&t=20s)

```

## 🚀 Uso

El proyecto tiene dos puntos de entrada. Puedes ejecutarlos en terminales separadas.

**Para el Tutor Basado en Scripts:**
```bash
python simple.py
```
Abre tu navegador y ve a `http://127.0.0.1:5001`.

**Para el Tutor en Vivo:**
```bash
python live.py
```
Abre tu navegador y ve a `http://127.0.0.1:5002`.

---

## 📂 Estructura del Proyecto

```
.
├── .env          # Archivo para las claves de API y configuración
├── live.py       # Aplicación Flask para el tutor en vivo
├── simple.py     # Aplicación Flask para el tutor basado en scripts
├── requirements.txt # Dependencias de Python
└── README.md     # Este archivo
```

---

## 💡 Potencial y Usos en la Industria

La tecnología de avatares de IA conversacionales tiene un vasto potencial en múltiples sectores:

- **Educación y EdTech:**
  - **Tutoría Personalizada 24/7:** Ofrecer ayuda escalable a estudiantes en cualquier materia.
  - **Aprendizaje de Idiomas:** Compañeros de conversación con paciencia infinita.
  - **Preparación de Exámenes:** Simulacros de entrevistas o exámenes orales.

- **Capacitación Corporativa y RRHH:**
  - **Onboarding de Empleados:** Guías interactivas sobre la cultura y procesos de la empresa.
  - **Desarrollo de Habilidades (Soft Skills):** Práctica de negociación, liderazgo o presentaciones.
  - **Entrenamiento de Cumplimiento Normativo:** Módulos interactivos y atractivos.

- **Salud y Bienestar:**
  - **Educación del Paciente:** Explicar diagnósticos o tratamientos de forma clara y visual.
  - **Asistentes de Terapia Cognitiva:** Realizar ejercicios guiados.

- **Ventas y Marketing:**
  - **Demostraciones de Productos Personalizadas:** Un avatar puede guiar a un cliente potencial a través de un producto.
  - **Cualificación de Leads:** Avatares en sitios web que interactúan con visitantes para calificarlos como clientes potenciales.

---

## 👨‍💻 Autor y Contacto

Este proyecto fue desarrollado por **Edwin Quintero Alzate**.

- **Perfil Profesional:** Ingeniero Industrial, Especialista en Big Data y Business Intelligence, y Data Engineer.
- **LinkedIn:** [linkedin.com/in/edwinquintero0329](https://www.linkedin.com/in/edwinquintero0329/)
- **GitHub:** [github.com/Edwin1719](https://github.com/Edwin1719)
- **Email:** [databiq29@gmail.com](mailto:databiq29@gmail.com)

---

## 🔮 Futuras Mejoras

- **Unificar Aplicaciones:** Combinar `simple.py` y `live.py` en una sola aplicación Flask con un menú de selección.
- **Análisis de Transcripciones:** Implementar un webhook para recibir las transcripciones de las conversaciones de Tavus y realizar análisis de calidad.
- **Gestión de Usuarios:** Añadir un sistema simple de usuarios para guardar el historial de videos generados.
- **UI/UX Mejorada:** Implementar un framework como Bootstrap o Tailwind CSS para una interfaz más pulida.
