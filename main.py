from telebot import TeleBot, types

# Initialize the bot with your token
bot = TeleBot("7628087790:AAFADZ1UQ1II7ECu2zwnctkbCbziDKW0QsA")

# Handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    # Create a button with WebApp URL
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = types.WebAppInfo("https://callmyphone.org/")  # Replace with your web app link
    button = types.KeyboardButton(text="Play Mini App", web_app=web_app)
    markup.add(button)

    # Send a message with the WebApp button
    bot.send_message(
        message.chat.id,
        "Click the button below to start the mini app!",
        reply_markup=markup
    )

# Polling
bot.polling()
