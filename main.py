import telebot
bot = telebot.TeleBot('8000721555:AAF0YwTphowNz9LkgMA0lN3ZEEm7g2aT5j0')

@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'Привет!!', parse_mode='Markdown')

@bot.message_handler(commands=['next'])
def main1(message):
	bot.send_message(message.chat.id, 'Как дела?', parse_mode='Markdown')

bot.infinity_polling()
