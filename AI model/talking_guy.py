import speech_recognition as sr
import os

import google.generativeai as genai
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)
# text_2=""
genai.configure(api_key="AIzaSyAKjdpAlrNWraKgGKNBV9uptjadPuYpjPw")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

def recognize_speech():
  recognizer = sr.Recognizer()
  mic = sr.Microphone()
  with mic as source:
    print("Please say something...")
    recognizer.adjust_for_ambient_noise(source)
    try:
      audio = recognizer.listen(source, timeout=5)  # Adjust timeout as needed (e.g., 5 seconds)
    except sr.WaitTimeoutError:
      print("Timeout. No speech detected.")
      return ""

  try:
    print("Recognizing speech...")
    text_1 = recognizer.recognize_google(audio)
    print(f"You said: {text_1}")
    response = chat_session.send_message(text_1)
    print(response.text)
    engine.say(response.text)
    engine.runAndWait()
    # return response
  except sr.UnknownValueError:
    print("Sorry, I did not understand that.")
    return ""
  except sr.RequestError:
    print("Sorry, the speech recognition service is unavailable.")
    return ""

if __name__=="__main__":
  recognize_speech()

# print(response.text)

test_1="hello"
print(type(test_1))

# import pyttsx3
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# engine.say("hi gokul welcome to the world of beasts")
# engine.setProperty('rate',150)
# engine.runAndWait()
#
#
# """
# Install the Google AI Python SDK
#
# $ pip install google-generativeai
#
# See the getting started guide for more information:
# https://ai.google.dev/gemini-api/docs/get-started/python
# """
#
# import os
#
# import google.generativeai as genai
# import pyttsx3
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# engine.setProperty('rate',150)
# genai.configure(api_key="AIzaSyADcS-xZSO5tAzWIJD7mg9o_xqXd8VwhQU")
#
# # Create the model
# # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 64,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }
# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#   },
# ]
#
# model = genai.GenerativeModel(
#   model_name="gemini-1.5-flash",
#   safety_settings=safety_settings,
#   generation_config=generation_config,
# )
#
# chat_session = model.start_chat(
#   history=[
#   ]
# )
#
# response = chat_session.send_message("reponse it in 100 words \ntell me about subash chandrapose")
#
# print(response.text)
# engine.say(response.text)
#
# engine.runAndWait()


