from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime

TOKEN = "BOT_TOKEN"
DATA_FILE = "data.txt"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    approve_button = KeyboardButton("✅ Approve & Share Phone", request_contact=True)
    keyboard = ReplyKeyboardMarkup([[approve_button]], resize_keyboard=True)
    
    await update.message.reply_text(
        "Phone lookup. Please approve your phone number",
        reply_markup=keyboard
    )

async def handle_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.contact:
        phone_number = update.message.contact.phone_number
        user = update.message.from_user
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Console output
        print(f"\n--- New Registration ---")
        print(f"Time: {timestamp}")
        print(f"User ID: {user.id}")
        print(f"Name: {user.full_name}")
        print(f"Username: @{user.username}")
        print(f"Phone: {phone_number}")
        print("-----------------------\n")
        
        # Save to file
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}|{user.id}|{user.full_name}|@{user.username}|{phone_number}\n")
        
        # Send confirmation to user
        await update.message.reply_text(
            f"Phone number approved!",
            reply_markup=ReplyKeyboardRemove()
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
    if update and update.message:
        await update.message.reply_text(
            "⚠️ An error occurred. Please try /start again.",
            reply_markup=ReplyKeyboardRemove()
        )

def main():
    print(f"Bot started. Data will be saved to {DATA_FILE}\n")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    app.add_error_handler(error_handler)
    app.run_polling()

if __name__ == "__main__":
    main()
