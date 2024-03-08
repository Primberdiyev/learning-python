from transliterate import to_cyrillic, to_latin
import telebot 
TOKEN='7065466699:AAF88cIXOhPiGROndUfUpWmyuuOzgO2fNQ8'
bot=telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    javob=f"Assalomu Aleykum {username}, xush kelibsiz!"
    javob+="\nMatn kiriting: "
    bot.reply_to(message, javob)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
 
    bot.reply_to(message,javob(msg))
    
    
bot.polling()