import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")  # Вставь свой токен в файл .env
if not TOKEN:
    raise ValueError("Токен не найден! Убедитесь, что он есть в файле .env.")
    
GROUP_ID = -4663207006  # ID вашей группы

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Принимаем любое сообщение от пользователя
@dp.message_handler()
async def forward_to_group(message: Message):
    text = f"📩 Новое анонимное сообщение:\n\n{message.text}"
    await bot.send_message(GROUP_ID, text)

# Основная асинхронная функция
async def main():
    logging.basicConfig(level=logging.INFO)  # Логирование для отслеживания ошибок
    await dp.start_polling()

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
