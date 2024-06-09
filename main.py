import telebot
from telebot import types
from time import sleep


token = open(r"C:\Users\пётр\Desktop\token bot.txt").read()

bot = telebot.TeleBot(token)

remember_txt = ''


@bot.message_handler(commands=["start"])
def start(message):
    inline_markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('вспоми', callback_data='remember')
    inline_markup.add(item1)

    bot.send_message(message.chat.id, 'привет, я бот, который будет помогать тебе с твоими паролями.', reply_markup=inline_markup)


@bot.message_handler(content_types=['text'])
def main_funk(message):
    try:
        if message.text.strip().lower() == 'вспомни':
            bot.send_message(message.chat.id, 'ну го')
    except:
        bot.send_message(message.chat.id, 'не понял вас, может вы хотите добавить пароль или вспомнить?')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global remember_txt
    match call.data:
        case 'remember':
            bot.send_message(call.chat.id, 'напиши ник или приложения, которого тебе нужен пароль')
            bot.register_next_step_handler(call, remem)


@bot.message_handler(commands=['remember'])
def remem(message):
    pass


while True:
    try:
        bot.polling()
    except:
        sleep(10)
