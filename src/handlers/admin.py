import asyncio
import aiogram
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils import constants
from keyboards import keyboards
from config import config


startpress = []
rationplanget = []
foodcaloriesget = []
workoutprogramget = []
recipesget = []
caloriescalculatorget = []
ankentget = []
users = []



router = Router()  

@router.message(Command("admin"))
async def FoodAdvices(message: Message, state: FSMContext):
  if message.from_user.id == int(config.BOT_ADMIN_TGID):
    text = f'''
    Статистика бота:

    Всего пользователей: {len(users)} 
    Нажатий на кнопку старт: {len(startpress)}
    
    Питание:
      План питания запрашивали: {len(rationplanget)} раз
      Калорийность продукта запрашивали: {len(foodcaloriesget)} раз 
      Примеры рецептов запрашивали: {len(recipesget)} раз
    
    Тренировки:
      Программу тренировок запрашивали: {len(workoutprogramget)} раз
    
    Калькулятор калорий:
      Запрашивали суточную норму калорий: {len(caloriescalculatorget)} раз

    Профиль:
      Данные о себе меняли: {len(ankentget)} раз
    '''
    await message.answer(
      text=text
    )
  else:
    text='Эта команда доступна только администраторам'
    await message.answer(
      text=text
    )


