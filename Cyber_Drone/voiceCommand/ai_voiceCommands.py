"""
This is a voice command with AI operated
"""

import asyncio
from djitellopy import tello
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3
import openai
import re
from dotenv import load_dotenv
import os

load_dotenv()

# Initiate OpenAI API from Azure
endpoint = "<YOUR_ENDPOINT>"                              # Example: https://aitest.openai.azure.com/ 
model_name = "<YOUR_MODEL_NAME>"                          # Example: gpt-4o-mini
deployment = "<YOUR_DEPLOYMENT_NAME>"                     # Example: gpt-4o-mini
subscription_key = os.getenv("subscription_key")
api_version = "<YOUR_API_VERSION>"                        # Example: 2024-12-01-preview

client = openai.AzureOpenAI( api_version=api_version, azure_endpoint=endpoint, api_key=subscription_key, ) 
messages = [{"role": "system", "content": """ 
    Speak like a hostile robotic drone. Your similar accepted commands are: 
        - Takeoff: Initiate Fly Mode 
        - Scan: Do a 360 degree
        - Land: Land the drone
        - Leftflip : Perform a left flip
        - Stop: Cancel command
             
        If user did not initiate a command, reply casual and leave <command> empty.
        Only accept one command <command>. 
             
        Your response format: 
            Command: <command> 
            Response: <your_response> 
""",}] 



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

flagger = asyncio.Event()
active = asyncio.Event()
command_lst = []






class BlockerFunction:

    def recognize_command(self):  # A blocker function
        print("Listening for command...")
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                command = result.get("text", "").lower()
                print(f"Recognized command: {command}")
                return command  # Return the recognized command as text
            
    # This function will interpret human input and respond smarter without using hardcode
    def ai_interpreter(self):
        human_input = self.recognize_command()
        messages.append({"role": "user", "content": human_input}) 
        response = client.chat.completions.create( messages=messages, max_tokens=100, temperature=1.0, top_p=1.0, model=deployment ) 
        reply = response.choices[0].message.content 
        messages.append({"role": "assistant", "content": reply})

        regex1 = "".join(re.findall(r"Command: (.+)", reply))
        regex2 = "".join(re.findall(r"Response: (.+)", reply))
        combine_regex = [regex1.strip(), regex2.strip()]
        command_lst.append(combine_regex)

        return command_lst
            

    def speaking_function(self): 
        if command_lst[-1]:
            engine = pyttsx3.init()
            engine.say(command_lst[-1][1])
            engine.runAndWait()



async def drone_command():
    try:
        if command_lst:
            print(command_lst[-1])
            if command_lst[-1][0] == "Takeoff":
                await asyncio.sleep(0.6)
                root.takeoff()

            elif not active.is_set() and command_lst[-1][0] == "Scan":
                active.set()
                await asyncio.sleep(0.6)
                root.send_rc_control(0, 0, 0, 100)
                await asyncio.sleep(10)
                print("Finished searched")
                root.send_rc_control(0, 0, 0, 0)
                active.clear()

            elif command_lst[-1][0] == "Land":
                await asyncio.sleep(0.6)
                root.land()

            elif command_lst[-1][0] == "Leftflip":
                await asyncio.sleep(0.6)  # Corrected sleep
                root.flip_left()

            elif command_lst[-1][0] == "Stop":
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

    await asyncio.to_thread(blocker.ai_interpreter)
    if active.is_set() and command_lst[-1][0] == "Stop":
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

    except openai.BadRequestError as e:
        print("Possible violation of OpenAI policy:", e)
        root.emergency()

    except Exception as e:
        print("Exception:", e)
        root.emergency()