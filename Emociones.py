# -*- coding: utf-8 -*-
"""
Detector de emociones en tiempo real usando FER + OpenCV
--------------------------------------------------------
Este script detecta rostros y emociones en video en vivo.
Optimizado para equipos Windows (como ASUS TUF) con cámaras
que pueden cambiar de backend entre DSHOW, MSMF o VFW.

Requisitos:
    pip install fer opencv-python tensorflow mtcnn numpy
"""

import cv2
import numpy as np
import time
from fer import FER

def abrir_camara():
    """
    Intenta abrir la cámara usando distintos backends de OpenCV.
    Devuelve el objeto VideoCapture si logra abrirla, o None si falla.
    """
    print("🔍 Buscando cámara disponible...")

    # Lista de backends a probar (de más compatible a menos)
    backends = [
        cv2.CAP_DSHOW,  # DirectShow
        cv2.CAP_MSMF,   # Media Foundation
        cv2.CAP_VFW,    # Video for Windows
        0               # Default (sin especificar)
    ]

    for backend in backends:
        cap = cv2.VideoCapture(0, backend)
        if cap.isOpened():
            print(f"✅ Cámara abierta correctamente con backend {backend}")
            return cap
        else:
            cap.release()

    print("❌ No se encontró ninguna cámara disponible.")
    return None


def main():
    detector = FER(mtcnn=True)  # Detector con MTCNN para mejor precisión

    cap = abrir_camara()
    if not cap:
        return

    prev_time = 0
    print("🎥 Iniciando detección de emociones... (Presiona 'q' para salir)")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ No se pudo leer un frame. Intentando continuar...")
                time.sleep(0.2)
                continue

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = detector.detect_emotions(rgb_frame)

            for res in results:
                (x, y, w, h) = res["box"]
                emotions = res["emotions"]

                top_emotion = max(emotions, key=emotions.get)
                score = emotions[top_emotion]

                # Dibujar rectángulo y etiqueta
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 200, 0), 2)
                label = f"{top_emotion}: {score:.2f}"

                (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
                cv2.rectangle(frame, (x, y - th - 8), (x + tw + 6, y), (0, 200, 0), -1)
                cv2.putText(frame, label, (x + 3, y - 6),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1)

            # Mostrar FPS
            cur_time = time.time()
            fps = 1 / (cur_time - prev_time) if prev_time else 0.0
            prev_time = cur_time
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 0, 0), 2)

            cv2.imshow("Detector de Emociones - Fabian Guerra", frame)

            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("👋 Saliendo del programa...")
                break

    except KeyboardInterrupt:
        print("🛑 Interrumpido por el usuario.")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("✅ Recursos liberados correctamente.")


if __name__ == "__main__":
    main()
