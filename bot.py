import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Facebook UID Finder Bot-এ স্বাগতম!\n"
        "একটি Facebook numeric UID পাঠান।\n"
        "আমি প্রোফাইল লিংক তৈরি করে দেব।"
    )

async def handle_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = (update.message.text or "").strip()

    if not re.fullmatch(r"\d{5,25}", uid):
        await update.message.reply_text("শুধু সঠিক numeric Facebook UID পাঠান।")
        return

    link = f"https://www.facebook.com/profile.php?id={uid}"
    await update.message.reply_text(
        f"Facebook UID: {uid}\n"
        f"Profile link: {link}"
    )

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is missing.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_uid))
    app.run_polling()

if __name__ == "__main__":
    main()
