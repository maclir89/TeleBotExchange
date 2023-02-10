import telebot
from Config import ID
from extensions import APIException, ExchangeConverter

bot = telebot.TeleBot(ID['token'])




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = f"Приветствую, {message.chat.first_name}!\nЯ умею конвертировать нужную вам валюту" \
           f" по курсу DemirBank. Чтобы узнать список валют напишите\n/values\nДля начала работы" \
           f" отправьте сообщение боту в виде <имя валюты, цену которой вы хотите узнать> <имя " \
           f"валюты, в которой надо узнать цену первой валюты> <количество первой валюты>" \
           f"\nПример:\nдоллар сом 100"
    bot.reply_to(message, text)

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        velues = message.text.lower().split(' ')

        if len(velues) != 3:
            raise APIException('Введено неверное количество параметров! Попробуйте снова!')

        base, quote, amount = velues
        total_base = ExchangeConverter.convert(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f"Цена {amount} {base} в {quote} - {total_base}"
        bot.send_message(message.chat.id, text)

bot.polling(non_stop=True, interval=0)
