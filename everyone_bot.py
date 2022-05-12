import telebot
from handlers.everyOneData import EveryOneData
from handlers.handlers import *

bot = telebot.TeleBot("5384660321:AAGg8UNrkMDoNJstAeRSAjzDbbDfGzNiPuA")

eData = EveryOneData()

@bot.message_handler(content_types=["text"])
def group_handler(message):
    fromUser = message.from_user
    nick = eData.getName(fromUser)
    text = message.text

    if isEveryoneCall(text):
        names = eData.getEveryoneNames()
        ids = eData.getEveryoneChatIds()
        for id in ids:
            if eData.is_userWontMessages(fromUser):
                bot.send_message(id, f"::{text}")
        bot.send_message(message.chat.id, f"Позвал {names}")

    if isSaveCall(text):
        eData.addUser(fromUser)
        bot.send_message(message.chat.id, f"Я тебя запомнил @{nick}.")

    elif isRemoveCall(text):
        eData.removeUser(fromUser)
        bot.send_message(message.chat.id, f"@{nick} больше тебя не упомяну.")

    if isMessSattusCall(text):
        eData.userWontMessages(fromUser, True)
        bot.send_message(message.chat.id, f"@{nick} буду присылать тебе уведомления ещё и в личку")

    elif isUnMessSattusCall(text):
        eData.userWontMessages(fromUser, False)
        bot.send_message(message.chat.id, f"@{nick} тебе больше писать в личку не буду.")

bot.polling(none_stop=True)