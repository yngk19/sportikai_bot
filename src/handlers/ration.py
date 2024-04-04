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
from fsm import states
from utils.gemini import GetPlan


router = Router()  

@router.callback_query(F.data == constants.CALLBACK_BTN_FOOD_PLAN)
async def Ration(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await Goal(callback, state)

async def Goal(callback: CallbackQuery, state: FSMContext):
  await state.set_state(states.RationPlan.Goal)
  file_ids = []
  menuImage = FSInputFile(config.MEDIA_PATH + "menu.jpg")
  result = await callback.message.answer_photo(
    menuImage,
    caption=constants.RATION,
    reply_markup=keyboards.GoalKeyboard()
  )
  file_ids.append(result.photo[-1].file_id)

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_GOAL)
async def BackToGoal(callback: CallbackQuery, state: FSMContext):
  await state.set_state(states.RationPlan.Goal)
  await Goal(callback, state)

@router.callback_query(StateFilter(states.RationPlan.Goal), lambda c: c.data.startswith("btn_goal"))
async def GoalCallback(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  if callback.data.split('_')[2] == 'lose':
    await state.update_data(goal='Похудеть')
  elif callback.data.split('_')[2] == 'muscular':
    await state.update_data(goal='Набрать мышечную массу')
  else:
    await state.update_data(goal='Поддерживать форму')
  await ActivityLevel(callback, state)

async def ActivityLevel(callback: CallbackQuery, state: FSMContext):
  await state.set_state(states.RationPlan.ActivityLevel)
  await callback.message.answer(
    text=constants.ACTIVITY_LEVEL,
    reply_markup=keyboards.ActivityLevelKeyboard()
  )

@router.message(StateFilter(states.RationPlan.ActivityLevel))
async def ActivityLevelCallback(message: Message, state: FSMContext):
  await state.update_data(activity_level=message.text)
  await Preferencies(message, state)

async def Preferencies(message: Message, state: FSMContext):
  await state.set_state(states.RationPlan.Preferencies)
  await message.answer(
    text=constants.PREFERENCIES,
    reply_markup=keyboards.PreferenciesKeyboard()
  )

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_ACTIVITY_LEVEL)
async def BackToActivityLevel(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await state.set_state(states.RationPlan.ActivityLevel) 
  await ActivityLevel(callback.message, state)

@router.message(StateFilter(states.RationPlan.Preferencies))
async def PreferenciesCallback(message: Message, state: FSMContext):
  await state.update_data(preferencies=message.text)
  await Budget(message, state)

async def Budget(message: Message, state: FSMContext):
  await state.set_state(states.RationPlan.Budget)
  await message.answer(
    text=constants.BUDGET,
    reply_markup=keyboards.BudgetKeyboard()
  )

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_PREFERENCIES)
async def BackToActivityLevel(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  await state.set_state(states.RationPlan.Preferencies) 
  await Preferencies(message, state)

@router.message(StateFilter(states.RationPlan.Budget))
async def PreferenciesCallback(message: Message, state: FSMContext):
  await state.update_data(budget=message.text)
  await state.set_state(state=None)
  await WaitForResult(message, state)

async def WaitForResult(message: Message, state: FSMContext):
  text = '''
  Sportik готовит ответ. Еще несколько секунд...
  '''
  await message.answer(
    text=text
  )
  await RationPlanResult(message, state)

async def RationPlanResult(message: Message, state: FSMContext):
  userData = await state.get_data()
  goal = userData['goal']
  activityLevel = userData['activity_level']
  preferencies = userData['preferencies']
  budget = userData['budget']
  prompt = f'''
  Составь рацион питания на месяц с учетом моих параметров, посчитай общую калорийность. Сообщение должно не превышать 3000 символов. Также вот мои данные:
  1. Цель: {goal}
  2. Уровень активности: {activityLevel}
  3. Пищевые предпочтения: {preferencies} 
  4. Бюджет: {budget}
  '''
  promptResult = GetPlan(prompt)
  text = ''
  if promptResult.status_code == 400:
      text = '''
      Извините, технические неполадки на сервере. Повторите попытку позднее.
      '''
      await state.update_data(ration_plan='')
  else:
      text = promptResult.json()['candidates'][0]['content']['parts'][0]['text'].replace('*', '- ')
      await state.update_data(ration_plan=text)

  await message.answer(
      text=text,
      reply_markup=keyboards.FoodAdvicesKeyboard()
  )
