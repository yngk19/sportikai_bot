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

@router.callback_query(F.data == constants.CALLBACK_BTN_RECIPES)
async def WaitForRecipes(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	text = '''
 	Sportik готовит ответ. Еще несколько секунд...
	'''
	await callback.message.answer(
		text=text,
  	)
	await Recipes(callback, state)

async def Recipes(callback: CallbackQuery, state: FSMContext):
	#await callback.message.delete()
	prompt = f'''
  	Дай мне примеры рецептов здоровых блюд вместе с их калорийностью.
  	'''
	promptResult = GetPlan(prompt)
	text = ''
	if promptResult.status_code == 400:
  	  text = '''
  	  Извините, технические неполадки на сервере. Повторите попытку позднее.
  	  '''
	else:
		text = promptResult.json()['candidates'][0]['content']['parts'][0]['text'].replace('*', '- ')

	await callback.message.answer(
  	  text=text,
      reply_markup=keyboards.FoodAdvicesKeyboard()
  	)