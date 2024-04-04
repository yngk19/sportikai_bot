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

@router.callback_query(F.data == constants.CALLBACK_BTN_CALORIFIC_CALCULATOR)
async def CaloriesCalculatorCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(state=None)
	await CaloriesCalculator(callback.message, state)

async def CaloriesCalculator(message: Message, state: FSMContext):
	userData = await state.get_data()
	age = userData['age']
	if age == '':
		await state.set_state(states.Calculator.Age)
		await message.answer(
			text=constants.ANKET_AGE,
			reply_markup=keyboards.BackToMenu()
		)
		return
	gender = userData['gender']
	if userData['gender'] == '':
		await state.set_state(states.Calculator.Gender)
		await message.answer(
			text=constants.ANKET_GENDER,
			reply_markup=keyboards.BackToMenu()
		)
		return
	growth = userData['growth']
	if growth == '':
		await state.set_state(states.Calculator.Growth)
		await message.answer(
			text=constants.ANKET_GROWTH,
			reply_markup=keyboards.BackToMenu()
		)
		return
	weight = userData['weight']
	if weight == '':
		await state.set_state(states.Calculator.Weight)
		await message.answer(
			text=constants.ANKET_WEIGHT,
			reply_markup=keyboards.BackToMenu()
		)
		return
	activityLevel = userData['activity_level']
	if activityLevel == '':
		await state.set_state(states.Calculator.ActivityLevel)
		await message.answer(
			text=constants.ACTIVITY_LEVEL,
			reply_markup=keyboards.BackToMenu()
		)
		return
	await WaitForCalories(message, state)

@router.message(StateFilter(states.Calculator.Age))
async def Age(message: Message, state: FSMContext):
	await state.update_data(age=message.text)
	await CaloriesCalculator(message, state)

@router.message(StateFilter(states.Calculator.Gender))
async def Gender(message: Message, state: FSMContext):
	await state.update_data(gender=message.text)
	await CaloriesCalculator(message, state)

@router.message(StateFilter(states.Calculator.Growth))
async def Growth(message: Message, state: FSMContext):
	await state.update_data(growth=message.text)
	await CaloriesCalculator(message, state)

@router.message(StateFilter(states.Calculator.Weight))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(weight=message.text)
	await CaloriesCalculator(message, state)

@router.message(StateFilter(states.Calculator.ActivityLevel))
async def Age(message: Message, state: FSMContext):
	await state.update_data(activity_level=message.text)
	await CaloriesCalculator(message, state)


async def WaitForCalories(message: Message, state: FSMContext):
	text = '''
 	Sportik готовит ответ. Еще несколько секунд...
	'''
	await message.answer(
		text=text
  	)
	await Calories(message, state)

async def Calories(message: Message, state: FSMContext):
	userData = await state.get_data()
	age = userData['age']
	gender = userData['gender']
	growth = userData['growth']
	weight = userData['weight']
	activityLevel = userData['activity_level']
	prompt = f'''
  	Ты - калькулятор калорий. Посчитай мою суточную норму калорий.
	1. Возраст: {age}
	2. Пол: {gender}
	3. Рост: {growth}
	4. Вес: {weight}
	5. Уровень активности: {activityLevel}
  	'''
	promptResult = GetPlan(prompt)
	text = ''
	if promptResult.status_code == 400:
		text = '''
		Извините, технические неполадки на сервере. Повторите попытку позднее.
		'''
		await state.update_data(my_calories='')
	else:
		text = promptResult.json()['candidates'][0]['content']['parts'][0]['text'].replace('*', '- ')
		await state.update_data(my_calories=text)
	await message.answer(
  	  text=text,
      reply_markup=keyboards.MenuKeyboard()
  	)

