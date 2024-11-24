from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext

# Command to send the button
def start(update: Update, context: CallbackContext):
    # Create the inline button with the URL
    button = InlineKeyboardButton(text="Let's go!", url="https://t.me/notpixel/app?startapp=f7046488481")
    keyboard = InlineKeyboardMarkup([[button]])

    # Send the message with the button
    update.message.reply_text("Click the button below to open the web app:", reply_markup=keyboard)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot token
    updater = Updater("7628087790:AAFADZ1UQ1II7ECu2zwnctkbCbziDKW0QsA", use_context=True)

    # Add command handler
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
