import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Получаем токен из переменной окружения (безопаснее)
BOT_TOKEN = ("8150614057:AAEqqWs0ERAolQE2j2CXu3eNVPYqcDhhVsA")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Приветствую! Оставь запрос (желательно одним сообщением)"
    )

# Обработчик всех остальных сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Запрос принят. Ожидайте ответ!")

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("Бот запущен...")
    app.run_polling()
