# About this project
The system will fetch the voice commands from the user and then structures response data from Azure OpenAI before forwarding the command to the drone over Wi-Fi. 

# Before you start (Important!)
Because you need to connect your drone through Wi-Fi, as well as connect to the internet to fetch the API endpoint, you require an extra Wi-Fi adapter to simultaneously connect to your drone and the internet. I recommend testing your drone in a safe environment with a good lighting source and a non-reflective surface to prevent confusing your drone's sensor. In case of an unstable flight, stop the script immediately.

# Requirements
You need:
* A drone that supports SDK (Software Development Kit). I recommend the DJI Tello for this experiment.
* To set up your own OpenAI model and your own OpenAI subscription token in Azure.
* PyCharm & Python (Version 3.9).

# How to start
This is the Python script you are going to use for this drone project: Cyber_Drone/voiceCommand/ai_voiceCommands.py
1. Open this project in PyCharm and execute this command to install the required libraries: "pip install -r requirements.txt" OR install the libraries manually.
2. Create a file called ".env" in "Cyber_Drone/voiceCommand/" and paste your OpenAI API token with this format: subscription_key=<YOUR_API_TOKEN>. A good security practice is to never paste your API token directly into the source code.
3. Replace the following variables in ai_voiceCommands.py (endpoint, model_name, deployment, and api_version) with your own.
4. Use your extra Wi-Fi adapter to connect to your drone.
5. Test your drone in a safe area. The following commands that are in function are:
  * Takeoff
  * Land
  * Leftflip
  * Stop
  * Scan

As for 09/04/25, this is my latest project.

