import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters

# Token obtained from Telegram @BotFather OK
TOKEN = 'GANTI DI SINI'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

user_data = {}

async def start_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data[user_id] = {'phone_number': '08123456789', 'balance': 200000}

    menu_text = (
        f"Your number phone is {user_data[user_id]['phone_number']}. Select a menu:\n"
        "1. Check credit\n"
        "0. Exit"
    )
    
    await update.message.reply_text(menu_text)

async def check_credit_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    menu_text = (
        f"Your credit is Rp{user_data[user_id]['balance']}.\n"
        "9. Back to previous\n"
        "0. Exit"
    )
    
    await update.message.reply_text(menu_text)

async def handle_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text == '1':
        await check_credit_menu(update, context)
    elif text == '9':
        await start_menu(update, context)
    elif text == '0':
        await update.message.reply_text("Exiting the menu.")
    else:
        await update.message.reply_text("Invalid choice. Please enter a valid menu number.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start_menu)
    application.add_handler(start_handler)

    check_credit_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_input)
    application.add_handler(check_credit_handler)

    application.run_polling()
