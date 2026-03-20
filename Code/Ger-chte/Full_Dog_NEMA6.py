# Importing necessary modules required
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS # google text to speech api
import pyttsx3  # conversion of text to speech
from langdetect import detect # to know what language was used
import pycountry
from pydub import AudioSegment
import simpleaudio as sa

import time
import board
import digitalio
from pathlib import Path
import speech_recognition as sr
sr.AudioData.FLAC_CONVERTER = "flac"

# define path to save audio files
AUDIO_DIR = Path("/Users/emmasokoll/Documents/TAWA/Gerüchte/Code/Ger-chte/sound_files")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# invoking Translator
translator = Translator()

#set BLINKA_FT232H=1

motor_1 = digitalio.DigitalInOut(board.D4)
motor_1.direction = digitalio.Direction.OUTPUT
motor_1.value = False  # Set MOTOR_1_PIN to LOW

motor_2 = digitalio.DigitalInOut(board.D5)
motor_2.direction = digitalio.Direction.OUTPUT
motor_2.value = False  # Set MOTOR_2_PIN to LOW

motor_3 = digitalio.DigitalInOut(board.D6)
motor_3.direction = digitalio.Direction.OUTPUT
motor_3.value = False  # Set MOTOR_3_PIN to LOW

motor_4 = digitalio.DigitalInOut(board.D7)
motor_4.direction = digitalio.Direction.OUTPUT
motor_4.value = False  # Set MOTOR_1_PIN to LOW

motor_5 = digitalio.DigitalInOut(board.C6)
motor_5.direction = digitalio.Direction.OUTPUT
motor_5.value = False  # Set MOTOR_2_PIN to LOW

motor_6 = digitalio.DigitalInOut(board.C7)
motor_6.direction = digitalio.Direction.OUTPUT
motor_6.value = False  # Set MOTOR_3_PIN to LOW

time.sleep(2)

# Initialize relay control pins and set them to LOW initially
# Define relay pins
relay1_pin = board.C0  # Assigning to pin C0
relay2_pin = board.C1  # Assigning to pin C1
relay3_pin = board.C2  # Assigning to pin C2
relay4_pin = board.C3  # Assigning to pin C3
relay5_pin = board.C4  # Assigning to pin C4
relay6_pin = board.C5  # Assigning to pin C5

# Set up relay pins as digital outputs
relay1 = digitalio.DigitalInOut(relay1_pin)
relay1.direction = digitalio.Direction.OUTPUT

relay2 = digitalio.DigitalInOut(relay2_pin)
relay2.direction = digitalio.Direction.OUTPUT

relay3 = digitalio.DigitalInOut(relay3_pin)
relay3.direction = digitalio.Direction.OUTPUT

relay4 = digitalio.DigitalInOut(relay4_pin)
relay4.direction = digitalio.Direction.OUTPUT

relay5 = digitalio.DigitalInOut(relay5_pin)
relay5.direction = digitalio.Direction.OUTPUT

relay6 = digitalio.DigitalInOut(relay6_pin)
relay6.direction = digitalio.Direction.OUTPUT

relay1.value = True
relay2.value = True
relay3.value = True
relay4.value = True
relay5.value = False
relay6.value = False

time.sleep(2)

# Function to toggle relay state
def toggle_relay(relay, state):
    relay.value = state
    time.sleep(0.1)  # Adjust the delay as needed

# Run the relay test
# test_relays()

# Now you can proceed with your main program logic


