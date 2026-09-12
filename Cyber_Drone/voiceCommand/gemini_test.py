# To run this code you need to install the following dependencies:
# pip install google-genai

"""
GOAL: 
- Learn how to use Gemini API before continuing drone project.
- Recall what you have learned about Docker.
"""


from google import genai
import os

def generate():
    client = genai.Client(
        api_key=os.environ.get("API_KEY")
    )

    chat = client.chats.create(model="gemini-3.5-flash-lite")
    response = chat.send_message("How are you?").text
    print(response)

if __name__ == "__main__":
    generate()

