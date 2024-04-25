import customtkinter
import openai
import os
import speech_recognition as sr
import threading
from PIL import Image, ImageTk
from customtkinter import CTkImage
import pyttsx3

customtkinter.set_appearance_mode("dark")  # Set dark mode for all widgets
customtkinter.set_default_color_theme("green")  # Set green theme

# Initialize the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# set up TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('pitch', 190)

root = customtkinter.CTk()
root.title("Goal Guardian")
root.geometry("800x450")  # Set the window size

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (800 / 2))
y = int((screen_height / 2) - (450 / 2))
root.geometry(f"+{x}+{y}")

# Load the image using PIL
mic_icon_pil = Image.open("Goal-Guardian-Chatbot-AI/docs/icon_mic.png")
mic_icon_resized = mic_icon_pil.resize((80, 80), Image.Resampling.LANCZOS)
mic_icon = ImageTk.PhotoImage(mic_icon_resized)

tasks = []  # List to hold tasks
recognizer = sr.Recognizer()

def read_program_input(filename):
    """Read the contents of the input file."""
    with open(filename, "r") as file:
        return file.read()

# This is the leading prompt
program_input = read_program_input("Goal-Guardian-Chatbot-AI/docs/programPrompt.txt")

### STT ###

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

def listen_for_speech():
    """Function to listen for speech once and process it."""
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        print("Listening...")
        try:
            audio = recognizer.listen(mic, timeout=5)  # timeout to avoid hanging
            user_input = recognizer.recognize_google(audio)
            user_input = user_input.lower()
            print("User: " + user_input)

            response = get_ai_response(program_input, user_input)
            formatted_response = format_task_operation(response)
            print("AI: " + formatted_response)
            update_ai_display(formatted_response)
            threading.Thread(target=speak, args=(formatted_response,)).start()

        except sr.UnknownValueError:
            print("Could not understand audio")
            update_ai_display("Could not understand audio")
        except sr.WaitTimeoutError:
            print("Listening timed out")
            update_ai_display("Listening timed out")
        except Exception as e:
            print(f"Error: {e}")
            update_ai_display(f"Error: {e}")


def voice_input():
    """Activate the speech recognition to listen once."""
    print("Voice input activated")
    listen_for_speech()  # This is now a direct call

### AI ###

def get_ai_response(program_input, user_input):
    """Generate AI response based on the program input and user input."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Correct method for chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": program_input + user_input}
            ],  # Correct structure for chat completions
            max_tokens=150  # Adjust based on the expected length of the response
        )
        return response['choices'][0]['message']['content'].strip()  # Correct way to access chat response
    except Exception as e:
        print("Error:", e)
        return "I had a problem understanding that command."
        
def format_task_operation(action_response):
    try:
        action, task = action_response.split(maxsplit=1)
    except ValueError:
        action = action_response  # Only the action is present, no task specified

    if action == "ADD":
        add_task_to_list(task)
        return f"I have added '{task}' to your to-do list."
    elif action == "DELETE":
        delete_task_from_list(task)
        return f"I have removed '{task}' from your to-do list."
    elif action == "UPDATE":
        original, new = task.split(" TO ")
        update_task_on_list(original, new)
        return f"I have updated '{original}' to '{new}' on your to-do list."
    elif action == "CLEAR":
        clear_the_list()
        return "I have cleared your to-do list."
    elif action == "READ":
        return "Here are the items on your to-do list: \n" + read_the_list()
    else:
        return "I'm sorry, I didn't understand your request."
    
# program executions 
def add_task_to_list(task):
    if task:
        tasks.append(task)
        update_task_display()
        entry.delete(0, 'end')

def delete_task_from_list(task):
    try:
        tasks.remove(task)  # Remove the first occurrence of the task
        update_task_display()
    except ValueError:
        pass  # Do nothing if the task is not found

def update_task_on_list(original, new):
    try:
        index = tasks.index(original)
        tasks[index] = new
        update_task_display()
    except ValueError:
        print("Task not found.")

def clear_the_list():
    tasks.clear()
    update_task_display()

def read_the_list():
    if len(tasks) >= 3:
        # If there are three or more tasks, format the last task with "and finally"
        return ', '.join(tasks[:-1]) + ", and finally " + tasks[-1] + "."
    elif len(tasks) == 2:
        # For two tasks, use "and" between them
        return ' and '.join(tasks) + "."
    elif len(tasks) == 1:
        # For a single task, just return it followed by a period
        return tasks[0] + "."
    else:
        # Return an empty string if there are no tasks
        return "Your list is empty."

### GUI ###

def add_task():
    # Add task from the entry box to the task list
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_display()
        entry.delete(0, 'end')  # Clear the entry box after adding

def update_task_display():
    # Update the display with the current list of tasks
    task_display.configure(state='normal')  # Enable editing of Text widget
    task_display.delete(1.0, 'end')  # Clear the current display
    for task in tasks:
        task_display.insert('end', f"{task}\n")
    task_display.configure(state='disabled')  # Disable editing of Text widget

def update_ai_display(ai_message):
    # Update with the AI response
    ai_display.configure(state='normal')  # Enable the widget for editing
    ai_display.delete(1.0, 'end')  # Clear the current display
    ai_display.insert('end', f"{ai_message}\n")  # Insert the new message
    ai_display.configure(state='disabled')  # Disable editing after update

# Create frames for different sections
left_frame = customtkinter.CTkFrame(master=root)
left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

right_frame = customtkinter.CTkFrame(master=root)
right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

# Elements in the left frame

voice_button = customtkinter.CTkButton(
    master=left_frame,
    image=mic_icon,  # Use CTkImage for proper scaling on HighDPI displays
    text="",
    command=voice_input,  # Use the function that activates voice input
    width=60, height=60,  # Adjust size as necessary
    corner_radius=100
)
voice_button.pack(pady=10, padx=10, anchor='center')
voice_button.image = mic_icon # Keep as reference

ai_display = customtkinter.CTkTextbox(master=left_frame, font=("Roboto", 20), height=10)
ai_display.pack(fill='both', expand=True, padx=10, pady=10)
ai_display.configure(state='disabled')  # Initially disable editing of Text widget
ai_display.configure(wrap='word')  # Set wrapping to word boundaries

# Task entry and add button
entry = customtkinter.CTkEntry(master=left_frame, placeholder_text="Manual task entry")
entry.pack(pady=10, fill='x', expand=False)

add_button = customtkinter.CTkButton(master=left_frame, text="Add Task", command=add_task)
add_button.pack(pady=10)

# Elements in the right frame

# The List
label = customtkinter.CTkLabel(master=right_frame, text="To-do List", font=("Roboto", 50))
label.pack(pady=10)

task_display = customtkinter.CTkTextbox(master=right_frame, font=("Roboto", 26), height=10)
task_display.pack(fill='both', expand=True, padx=10, pady=10)
task_display.configure(state='disabled')  # Initially disable editing of Text widget

root.mainloop()
