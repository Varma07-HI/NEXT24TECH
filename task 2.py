import nltk
from nltk.chat.util import Chat, reflections
from introduction import introduction_convo  
from science import science_convo
from sports import sports_convo
from trivia import trivia_convo

# Create a chatbot instance
convos = trivia_convo + science_convo + sports_convo + introduction_convo

mychatbot = Chat(convos, reflections) 

# Start the conversation
print("!!HELLO!!")
print("I am your personal Chatbot")
print("How can I help you?")
print("Type 'quit' to exit")
mychatbot.converse()

