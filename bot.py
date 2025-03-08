import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

load_dotenv()
# 🔑 Вставьте свой токен
TOKEN = "7530075380:AAHW37SyfGCu6kPJnZHLgVqBLeUElYgSqSs"
GROUP_ID = -4663207006  # ID вашей группы

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Принимаем любое сообщение от пользователя
@dp.message()
async def forward_to_group(message: Message):
    text = f"📩 Новое анонимное сообщение:\n\n{message.text}"
    await bot.send_message(GROUP_ID, text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
