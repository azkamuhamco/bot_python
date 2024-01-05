import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Token obtained from Telegram @BotFather
TOKEN = 'GANTI DI SINI'

# Logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send a welcome message with the interactive menu
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="City and Regency Checker - Special Region of Yogyakarta",
    )

# Message handler for handling user choices
async def handle_menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the user's choice
    user_choice = update.message.text

    # Check Regency or City
    regencies = ["Yogyakarta", "Sleman", "Gunungkidul", "Bantul", "Kulon Progo"]

    # Process the user's choice and send a response
    if user_choice in regencies:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Right! '"+ user_choice +"' is located in Special Region of Yogyakarta.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong! Try again!")

# Run the program
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command and message handlers
    start_handler = CommandHandler('start', start)
    menu_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice)

    application.add_handler(start_handler)
    application.add_handler(menu_handler)

    # Start the bot
    application.run_polling()
