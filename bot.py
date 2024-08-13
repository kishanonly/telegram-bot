from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

BOT_TOKEN = "6901363578:AAFFwiHm2qpZq28cH8yKrkmshMyKylsoBF8"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Welcome to SathikissBot!')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "/start - Start interacting with the bot kishan \n"
        "/help - Get this help message kishan "
    )

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
