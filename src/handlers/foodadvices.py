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


router = Router()  

@router.callback_query(F.data == constants.CALLBACK_BTN_FOOD_ADVICES)
async def FoodAdvices(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  file_ids = []
  menuImage = FSInputFile(config.MEDIA_PATH + "menu.jpg")
  result = await callback.message.answer_photo(
    menuImage,
    caption=constants.FOOD_ADVICES,
    reply_markup=keyboards.FoodAdvicesKeyboard()
  )
  file_ids.append(result.photo[-1].file_id)


@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_FOOD_ADVICES)
async def BackToFoodAdvices(callback: CallbackQuery, state: FSMContext):
  await FoodAdvices(callback, state)