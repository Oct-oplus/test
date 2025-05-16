import telebot

# استبدل 'YOUR_TOKEN' بالتوكن الذي حصلت عليه من BotFather
TOKEN = '8039737769:AAEcoiSKmE6MOBOlvY0kI1oZoUPxocDNBoQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! أنا بوت بسيط. كيف يمكنني مساعدتك؟")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.infinity_polling()