"""
This is a voice command without OpenAI. No need to use internet connection.
Using Vosk for offline speech recognition and pyttsx3 for text-to-speech.
"""


import asyncio
from djitellopy import tello
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3

# Load the offline model
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Initialize microphone input
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Initialize the drone
root = tello.Tello()
root.connect()
print((root.get_battery()))
root.send_rc_control(0, 0, 0, 0)

history_commands = []
flagger = asyncio.Event()
active = asyncio.Event()

class BlockerFunction:
    def recognize_command(self):  # A blocker function
        print("Listening for command...")
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result.get("text", "").lower()
                print(f"Recognized command: {command}")
                history_commands.append(command)
                return command  # Return the recognized command as text

    def speaking_function(self):  # A blocker function
        if history_commands:
            engine = pyttsx3.init()

            if history_commands[-1] == "take off":
                engine.say("COMMAND ACCEPTED, INITIATING LIFT-OFF PROCEDURE. STANDBY FOR FURTHER ORDERS.")
                engine.runAndWait()

            elif history_commands[-1] == "search":
                engine.say("AREA SCAN INITIATED.")
                engine.runAndWait()

            elif history_commands[-1] == "stop":
                engine.say("Cancelled!")
                engine.runAndWait()

            elif history_commands[-1] == "flip":
                engine.say("PERFORMING A LEFT FLIP.")
                engine.runAndWait()

            elif history_commands[-1] == "hold":
                engine.say("HOLDING POSITION.")
                engine.runAndWait()

            elif history_commands[-1] == "land":
                engine.say("LANDING.")
                engine.runAndWait()


async def drone_command():
    try:
        if history_commands:
            command = history_commands[-1]

            if command == "take off":
                await asyncio.sleep(0.6)
                root.takeoff()

            elif not active.is_set() and command == "search":
                active.set()
                await asyncio.sleep(0.6)
                root.send_rc_control(0, 0, 0, 100)
                await asyncio.sleep(10)
                print("Finished searched")
                root.send_rc_control(0, 0, 0, 0)
                active.clear()

            elif command == "land":
                await asyncio.sleep(0.6)
                root.land()

            elif command == "flip":
                await asyncio.sleep(0.6)  # Corrected sleep
                root.flip_left()

            elif command == "hold":
                await asyncio.sleep(0.6)
                root.send_rc_control(0,0,0,0)

    except asyncio.CancelledError:
        active.clear()
        root.send_rc_control(0, 0, 0, 0)
        print("Drone got Cancelled! Returning to holding position")


async def sound_blocker():
    await asyncio.to_thread(blocker.speaking_function)
    await asyncio.sleep(1)
    await main() # Infinite loop

async def main():
    global drone_task

    await asyncio.to_thread(blocker.recognize_command)
    if active.is_set() and history_commands[-1] == "stop":
        drone_task.cancel()

    drone_task = asyncio.create_task(drone_command())
    sound_block = asyncio.create_task(sound_blocker())
    await asyncio.gather(sound_block, drone_task)


if __name__ == "__main__":
    blocker = BlockerFunction()
    # execution = BasicMovement()

    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print("KeyBoard Error:", e)
        root.emergency()
    except Exception as e:
        print("Exception:", e)
        root.emergency()