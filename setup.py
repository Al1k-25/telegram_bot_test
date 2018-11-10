import telebot
from telebot.types import Message

TOKEN = '785892912:AAEN6eVQ89J_X-ezIgpTtfbZsCD7bQue-80'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def message_handler(message: Message):
    bot.reply_to(message, 'start command reply')

@bot.message_handler(commands=['help'])
def message_handler(message: Message):
    bot.reply_to(message, 'Help command reply')

@bot.message_handler(content_types=['text'])
def message_handler(message: Message):
    bot.reply_to(message, 'test reply')
    
    
    


bot.polling()