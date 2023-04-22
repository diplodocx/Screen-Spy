import telebot
from clientWebsocket.client import ScreenClient
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['p'])
def get_photo(message):
    client = ScreenClient("localhost", 2000)  # choose server port
    if client.client:
        file_name = client.get_screen(str(message.id))
        with open(file_name, 'rb') as image:
            bot.send_photo(message.chat.id, image)
    else:
        bot.send_message(message.chat.id, "Сервер не отвечает")


bot.infinity_polling()
