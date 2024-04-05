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
from handlers.admin import ankentget


router = Router()  

@router.callback_query(F.data == constants.CALLBACK_BTN_BODY_PARAMETERS)
async def Parameters(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(state=None)
	await UserInfo(callback.message, state)

async def UserInfo(message: Message, state: FSMContext):
	await state.set_state(state=None)
	userData = await state.get_data()
	age = userData['age']
	if age == '':
		age = 'пусто'
	gender = userData['gender']
	if gender == '':
		gender = 'пусто'
	growth = userData['growth']
	if growth == '':
		growth = 'пусто'
	weight = userData['weight']
	if weight == '':
		weight = 'пусто'
	firstName = userData['first_name']
	text = f'''
	Мои данные:

	Пользователь: {firstName} 
	Возраст: {age}
	Пол: {gender}
	Рост: {growth}
	Вес: {weight}

	Редактируйте данные, нажимая на кнопки ниже
	'''
	await message.answer(
		text=text,
    	reply_markup=keyboards.AnketKeyboard()
	)

@router.callback_query(F.data == constants.CALLBACK_BTN_BACK_TO_ANKET)
async def BackToAnket(callback: CallbackQuery, state: FSMContext):
	await Parameters(callback, state)


@router.callback_query(F.data == constants.CALLBACK_BTN_AGE)
async def AgeCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(states.Anket.Age)
	await callback.message.answer(
		text=constants.ANKET_AGE,
    	reply_markup=keyboards.BackToAnketKeyboard()
	)

@router.message(StateFilter(states.Anket.Age))
async def Age(message: Message, state: FSMContext):
	await state.update_data(age=message.text)
	ankentget.append(1)
	await UserInfo(message, state)

@router.callback_query(F.data == constants.CALLBACK_BTN_GENDER)
async def GenderCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(states.Anket.Gender)
	await callback.message.answer(
		text=constants.ANKET_GENDER,
    	reply_markup=keyboards.BackToAnketKeyboard()
	)

@router.message(StateFilter(states.Anket.Gender))
async def Gender(message: Message, state: FSMContext):
	await state.update_data(gender=message.text)
	ankentget.append(1)
	await UserInfo(message, state)

@router.callback_query(F.data == constants.CALLBACK_BTN_GROWTH)
async def GrowthCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(states.Anket.Growth)
	await callback.message.answer(
		text=constants.ANKET_GROWTH,
    	reply_markup=keyboards.BackToAnketKeyboard()
	)

@router.message(StateFilter(states.Anket.Growth))
async def Growth(message: Message, state: FSMContext):
	await state.update_data(growth=message.text)
	ankentget.append(1)
	await UserInfo(message, state)

@router.callback_query(F.data == constants.CALLBACK_BTN_WEIGHT)
async def WeightCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(states.Anket.Weight)
	await callback.message.answer(
		text=constants.ANKET_WEIGHT,
    	reply_markup=keyboards.BackToAnketKeyboard()
	)

@router.message(StateFilter(states.Anket.Weight))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(weight=message.text)
	await UserInfo(message, state)