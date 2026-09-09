from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from googletrans import Translator

translator = Translator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga matn yuboring, men uni tarjima qilib beraman.")

async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    detected = translator.detect(user_text).lang
    target = 'en' if detected == 'uz' else 'uz'
    
    translated = translator.translate(user_text, dest=target)
    await update.message.reply_text(translated.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token("8758662304:AAEbojfBYTUVAf_BSTqQu5EH7nmryuLjgQI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))
    app.run_polling()
