# About this project
Control your drone using voice commands! With the implementation of OpenAI API, your drone can now communicate through natural language (english) instead of following hardcoded response.
As for 09/04/25, this is my latest project.

# Before you start (Important!)
Because you need to connect your drone through Wi-Fi, as well as connecting to the internet and fetch the API endpoint, you need an extra Wi-Fi adapter to connect to your drone and to the internet at the same time. 
I recommend to test your drone in a safe environment with a good lightning source and with non-reflectable surface to prevent confusing your drone sensor. In case of an unstable flight, stop the script immediately.

# Requirements
You need:
- A drone that support SDK (Software Development Kit). I recommend DJI Tello for this experiment.
- To setup your own OpenAI model and your own OpenAI subscription token in Azure. 
- PyCharm & Python (Version 3.9)

# How to start
This is the Python script you are going to use for this dron project: Cyber_Drone/voiceCommand/ai_voiceCommands.py
1. Execute this command to install the required libraries: pip install -r requirements.txt
2. Create a file called ".env" in "Cyber_Drone/voiceCommand/" and paste your OpenAI API token with this format: *subscription_key=<YOUR_API_TOKEN>*. A good security practice is to never paste your API token directly into the source code.
3. Replace the following variables in ai_voiceCommands.py (endpoint, model_name, deployment and api_version) with your own.
4. Use your extra Wi-Fi adapter to connect to your drone.
5. Test your drone in a safe area. The following commands that are in function are:
   - Takeoff
   - Land
   - Leftflip
   - Stop
   - Scan
