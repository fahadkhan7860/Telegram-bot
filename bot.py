from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8845487590:AAGVnDuUfq5llIh3FUEujpn2Q_t3DzlGQCE"

async def start(update, context):
    await update.message.reply_text("Crypto Father Bot online hai.")

async def reply(update, context):
    text = update.message.text
    await update.message.reply_text(f"Aapne likha: {text}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

print("Bot start ho raha hai...")
app.run_polling() 
from telegram.ext import Application, CommandHandler

TOKEN = "8845487590:AAGVnDuUfq5llIh3FUEujpn2Q_t3DzlGQCE"

async def start(update, context):
    await update.message.reply_text("Hello! Crypto Father Bot online hai.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot start ho raha hai...")
app.run_polling()
