from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR TOKEN HERE' with your actual bot token
BOT_TOKEN = "6901363578:AAFFwiHm2qpZq28cH8yKrkmshMyKylsoBF8"

def start(update, context):
    update.message.reply_text('Hello! Welcome to SathikissBot!')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
