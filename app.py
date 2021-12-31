import telebot
from config import TOKEN, keys
from utils import ConvertionExeption, CryptoConverter
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате: \n<имя валюты> \
    <в какую валюту перевести> \
    <количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convetr(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Вводите только три параметра!')

        quote, base, amount = values
        total_base = CryptoConverter.convetr(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду, cмотрите /help \n{e}')
    else:
        text = f'{amount} {quote} = {total_base} {base}'
        bot.send_message(message.chat.id, text)

bot.polling()



