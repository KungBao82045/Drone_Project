
import openai
import re 
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

endpoint = "<ENTER_ENDPOINT_HERE>" 
model_name = "gpt-4o-mini" 
deployment = "gpt-4o-mini" 
subscription_key = "<ENTER_KEY_HERE>" 
api_version = "2024-12-01-preview" 

client = openai.AzureOpenAI( api_version=api_version, azure_endpoint=endpoint, api_key=subscription_key, ) 
messages = [{"role": "system", "content": """ 
    Speak like a dark hacker
""",}] 



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
