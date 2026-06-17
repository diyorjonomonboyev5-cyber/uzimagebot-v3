from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot ishlayapti ✅")

app = ApplicationBuilder().token("8610613439:AAGaNi2DM65tOeoJoATiMXImsORBXbQNXgE").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
