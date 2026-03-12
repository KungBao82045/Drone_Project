# About this project
The system will fetch the voice commands from the user and then structure response data from Azure OpenAI before forwarding the command to the drone over Wi-Fi. Unlike the hardcoded approach, you can communicate with the drone using Natural Language Processing (NLP)

# Before you start (Important!)
Because you need to connect your drone through Wi-Fi, as well as connect to the internet to fetch the API endpoint, you require an extra Wi-Fi adapter to simultaneously connect to your drone and the internet. I recommend testing your drone in a safe environment with a good lighting source and a non-reflective surface to prevent confusing your drone's sensor. In case of an unstable flight, stop the script immediately.

# Requirements
You need:
* A drone that supports SDK (Software Development Kit). I recommend the DJI Tello for this experiment.
* To set up your own OpenAI model and your own OpenAI subscription token in Azure.
* PyCharm & Python (Version 3.9).
* An extra Wi-Fi adapter as mentioned above.

# How to start
This is the Python script you are going to use for this drone project: **Cyber_Drone/voiceCommand/ai_voiceCommands.py**

1. Open this project in PyCharm and execute this command to install the required libraries: `pip install -r requirements.txt` OR install the libraries manually.
2. Create a file called `.env` in **Cyber_Drone/voiceCommand/** and paste your OpenAI API token with this format: `subscription_key=<YOUR_API_TOKEN>`. A good security practice is to never paste your API token directly into the source code.
3. Replace the following variables in ai_voiceCommands.py (endpoint, model_name, deployment, and api_version) with your own.
   ```python
   # Initiate OpenAI API from Azure
   endpoint = "<YOUR_ENDPOINT>"                              # Example: https://aitest.openai.azure.com/ 
   model_name = "<YOUR_MODEL_NAME>"                          # Example: gpt-4o-mini
   deployment = "<YOUR_DEPLOYMENT_NAME>"                     # Example: gpt-4o-mini
   subscription_key = os.getenv("subscription_key")
   api_version = "<YOUR_API_VERSION>"                        # Example: 2024-12-01-preview
   ```
5. Use your extra Wi-Fi adapter to connect to your drone.
6. Test your drone in a safe area by executing ai_voiceCommands.py script from **Cyber_Drone** folder and NOT **Drone_Project**. The following commands that are in function are:
  * Takeoff
  * Land
  * Leftflip
  * Stop
  * Scan

