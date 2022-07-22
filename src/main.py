from core.config import app_config

from pathlib import Path
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, File, Message

from speechkit.google import GoogleAPI

bot = Bot(token=app_config.BOT_TOKEN)
dp = Dispatcher(bot)


async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

    return GoogleAPI.recognize(f"{path}/{file_name}")


@dp.message_handler(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "tmp/voices"

    recognized_words = await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)
    await message.reply(recognized_words)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
