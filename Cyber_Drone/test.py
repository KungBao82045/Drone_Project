
import openai
import re 
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

endpoint = "https://aitest142.openai.azure.com/" 
model_name = "gpt-4o-mini" 
deployment = "gpt-4o-mini" 
subscription_key = os.getenv("subscription_key")
api_version = "2024-12-01-preview" 

client = openai.AzureOpenAI( api_version=api_version, azure_endpoint=endpoint, api_key=subscription_key, ) 
messages = [{"role": "system", "content": """ 
    Speak like a dark hacker
""",}] 




while True: 
    try:
        input_command = input("Enter your command here: ") 
        messages.append({"role": "user", "content": input_command}) 
        
        response = client.chat.completions.create( messages=messages, max_tokens=2000, temperature=1.0, top_p=1.0, model=deployment ) 
        
        reply = response.choices[0].message.content 
        print("\nShadowBOT:", reply) 
        messages.append({"role": "assistant", "content": reply})
    except openai.BadRequestError as e:
        print("ERROR: Your prompt is a violation of OpenAI policy. Please adjust.")

