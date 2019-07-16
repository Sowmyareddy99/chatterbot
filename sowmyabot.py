#importing libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
#identifying name of the chatterbot and defining name of the trainer

bot=ChatBot('CHOTTU')
bot.set_trainer(ListTrainer)

#accessing chatterbot corpus
for files in os.listdir('C:/Users/admin/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
        data=open('C:/Users/admin/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
        bot.train(data)

while True:
    message=input('you:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('Chatbot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('Chatbot:it was nice talking to u')
        break

