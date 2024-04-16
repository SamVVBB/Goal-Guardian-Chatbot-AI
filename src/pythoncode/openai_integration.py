import openai
import os

# # Print the value of the OPENAI_API_KEY environment variable
# print(os.getenv('OPENAI_API_KEY'))

# Initialize the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def read_program_input(filename):
    """Read the contents of the input file."""
    with open(filename, "r") as file:
        return file.read()

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

def execute_command(command, program_input):
    """Handle user command and generate response."""
    ai_response = get_ai_response(program_input, command)
    # Here, you'd parse ai_response to determine CRUD operations
    # Example: if 'add' in ai_response, then call a function to add an item to the to-do list
    return ai_response

def main():
    program_input = read_program_input("Goal-Guardian-Chatbot-AI/docs/programPrompt.txt")
    user_input = "Add 'buy groceries' to my to-do list"

    # print(program_input + user_input)

    response = execute_command(program_input, user_input)
    print(response)

if __name__ == "__main__":
    main()
