import telebot
from data import pcodes
from TOKEN_bot import token
bot = telebot.TeleBot(token)
baza = {}
@bot.message_handler(commands=['start'])
def start(message):
    name = str(message.from_user.first_name)
    bot.send_message(message.from_user.id,'Salom' + name)
    bot.send_message(message.from_user.id,'Promokodni yuborishingiz mumkin!')
@bot.message_handler(content_types=['text'])
def send(message):
    l = str(message.from_user.id)
    print(l)
    got = True
    if l not in baza.keys():
        baza[l] = [0, []]
    text = message.text
    if text == 'hisobim':
        bot.send_message(message.from_user.id, f"Sizning hisobingizda {baza[l][0]} so'm mablag' mavjud")
        got = False
    elif text in pcodes:
        if text not in baza[l][1]:
            baza[l][0] += 200
            baza[l][1].append(text)
            bot.send_message(message.from_user.id, f"Sizning hisobingizda {baza[l][0]} so'm mablag' mavjud")
            got = False
        else:
            bot.send_message(message.from_user.id, f"Bu promokodni ishlatgansiz")
            got = False
    if got:
        bot.send_message(message.from_user.id, "Noma'lum muammo /start")
bot.polling(none_stop = True)