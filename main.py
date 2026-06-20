import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from deep_translator import GoogleTranslator
import random as rd
duration = 5  # segundos de grabación
sample_rate = 44100
oportunidades = 3

palabras = {
    "easy": ["Hola", "Adiós", "Sí", "No", "Por favor", "Gracias", "Mirar", "Escuchar", "Detenerse", "Ir"],
    "medium": ["Querer", "Pensar", "Encontrar", "Necesitar", "Hacer", "Porque", "Pero", "Antes", "Después", "Debajo"],
    "hard": ["Petricor", "Serendipia", "Melindroso"]
}
while True:
    dificultad = input("Elige la dificultad (en ingles XD): ")
    if dificultad == "easy":
        palabra = rd.choice(palabras["easy"])
        print(f"traduce: {palabra}")
        break
    elif dificultad == "medium":
        palabra = rd.choice(palabras["medium"])
        print(f"traduce: {palabra}")
        break
    elif dificultad == "hard":
        palabra = rd.choice(palabras["medium"])
        print(f"traduce: {palabra}")
        break
    else:
        print("Oye, escribe una dificultad existente >:v")

while True:
    print("Habla ahora...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16")
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    print("Grabación completa, reconociendo...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
        print("Dijiste:", text)
        traduccion = GoogleTranslator(source="auto", target="en").translate(palabra)
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla.")
    except sr.RequestError as e:
        print(f"Error del servicio: {e}")
    if traduccion.lower() == text:
        print("Felicidades niño, buena traduccion")
    else:
        print("Perdiste")
        print(f"Se dice {traduccion}")
        oportunidades -= 1
    if oportunidades == 0:
        print("Perdiste :,(")