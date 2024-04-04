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

@router.message(Command("start"))
async def StartCommand(message: Message, state: FSMContext):
  userData = await state.get_data()
  try:
    agreement = userData['agreement']
    if not agreement:
      await Agreement(message, state)
      return
  except:
    await Agreement(message, state)
    return
  file_ids = []
  menuImage = FSInputFile(config.MEDIA_PATH + "menu.jpg")
  result = await message.answer_photo(
    menuImage,
    caption=constants.MENU,
    reply_markup=keyboards.MenuKeyboard()
  )
  file_ids.append(result.photo[-1].file_id)

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_MENU)
async def BackToMenu(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await StartCommand(callback.message, state)

async def Agreement(message: Message, state: FSMContext):
  await message.answer(
    text=constants.AGREEMENT,
    reply_markup=keyboards.AgreementKeyboard()
  )


@router.callback_query(F.data == constants.CALLBACK_BTN_AGREEMENT_YES)
async def AgreementCheck(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await state.update_data(agreement=True)
  await state.update_data(age='')
  await state.update_data(gender='')
  await state.update_data(growth='')
  await state.update_data(weight='')
  await state.update_data(username=callback.message.chat.username)
  await state.update_data(first_name=callback.message.chat.first_name)
  await state.update_data(activity_level='')
  await state.update_data(wicknessess='')
  await state.update_data(freetime='')
  await state.update_data(exercise_preferencies='')
  await state.update_data(goal='')
  await StartCommand(callback.message, state)

@router.callback_query(F.data == constants.CALLBACK_BTN_AGREEMENT_NO)
async def AgreementCheck(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await state.update_data(agreement=False)
  await Disagreement(callback.message, state)


async def Disagreement(message: Message, state: FSMContext):
  await state.update_data(agreement=False)
  await message.answer(
    text=constants.DISAGREEMENT,
  )