# A tuple containing all the language - codes of the language will be detected
all_languages = ('afrikaans', 'af', 'albanian', 'sq', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be','bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)','zh-tw', 'corsican', 'co', 'croatian', 'hr','czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo','estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german','de', 'greek', 'el', 'gujarati', 'gu','haitian creole', 'ht', 'hausa', 'ha','hawaiian', 'haw', 'hebrew', 'he', 'hindi','hi', 'hmong', 'hmn', 'hungarian','hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian','id', 'irish', 'ga', 'italian','it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)','ku', 'kyrgyz', 'ky', 'lao', 'lo','latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb','macedonian', 'mk', 'malagasy', 'mg', 'malay','ms', 'malayalam', 'ml', 'maltese','mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian','mn', 'myanmar (burmese)', 'my','nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa','polish', 'pl', 'portuguese', 'pt', 'punjabi','pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd','serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl','somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish','sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu','te', 'thai', 'th', 'turkish','tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur','ug', 'uzbek', 'uz','vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')
lang_standard = 'de'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)


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

    end = 12
    x = 0

    #relay1_pin = board.C0  # Assigning to pin C0
    #relay1 = digitalio.DigitalInOut(relay1_pin)
    #relay1.direction = digitalio.Direction.OUTPUT
    #relay1.value = True

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

        # Convert translated text to speech
        tts = gTTS(text=text_standard, lang=lang_standard, slow=False)

        audio_mp3 = AUDIO_DIR / "audioCap.mp3"
        audio_wav = AUDIO_DIR / "louder_audio.wav"

        # Save and process audio
        tts.save(audio_mp3)
        audio = AudioSegment.from_file(audio_mp3)
        louder_audio = audio + 15
        louder_audio.export(audio_wav, format="wav")

        if x == 0:
            ## Turn motor 1
            print("Triggering Motor 1")
            motor_1.value = True  # Set MOTOR_1_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 1 Pin to LOW
            motor_1.value = False  # Set MOTOR_1_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 1 on
            toggle_relay(relay1, False)
            print("Relay 1 ON")
            time.sleep(1)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()

            time.sleep(1)

            ## Turn motor 1 back
            print("Turning back Motor 1")
            motor_1.value = True  # Set MOTOR_1_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 1 Pin to LOW
            motor_1.value = False  # Set MOTOR_1_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor


            ## Switch relay 2 off
            toggle_relay(relay1, True)
            print("Relay 1 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        elif x == 1:
            ## Turn motor 2
            print("Triggering Motor 2")
            motor_2.value = True  # Set MOTOR_2_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 2 Pin to LOW
            motor_2.value = False  # Set MOTOR_2_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 2 on
            toggle_relay(relay2, False)
            print("Relay 2 ON")
            time.sleep(1)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()


            ## Printing Output
            print(text)
            query = text_standard

            time.sleep(1)

            ## Turn motor 2 back
            print("Turning back Motor 2")
            motor_2.value = True  # Set MOTOR_2_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 2 Pin to LOW
            motor_2.value = False  # Set MOTOR_2_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 2 off
            toggle_relay(relay2, True)
            print("Relay 2 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        elif x == 2:
            ## Turn motor 3
            print("Triggering Motor 3")
            motor_3.value = True  # Set MOTOR_3_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 3 Pin to LOW
            motor_3.value = False  # Set MOTOR_3_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 3 on
            toggle_relay(relay3, False)
            print("Relay 3 ON")
            time.sleep(1)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()
            time.sleep(1)

            # Printing Output
            print(text)
            query = text_standard

            time.sleep(1)

            ## Turn motor 3 back
            print("Turning back Motor 3")
            motor_3.value = True  # Set MOTOR_3_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 3 Pin to LOW
            motor_3.value = False  # Set MOTOR_3_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 3 off
            toggle_relay(relay3, True)
            print("Relay 3 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        elif x == 3:
            ## Turn motor 4
            print("Turning Motor 4")
            motor_4.value = True  # Set MOTOR_4_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 4 Pin to LOW
            motor_4.value = False  # Set MOTOR_4_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 4 on
            toggle_relay(relay4, False)
            print("Relay 4 ON")
            time.sleep(1)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()

            # Printing Output
            print(text)
            query = text_standard

            time.sleep(1)

            ## Turn motor 4 back
            print("Turning back Motor 4")
            motor_4.value = True  # Set MOTOR_4_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 4 Pin to LOW
            motor_4.value = False  # Set MOTOR_4_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 4 off
            toggle_relay(relay4, True)
            print("Relay 4 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        elif x == 4:
            ## Turn motor 5
            print("Turning Motor 5")
            motor_5.value = True  # Set MOTOR_5_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 5 Pin to LOW
            motor_5.value = False  # Set MOTOR_5_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 5 on
            toggle_relay(relay5, True)
            print("Relay 5 ON")
            time.sleep(1)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()

            # Printing Output
            print(text)
            query = text_standard

            time.sleep(1)

            ## Turn motor 5 back
            print("Turning back Motor 5")
            motor_5.value = True  # Set MOTOR_5_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 5 Pin to LOW
            motor_5.value = False  # Set MOTOR_5_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 5 off
            toggle_relay(relay5, False)
            print("Relay 5 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        elif x == 5:
            ## Turn motor 6
            print("Turning Motor 6")
            motor_6.value = True  # Set MOTOR_6_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 6 Pin to LOW
            motor_6.value = False  # Set MOTOR_6_PIN to LOW
            time.sleep(2)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 6 on
            toggle_relay(relay6, True)
            print("Relay 6 ON")
            time.sleep(3)

            ## Play sound
            wave_obj = sa.WaveObject.from_wave_file(str(audio_wav))
            play_obj = wave_obj.play()
            # wait for playback to finish
            play_obj.wait_done()

            # Printing Output
            print(text)
            query = text_standard

            time.sleep(1)

            ## Turn motor 6 back
            print("Turning back Motor 6")
            motor_6.value = True  # Set MOTOR_6_PIN to HIGH
            time.sleep(0.5)  # Keep it high for 0.5 seconds

            # Set Motor 6 Pin to LOW
            motor_6.value = False  # Set MOTOR_6_PIN to LOW
            time.sleep(5)  # Wait for 5 seconds before triggering the next motor

            ## Switch relay 6 off
            toggle_relay(relay6, False)
            print("Relay 6 OFF")

            audio_mp3.unlink(missing_ok=True)
            audio_wav.unlink(missing_ok=True)

        x += 1
        if x == 6:
            x = 0

y = 1
while y == 1:

        translate()
# Clean up
#for channel in servo_channels:
#    set_servo_angle(channel, 0)  # Set all servo angles back to 0 degrees
