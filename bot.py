import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Download necessary NLTK datasets
nltk.download('punkt')

# Define pairs of input-output responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name?', ['I am a simple chatbot.', 'I am your chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
    (r'(.*)', ['Sorry, I didn\'t understand that. Can you rephrase?']),
]

# Define a chatbot class
class SimpleChatbot:
    def __init__(self):
        self.chat = Chat(pairs, reflections)
    
    def get_response(self, user_input):
        return self.chat.respond(user_input)

# Main function to interact with the chatbot
def main():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    chatbot = SimpleChatbot()
    
    while True:
        # Get user input
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input in ['bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        
        # Get the chatbot response
        response = chatbot.get_response(user_input)
        
        # Print chatbot's response
        print("Chatbot:", response)

# Run the chatbot
if __name__ == '__main__':
    main()
