import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
listener = sr.Recognizer()
speaker = pyttsx3.init()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
        return command.lower()

def handle_command(command):
    if "what is on my to-do list" in command:
        # Fetch to-do list from the database and create a response
        response = "Here is what is on your to-do list: Walk dog, pay loan, and order food."
    elif "put" in command and "on my list" in command:
        # Extract task and add to the database
        task = command.split("put")[1].split("on my list")[0].strip()
        # Insert task into the database
        response = f"I've successfully added '{task}' to your to-do list."
    else:
        response = "Sorry, I didn't understand that."
    return response

def speak(response):
    print(response)
    speaker.say(response)
    speaker.runAndWait()

def main():
    command = listen_command()
    response = handle_command(command)
    speak(response)

if __name__ == "__main__":
    main()
