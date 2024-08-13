import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

BOT_TOKEN = "6901363578:AAFFwiHm2qpZq28cH8yKrkmshMyKylsoBF8"

# Function to get phone number from database
def get_phone_number(name):
    conn = sqlite3.connect('family.db')
    cursor = conn.cursor()
    cursor.execute("SELECT phone_number FROM family WHERE name = ?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "No entry found for that name."

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! Welcome to SathikissBot!')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "/start - Start interacting with the bot\n"
        "/help - Get this help message"
    )

async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "kishan" in text:
        phone_number = get_phone_number("Kishan")
        await update.message.reply_text(f"Kishan's phone number is {phone_number}.")
    else:
        await update.message.reply_text("You said: " + update.message.text)

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
