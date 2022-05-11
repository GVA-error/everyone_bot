import telebot
from handlers.everyOneData import EveryOneData
from handlers.handlers import *

bot = telebot.TeleBot("5384660321:AAGg8UNrkMDoNJstAeRSAjzDbbDfGzNiPuA")

eData = EveryOneData()

@bot.message_handler(content_types=["text"])
def group_handler(message):
    fromUser = message.from_user
    nick = fromUser.first_name
    text = message.text

    if isEveryoneCall(text):
        names = eData.getEveryoneNames()
        ids = eData.getEveryoneChatIds()
        for id in ids:
            bot.send_message(id, f"::{text}")
        bot.send_message(message.chat.id, f"Позвал {names}")

    if isSaveCall(text):
        eData.addUser(fromUser)
        bot.send_message(message.chat.id, f"Я тебя запомнил @{nick}.")
    elif isRemoveCall(text):
        eData.removeUser(fromUser)
        bot.send_message(message.chat.id, f"Больше не буду тебе писать @{nick}.")


bot.polling(none_stop=True)