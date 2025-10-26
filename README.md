🎭 Detector de Emociones con IA

Sistema de inteligencia artificial que detecta y clasifica emociones faciales en tiempo real usando Deep Learning y Computer Vision.
---
## 🧠 Tecnologías utilizadas
- Python 3.12
- OpenCV
- TensorFlow
- FER (Facial Emotion Recognition)
---
## ⚙️ Instalación

- Clonar repositorio

  git clone https://github.com/fguerra369/detector-emociones.git
  
  cd detector-emociones

- Crear entorno virtual (recomendado)

  python -m venv .venv

- Activar entorno

  .venv\Scripts\activate  # Windows
  
  source .venv/bin/activate  # Mac/Linux

- Instalar dependencias

  pip install -r requirements.txt

- Ejecutar
 
  python Emociones.py
  
---
## 🎓 Casos de Uso
💼 Análisis de sentimientos en customer service

🧠 Investigación en psicología y comportamiento

🔒 Sistemas de seguridad inteligentes

📊 Marketing y UX research

💚 Aplicaciones de salud mental

---
## 📊 Arquitectura del Sistema

┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│ Video Input │ --> │ Face Detect  │ --> │   CNN Model │ --> │   Emotion    │
│  (Webcam)   │     │   (MTCNN)    │     │   (FER)     │     │ Classification│
└─────────────┘     └──────────────┘     └─────────────┘     └──────────────┘

---
## 📸 Demostración
El sistema detecta emociones en tiempo real y muestra la probabilidad de cada una:

😐 Neutral
😀 Feliz
😢 Triste
😡 Enojado
😮 Sorprendido

# Controles:

Q - Salir del programa

S - Capturar screenshot  

 

## 👨‍💻 Autor 
Fabián Guerra C.
