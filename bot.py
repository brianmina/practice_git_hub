# bot.py

from chatterbot import ChatBot

chatbot = ChatBot("Chatpot_error")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}") 
