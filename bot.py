# bot.py

from chatterbot import ChatBot

<<<<<<< HEAD
chatbot = ChatBot("Chatpot_error__lets see")
=======
chatbot = ChatBot("Chatpot_thehellomodification")
>>>>>>> hello-world

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}") 
