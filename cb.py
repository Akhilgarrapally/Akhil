
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Test')
conv = open('chats.txt', 'r').readlines()

bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
    request = input('We: ')
    response = bot.get_response(request)
    print('Bot: ', response)
