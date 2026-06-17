from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 TOKENINGNI SHU YERGA QO‘Y
TOKEN = "8610613439:AAGaNi2DM65tOeoJoATiMXImsORBXbQNXgE"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\n\nBot ishlayapti ✅"
    )

# /help command
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Buyruqlar:\n/start - botni ishga tushirish\n/help - yordam"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("Bot ishga tushdi...")

    app.run_polling()

if __name__ == "__main__":
    main()
