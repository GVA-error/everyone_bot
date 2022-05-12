import telebot
from handlers.everyOneData import EveryOneData
from handlers.handlers import *

bot = telebot.TeleBot("5384660321:AAGg8UNrkMDoNJstAeRSAjzDbbDfGzNiPuA")

eData = EveryOneData()
#f_mutex = False
@bot.message_handler(content_types=["text"])
def group_handler(message):
    fromUser = message.from_user
    nick = eData.getName(fromUser)
    text = message.text

    if isEveryoneCall(text):
        names = eData.getEveryoneNames()
        ids = eData.getEveryoneChatIds()
        badIds = []
        for id in ids:
            try:
                if eData.is_userWontMessages(fromUser):
                    bot.send_message(id, f"::{text}")
            except:
                badIds.append(id)

        bot.send_message(message.chat.id, f"Позвал: {names}")
        badNames = []
        for i, id in enumerate(ids):
            if id in badIds:
                badNames.append(eData.names[i])
        badNamesSting = f",".join(list(map(lambda name:f"@{name}", badNames)))
        if len(badNames) > 0:
            bot.send_message(message.chat.id, f"Не доступны (нет диалога): {badNamesSting}")


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