from gtts import gTTS
import os

# Text in Norwegian
text_norwegian = "Nagsimula na ang takeoff. Pag-akyat, pasulong sa target na altitude."  # "Hi, how are you?"

# Language: Norwegian (code: 'no')
tts_norwegian = gTTS(text=text_norwegian, lang='tl')

# Save the speech to a file
tts_norwegian.save("norwegian_output.mp3")

# Play the generated speech (optional)
os.system("mpg321 norwegian_output.mp3")
