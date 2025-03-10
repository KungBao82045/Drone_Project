import asyncio
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3

# # Load the offline model
# model = Model("vosk-model-small-en-us-0.15")
# recognizer = KaldiRecognizer(model, 16000)

# # Initialize microphone input
# mic = pyaudio.PyAudio()
# stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
# stream.start_stream()


# history_commands = []
# flagger = asyncio.Event()
# active = asyncio.Event()


# engine = pyttsx3.init()
# engine.say("Hvordan går det?")
# engine.runAndWait()
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# for i, voice in enumerate(voices):
#     print(f"idx: {i} Voice: {voice.name}, ID: {voice.id}, Languages: {voice.languages}")

#     engine.say("こんにちは、元気ですか?")
#     engine.runAndWait()

engine.say("LEFT FLIP INITIATED. EXECUTING NOW.")
engine.runAndWait()
