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
from handlers.admin import foodcaloriesget


router = Router()  

@router.callback_query(F.data == constants.CALLBACK_BTN_FOOD_CALORIES)
async def FoodCalories(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(states.FoodCalories.FoodName)
	await callback.message.answer(
		text=constants.FOOD_CALORIES,
    	reply_markup=keyboards.FoodCaloriesKeyboard()
	)

@router.message(StateFilter(states.FoodCalories.FoodName))
async def FoodName(message: Message, state: FSMContext):
	await state.update_data(food_name=message.text)
	await state.set_state(states.FoodCalories.FoodWeight)
	await message.answer(
		text=constants.FOOD_WEIGHT,
    	reply_markup=keyboards.FoodWeightKeyboard()
	)

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_FOOD_NAME)
async def BackToFoodWeight(callback: CallbackQuery, state: FSMContext):
	await FoodCalories(callback, state)

@router.message(StateFilter(states.FoodCalories.FoodWeight))
async def FoodWeight(message: Message, state: FSMContext):
	await state.update_data(food_weight=message.text)
	await state.set_state(state=None)
	await WaitForFoodCalories(message, state)


async def WaitForFoodCalories(message: Message, state: FSMContext):
	text = '''
 	Sportik готовит ответ. Еще несколько секунд...
	'''
	await message.answer(
		text=text
  	)
	await Calories(message, state)

async def Calories(message: Message, state: FSMContext):
	foodcaloriesget.append(1)
	userData = await state.get_data()
	foodName = userData['food_name']
	FoodWeight = userData['food_weight']
	prompt = f'''
  	Ты - калькулятор калорий. Посчитай количество калорий в продукте.
  	1. Название продукта: {foodName}
  	2. Масса продукта: {FoodWeight}
  	'''
	promptResult = GetPlan(prompt)
	text = ''
	if promptResult.status_code == 400:
  	  text = '''
  	  Извините, технические неполадки на сервере. Повторите попытку позднее.
  	  '''
	else:
		text = promptResult.json()['candidates'][0]['content']['parts'][0]['text'].replace('*', '- ')

	await message.answer(
  	  text=text,
      reply_markup=keyboards.FoodAdvicesKeyboard()
  	)





