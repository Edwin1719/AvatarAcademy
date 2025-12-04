import os, requests
from flask import Flask, request, render_template_string
from dotenv import load_dotenv

load_dotenv()
TAVUS_API_KEY = os.getenv("TAVUS_API_KEY")

PERSONA_ID = os.getenv("PERSONA_ID")
REPLICA_ID = os.getenv("REPLICA_ID")

HEADERS = {"x-api-key": TAVUS_API_KEY, "Content-Type": "application/json"}
API = "https://tavusapi.com/v2"

HTML = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Live AI Tutor</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary-color: #6a0dad; /* Deep Purple */
      --primary-hover-color: #5a099a;
      --secondary-color: #007bff; /* Blue for secondary actions/links */
      --background-light: #eef1f5; /* Lighter background */
      --text-dark: #2c3e50; /* Darker text for readability */
      --text-muted: #7f8c8d;
      --card-background: #ffffff;
      --border-color: #e0e0e0;
      --shadow-sm: rgba(0, 0, 0, 0.08);
      --shadow-md: rgba(0, 0, 0, 0.15);
      --shadow-lg: rgba(0, 0, 0, 0.2);
    }
    body {
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 2.5rem;
      background-color: var(--background-light);
      color: var(--text-dark);
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      box-sizing: border-box;
      line-height: 1.6;
    }
    .container {
      max-width: 700px; /* Reduced width */
      width: 100%;
      margin: auto;
    }
    h1 {
      color: var(--primary-color);
      text-align: center;
      margin-bottom: 2.5rem;
      font-size: 2.8rem; /* Larger title */
      font-weight: 800; /* Extra bold */
      letter-spacing: -0.03em;
    }
    form {
      background: var(--card-background);
      padding: 3rem; /* More padding */
      border-radius: 16px; /* More rounded */
      border: 1px solid var(--border-color);
      box-shadow: 0 8px 30px var(--shadow-lg); /* Stronger shadow */
      display: flex;
      flex-direction: column;
      gap: 1.8rem; /* Increased gap */
      width: 100%;
    }
    .form-group {
      display: flex;
      flex-direction: column;
    }
    label {
      font-weight: 700; /* Bolder labels */
      margin-bottom: .8rem; /* More space */
      color: var(--text-dark);
      font-size: 1.15rem; /* Slightly larger labels */
    }
    textarea {
      width: 100%;
      height: 100px; /* Reduced height */
      padding: 0.8rem; /* Reduced padding */
      border-radius: 10px; /* More rounded */
      border: 1px solid var(--border-color);
      font-size: 1.05rem;
      resize: vertical;
      box-sizing: border-box;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    textarea:focus {
      border-color: var(--primary-color);
      box-shadow: 0 0 0 4px rgba(106, 13, 173, 0.2); /* Purple focus ring */
      outline: none;
    }
    button {
      padding: 0.8rem 1.5rem; /* Reduced padding */
      margin-top: 1.5rem;
      border-radius: 10px;
      border: none;
      background: linear-gradient(45deg, var(--primary-color), var(--primary-hover-color));
      color: white;
      font-weight: 700;
      font-size: 1.1rem; /* Slightly reduced font size */
      cursor: pointer;
      transition: all 0.3s ease;
      box-shadow: 0 6px 20px var(--shadow-md);
      letter-spacing: 0.02em;
    }
    button:hover {
      background: linear-gradient(45deg, var(--primary-hover-color), var(--primary-color)); /* Reverse gradient on hover */
      transform: translateY(-3px) scale(1.01);
      box-shadow: 0 8px 25px var(--shadow-lg);
    }
    button:active {
      transform: translateY(0);
      box-shadow: 0 4px 15px var(--shadow-md);
    }
    iframe {
      width: 100%;
      height: 650px; /* Slightly taller iframe */
      border: none;
      border-radius: 16px;
      margin-top: 3rem; /* More spacing */
      box-shadow: 0 10px 30px var(--shadow-lg);
      background-color: var(--card-background);
    }
    .note {
      color: var(--text-muted);
      text-align: center;
      margin-top: 2rem;
      font-size: 1rem;
      line-height: 1.5;
    }
    .note a {
      color: var(--secondary-color);
      text-decoration: none;
      font-weight: 600;
    }
    .note a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Live AI Tutor Personalizado</h1>
    <form method="post">
      <div class="form-group">
        <label for="context">Contexto de la Conversación (¿Qué debería saber el tutor?)</label>
        <textarea name="context" id="context" placeholder="Ej: Estamos cubriendo ecuaciones cuadráticas; mantén las respuestas cortas y haz preguntas de verificación."></textarea>
      </div>
      <button type="submit">✨ Iniciar Llamada con Tutor</button>
    </form>

    {% if conversation_url %}
      <p class="note">Tu sesión está lista. ¡Puedes empezar a hablar! Si el video no carga, por favor, recarga la página o revisa la consola del navegador.</p>
      <iframe allow="camera; microphone; autoplay; clipboard-read; clipboard-write"
              src="{{ conversation_url }}"></iframe>
      <p class="note">Comparte este enlace si es necesario: <a href="{{ conversation_url }}" target="_blank">{{ conversation_url }}</a></p>
    {% endif %}
  </div>
</body>
</html>
"""

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conversation_url = None
    if request.method == "POST":
        ctx = request.form.get("context", "").strip()
        body = {
            "persona_id": PERSONA_ID,
            "replica_id": REPLICA_ID,
            "properties": {
                "language": "spanish"
            }
        }
        if ctx:
            body["conversational_context"] = ctx

        r = requests.post(f"{API}/conversations", headers=HEADERS, json=body, timeout=60)
        r.raise_for_status()
        conversation_url = r.json().get("conversation_url")

    return render_template_string(HTML, conversation_url=conversation_url)

if __name__ == "__main__":
    app.run(debug=True, port=5002)