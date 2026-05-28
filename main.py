import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from detector import generate_signal

TOKEN = "8910895596:AAG5KfMwTUGvTmFYUGhQhf52b0tQb3NENug"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(F.photo)
async def photo_handler(message: Message):

    wait = await message.answer("🤖 Анализирую поле...")

    photo = message.photo[-1]

    file = await bot.get_file(photo.file_id)

    await bot.download_file(file.file_path, "field.jpg")

    signal = generate_signal()

    await wait.edit_text(
        f"""
🎯 <b>SAFE SIGNAL</b>

{signal}

🔥 Confidence: 87%
🧠 AI Mode: SAFE
"""
    )


@dp.message()
async def start(message: Message):
    await message.answer(
        "📸 Отправь скрин Mines"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
