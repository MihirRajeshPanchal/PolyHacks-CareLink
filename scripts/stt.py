import speech_recognition as sr
import pyaudio 
from speech_recognition import *
from tts import tts
def stt():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            try: 
                text = r.recognize_google(audio)
                print(text)
            except:
                tts('Couldnt Recognize your voice')
                return "love agrodrone"
            return text
