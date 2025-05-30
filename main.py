from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Ваш токен Telegram бота
import os
BOT_TOKEN = os.getenv("8150614057:AAF6qM6JXUsTpAs7-g-pGI7zIVdLXCu6k4Y")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "Приветствую!\n"
        "Это бот обратной связи. Сообщения любого формата приветствуются.\n\n"
        "Связь с разработчиком гарантирована!"
    )
    await update.message.reply_text(welcome_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Здесь можно реализовать логирование сообщений или пересылку админу
    await update.message.reply_text("Спасибо за сообщение! Мы свяжемся с вами при необходимости.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("Бот запущен...")
    app.run_polling()
