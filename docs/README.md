# Goal Guardian

## Introduction
**Goal Guardian** is an innovative to-do list application that harnesses the power of Artificial Intelligence (AI) to process user commands through voice input. This application leverages OpenAI's GPT model to interpret and execute commands on a user's to-do list, making task management more interactive and accessible.

## Features
- **Voice-Activated Commands**: Users can add, delete, update, and read tasks through simple voice commands.
- **AI-Powered Processing**: Integrates OpenAI's GPT to intelligently process spoken input, determine intent, and manage tasks accordingly.
- **Persistent Task Management**: Utilizes SQLite database to maintain a persistent state of tasks, ensuring data retention across sessions.
- **Accessible Interface**: Features a clean and simple user interface with high-contrast visuals for easy navigation and task management.

## How It Works
1. **Voice Recognition**: The application listens for user voice input using a microphone.
2. **Command Interpretation**: Voice inputs are sent to OpenAI's GPT model, which interprets the commands and generates task-specific actions like "ADD", "DELETE", "UPDATE", "READ", and "CLEAR".
3. **Task Management**: Depending on the AI's response, the application performs the necessary operations on the to-do list stored in a local SQLite database.
4. **Feedback**: The system provides vocal feedback to the user through text-to-speech technology, confirming the actions taken or asking for clarification.

## Example
Here are some typical interactions with Goal Guardian to illustrate its capabilities:

- **Add a Task**:
  - **Command**: "Add 'clean the kitchen' to my list" or "Put 'clean the kitchen' on the list."
  - **Action**: These commands are interpreted as "ADD clean the kitchen," and the program will add "clean the kitchen" to the database and update the task display.

- **Delete a Task**:
  - **Command**: "Delete 'clean the kitchen'" or "Remove 'clean the kitchen' from the list."
  - **Action**: Recognized as a "DELETE clean the kitchen," it will remove the specified task from the database.

- **Update a Task**:
  - **Command**: "Change 'clean the kitchen' to 'clean the living room'."
  - **Action**: This is interpreted as "UPDATE clean the kitchen TO clean the living room," and the task in the database is updated accordingly.

- **Read the Task List**:
  - **Command**: "What's on the list?" or "Read out my list."
  - **Action**: These are understood as a "READ" command, and the program will vocalize the current list of tasks.

- **Clear the Task List**:
  - **Command**: "Clear the list" or "Empty the list."
  - **Action**: Interpreted as a "CLEAR," which will remove all tasks from the database.

**Note**: For best results, ensure that commands are spoken clearly. The system is designed to handle minor variations in phrasing, enhancing user experience by accommodating natural speech patterns.

## Potential Expansions
While currently focused on task management, the architecture of **Goal Guardian** allows for expansion into other domains such as event scheduling, reminder systems, or even integrating with other services like email or calendar apps. The flexibility of the AI model provides a robust foundation for adding new features and capabilities.
