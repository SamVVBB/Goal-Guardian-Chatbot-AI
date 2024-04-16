# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 110)
# engine.say("America yah")
# engine.setProperty('rate', 200)
# while True:
#     answer = input("Enter \"Hallo\": \n")
#     if answer == "q":
#         engine.stop()
#         break
#     repeated_answer = answer * 4  # Repeat answer 4 times
#     engine.say(repeated_answer)
#     engine.runAndWait()
# engine.stop()

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 190)
# engine.setProperty('pitch', 190)

# while True:
#     wordsToSpeak = input("Enter words: \n")
#     if wordsToSpeak == "q":
#         engine.stop()
#         break
#     engine.say(wordsToSpeak)
#     engine.runAndWait()
# engine.stop()

import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('pitch', 190)

while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(text)
            engine.say(text)

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue


    # wordsToSpeak = input("Enter words: \n")
    # if wordsToSpeak == "q":
    #     engine.stop()
    #     break
    
    engine.runAndWait()
engine.stop()
