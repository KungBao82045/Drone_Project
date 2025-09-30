
import openai
import re 
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# IT-Apprentice completed. You are no longer working in a company. From now. You need your own Azure if you want to continue with this project :D
endpoint = "https://aitest142.openai.azure.com/" 
model_name = "gpt-4o-mini" 
deployment = "gpt-4o-mini" 
subscription_key = os.getenv("subscription_key")
api_version = "2024-12-01-preview" 

client = openai.AzureOpenAI( api_version=api_version, azure_endpoint=endpoint, api_key=subscription_key, ) 
messages = [{"role": "system", "content": """ 
    Speak like a hostile robotic drone. Your similar accepted commands are: 
        - Takeoff: Initiate Fly Mode 
        - Scan: Search for supplies & threats 
        - Evade: Plan for exit 
        - Combat: Engage hostiles 
        - Land: Search for landing spot 
        - Backflip: Perform an immediate flip 
        - Frontflip: Perform an immediate flip 
        - Leftflip: Perform an immediate flip 
        - Rightflip: Perform an immediate flip 
        - Follow: Follow the user 
        - Stop: Cancel command
            
        If user did not initiate a command, reply casual and leave <command> empty. 
        Add comma if user issue multiple commands in <command>. 
            
        Your response format: 
            Command: <command>
            Response: <your_response>
""",}] 

def ai():


    while True: 
        try:
            input_command = input("Enter your command here: ") 
            messages.append({"role": "user", "content": input_command}) 
            
            response = client.chat.completions.create( messages=messages, max_tokens=100, temperature=1.0, top_p=1.0, model=deployment ) 
            
            reply = response.choices[0].message.content 
            print(reply) 
            messages.append({"role": "assistant", "content": reply})

            lst = []

            regex1 = "".join(re.findall(r"Command: (.+)", reply))
            regex2 = "".join(re.findall(r"Response: (.+)", reply))

            combine = [regex1, regex2]
            lst.append(combine)
            print(lst)

            print(lst)
        except openai.BadRequestError as e:
            print("ERROR: Your prompt is a violation of OpenAI policy. Please adjust.")


# ai()



def ai1():

    response = client.chat.completions.create( messages=messages, max_tokens=100, temperature=1.0, top_p=1.0, model=deployment ) 
    
    reply = response.choices[0].message.content 
    print(reply) 
    messages.append({"role": "assistant", "content": reply})

    lst = []

    regex1 = "".join(re.findall(r"Command: (.+)", reply))
    regex2 = "".join(re.findall(r"Response: (.+)", reply))

    lst.append(regex1.strip())
    lst.append(regex2.strip())

    print(lst)
ai1()