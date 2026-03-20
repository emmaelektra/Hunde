# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS # google text to speech api
import os # to save the audio file
import pyttsx3  # conversion of text to speech
from langdetect import detect # to know what language was used
import pycountry
import numpy as np

import time
import board
import digitalio

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit

#set BLINKA_FT232H=1

#Servo set-up
# Initialize I2C bus
i2c_bus = busio.I2C(SCL, SDA)

# Initialize PCA9685 controller
pca = PCA9685(i2c_bus)
pca.frequency = 50  # Set the PWM frequency (you may need to adjust this based on your servo specifications)

# Initialize ServoKit
kit = ServoKit(channels=16)

# Define servo channels on PCA9685
servo_channels = [0, 1]  # Use the channels connected to your servo motors

# Function to set servo angle
def set_servo_angle(channel, angle):
    kit.servo[servo_channels[channel]].angle = angle  # Set servo angle directly

#Relay set-up
# Define relay pins
relay0_pin = board.C0  # Assigning to pin C0
relay1_pin = board.C1  # Assigning to pin C1

# Set up relay pins as digital outputs
relay0 = digitalio.DigitalInOut(relay0_pin)
relay0.direction = digitalio.Direction.OUTPUT

relay1 = digitalio.DigitalInOut(relay1_pin)
relay1.direction = digitalio.Direction.OUTPUT

# Button setup
button_pin = board.C4
button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
#button.pull = digitalio.Pull.DOWN

# Function to toggle relay state
def toggle_relay(relay, state):
    relay.value = state
    time.sleep(0.1)  # Adjust the delay as needed

relay0.value = True
relay1.value = True

# A tuple containing all the language - codes of the language will be detected
all_languages = ('afrikaans', 'af', 'albanian', 'sq', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be','bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)','zh-tw', 'corsican', 'co', 'croatian', 'hr','czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo','estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german','de', 'greek', 'el', 'gujarati', 'gu','haitian creole', 'ht', 'hausa', 'ha','hawaiian', 'haw', 'hebrew', 'he', 'hindi','hi', 'hmong', 'hmn', 'hungarian','hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian','id', 'irish', 'ga', 'italian','it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)','ku', 'kyrgyz', 'ky', 'lao', 'lo','latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb','macedonian', 'mk', 'malagasy', 'mg', 'malay','ms', 'malayalam', 'ml', 'maltese','mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian','mn', 'myanmar (burmese)', 'my','nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa','polish', 'pl', 'portuguese', 'pt', 'punjabi','pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd','serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl','somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish','sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu','te', 'thai', 'th', 'turkish','tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur','ug', 'uzbek', 'uz','vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')
lang_standard = 'en'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getLangName(lang_code):
    language = pycountry.languages.get(alpha_2 = lang_code)
    return language.name

# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language=lang_standard)
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query

def destination_language():
    print("Enter the language in which you	want to convert : Ex. Hindi , English , Spanish, etc.")
    print()

    # Input destination language in
    # which the user wants to translate
    to_lang = takecommand()
    while to_lang == "None":
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang

def translate():
    print ("Welcome to the translator! ")
    #speak ("Welcome to the translator! ")
    print ("Say the sentence you want to translate once you see the word 'listening'")

    # Input from user and make input to lowercase
    query = takecommand()
    while (query == "None"):
        query = takecommand()

    from_lang = detect(query)
    print ("The user's sentence is in ", getLangName(from_lang))

    # invoking Translator
    translator = Translator()

    end = 30

    #Make sure all servos on 0 deg
    for channel in servo_channels:
        set_servo_angle(channel, 0)  # Set initial angle (0 degrees)
    time.sleep(2)

    angles0 = np.linspace(0,70,90)
    angles0 = angles0.tolist()

    angles_back0 = np.linspace(70, 0, 90)
    angles_back0 = angles_back0.tolist()

    angles1 = np.linspace(0, 80, 80)
    angles1 = angles1.tolist()

    angles_back1 = np.linspace(80, 0, 80)
    angles_back1 = angles_back1.tolist()

    angles2 = np.linspace(0, 80, 80)
    angles2 = angles2.tolist()

    angles_back2 = np.linspace(80, 0, 80)
    angles_back2 = angles_back2.tolist()

    x = 0

    for n in range(0,end,2):
        to_lang = all_languages[n+1]
        print('n = ',n)

        # Mapping it with the code
        while (to_lang not in all_languages):
            print(
                "Language in which you are trying to convert is currently not available, please input some other language")
            print()
            to_lang = destination_language()

        # Translating from src to dest
        text_to_translate = translator.translate(query, dest=to_lang)

        text = text_to_translate.text

        #Translating back to English
        text_to_standard = translator.translate(text,dest=lang_standard)
        text_standard = text_to_standard.text

        # Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the destination language which is stored in to_lang.
        # Also, we have given 3rd argument as False because by default it speaks very slowly

        speak = gTTS(text=text_standard, lang=lang_standard, slow=False)

        # Using save() method to save the translated speech in capture_voice.mp3
        speak.save(r"C:\Users\limbo\Desktop\TAWA\Real-Time-Voice-Translator-in-Python\audioCap.mp3")

        if x == 0:
            # Turn servo 1
            for a in angles0:
                set_servo_angle(0, a)
                # time.sleep(0.1)
            # Switch relay 1 on
            #toggle_relay(relay0, False)
            print("Relay 1 ON")

            # Play sound
            playsound('audioCap.mp3')

            # Turn servo 1 back
            for ab in angles_back0:
                set_servo_angle(0, ab)
                # time.sleep(0.1)
            # Switch relay 2 off
            #toggle_relay(relay0, True)
            print("Relay 1 OFF")

            os.remove('audioCap.mp3')

        elif x == 1:
            # Turn servo 2
            for a in angles1:
                set_servo_angle(1, a)
                # time.sleep(0.1)
            # Switch relay 2 on
            #toggle_relay(relay1, False)
            print("Relay 2 ON")

            # Play sound
            playsound('audioCap.mp3')

            # Printing Output
            print(text)
            query = text_standard

            for ab in angles_back1:
                set_servo_angle(1, ab)
                # time.sleep(0.1)
            # Switch relay 2 off
            #toggle_relay(relay1, True)
            print("Relay 2 OFF")

            os.remove('audioCap.mp3')

        x += 1
        if x == 3:
            x = 0

y = 1
while y == 1:
    if not button.value:
        translate()

# Clean up
#for channel in servo_channels:
#    set_servo_angle(channel, 0)  # Set all servo angles back to 0 degrees

    #    pca.deinit()