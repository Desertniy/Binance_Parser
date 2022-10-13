# Python Files
import Token
import main

# Lib
import telebot
import json


bot = telebot.TeleBot(Token.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    stc = open('F:/Binance_P2P/Material/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stc)
    bot.send_message(message.chat.id,
                     f"Приветствую, <b>{message.from_user.first_name}</b>!\n Это я - <b>ИлонБот</b>. Я тебе помогу "
                     f"найти лучший курс закупки на Binance.",
                     parse_mode='HTML')
    bot.send_message(message.chat.id, "Выберите монету, о которой хотели бы пролучить информацию? <b>USDT</b>,"
                                      "<b>BTC</b>,<b>BUSD</b>,<b>BNB</b>,<b>ETH</b>,<b>SHIB</b>", parse_mode='html')


@bot.message_handler(content_types=['text'])
def rate_of_coins(message):
    stc_work = open('F:/Binance_P2P/Material/work.webp', 'rb')
    bot.send_sticker(message.chat.id, stc_work)
    bot.send_message(message.chat.id, f"<b>Одну секунду,посмотрим, что там на рынке с {message.text}</b>", parse_mode='html')
    main.main(message.text)
    with open(f'{message.text}.json', 'r') as file:
        js_f = json.load(file)
    for item in js_f:
        bot.send_message(message.chat.id, f"<b>{item['mn']}</b>\n<i>{item['link']}</i>", parse_mode='html')

bot.polling(none_stop=True)
