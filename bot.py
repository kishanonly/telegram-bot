import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

BOT_TOKEN = "6901363578:AAFFwiHm2qpZq28cH8yKrkmshMyKylsoBF8"

# Function to get phone numbers from database
def get_phone_numbers(name):
    conn = sqlite3.connect('family.db')
    cursor = conn.cursor()
    
    # Execute query to get all matching records
    cursor.execute("SELECT phone_number FROM family WHERE name = ?", (name,))
    results = cursor.fetchall()  # Fetch all matching rows
    
    conn.close()
    
    # Check if results are found
    if results:
        # Join all phone numbers into a single string, separated by commas
        phone_numbers = ', '.join([result[0] for result in results])
        return phone_numbers
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
    # Get the text message from the user
    text = update.message.text.strip().lower()

    # Search the database for the name
    phone_numbers = get_phone_numbers(text.capitalize())  # Capitalize to match the database entries

    if phone_numbers != "No entry found for that name.":
        # If found, reply with the phone numbers
        await update.message.reply_text(f"{text.capitalize()}'s phone number(s): {phone_numbers}.")
    else:
        # If not found, reply with "Not found"
        await update.message.reply_text("Not found.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
