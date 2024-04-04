import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile, CallbackQuery
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.methods.set_my_commands import SetMyCommands
import redis.asyncio as redis

from config import config
from utils.setupcommands import SetupCommands
from handlers import start, foodadvices, ration, recipes, foodcalories, myparameters, caloriescalculator, workoutprogram


if config.USE_CACHE:
    storage = RedisStorage.from_url(url=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/0")
    dp = Dispatcher(storage=storage)
else:
    dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.BOT_TOKEN)

    await bot.set_my_commands(commands=SetupCommands())
    dp.include_router(start.router)
    dp.include_router(foodadvices.router)
    dp.include_router(ration.router)
    dp.include_router(recipes.router)
    dp.include_router(foodcalories.router)
    dp.include_router(myparameters.router)
    dp.include_router(caloriescalculator.router)
    dp.include_router(workoutprogram.router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())