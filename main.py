from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot_corpus



chatbot = ChatBot('Export Example Bot')

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

# if BotData.json is not empty then train the bot with the data in the file
try:
    trainer.train('./BOTDATA.json')
    print("Failed to load BOTDATA.json")
except:
    pass



#make it so the user can talk to the bot in the terminal using the input() function
while True:
    try:
        bot_input = chatbot.get_response(input("You:"))
        print("Bot:", bot_input)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

# Now we can export the data to a file
trainer.export_for_training('./BOTDATA.json')
