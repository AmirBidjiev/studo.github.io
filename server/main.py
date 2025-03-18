import asyncio
from config import *
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Открыть WebApp", web_app=WebAppInfo(url="https://amirbidjiev.github.io/studo.github.io/client/index.html"))],
        [KeyboardButton(text="Просто кнопка")]
    ], resize_keyboard=True)
    await message.answer("Привет, я универсальный бот для помощи студентам. Здесь можно обмениваться записями лекций, семинаров, искать людей в свой старта, находить того, кто поможет с домашкой или проектом или наоборот - зарабатывать, помогая другим")
    await message.answer("Но сначала нужно зарегестрироваться:", reply_markup = kb)

@dp.message(F.web_app_data)
async def web_data_handler(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Получены данные из WebApp: {data}")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
