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

@router.callback_query(F.data == constants.CALLBACK_BTN_TRAINING_PROGRAMS)
async def WorkoutProgramsCallback(callback: CallbackQuery, state: FSMContext):
	await callback.message.delete()
	await state.set_state(state=None)
	await WorkoutPrograms(callback.message, state)

async def WorkoutPrograms(message: Message, state: FSMContext):
	userData = await state.get_data()
	age = userData['age']
	if age == '':
		await state.set_state(states.WorkoutPrograms.Age)
		await message.answer(
			text=constants.ANKET_AGE,
			reply_markup=keyboards.BackToMenu()
		)
		return
	gender = userData['gender']
	if userData['gender'] == '':
		await state.set_state(states.WorkoutPrograms.Gender)
		await message.answer(
			text=constants.ANKET_GENDER,
			reply_markup=keyboards.BackToMenu()
		)
		return
	growth = userData['growth']
	if growth == '':
		await state.set_state(states.WorkoutPrograms.Growth)
		await message.answer(
			text=constants.ANKET_GROWTH,
			reply_markup=keyboards.BackToMenu()
		)
		return
	weight = userData['weight']
	if weight == '':
		await state.set_state(states.WorkoutPrograms.Weight)
		await message.answer(
			text=constants.ANKET_WEIGHT,
			reply_markup=keyboards.BackToMenu()
		)
		return
	goal = userData['goal']
	if goal == '':
		await state.set_state(states.WorkoutPrograms.Goal)
		await message.answer(
			text=constants.WORKOUT_GOAL,
			reply_markup=keyboards.WorkoutProgramsKeyboard()
		)
		return
	exercisePreferencies = userData['exercise_preferencies']
	if exercisePreferencies == '':
		await state.set_state(states.WorkoutPrograms.Preferencies)
		await message.answer(
			text=constants.EXERCISE_PREFERENCIES,
			reply_markup=keyboards.BackToMenu()
		)
		return
	wicknessess = userData['wicknessess']
	if wicknessess == '':
		await state.set_state(states.WorkoutPrograms.Wicknessess)
		await message.answer(
			text=constants.WICKNESSESS,
			reply_markup=keyboards.BackToMenu()
		)
		return
	freetime = userData['freetime']
	if freetime == '':
		await state.set_state(states.WorkoutPrograms.FreeTime)
		await message.answer(
			text=constants.FREE_TIME,
			reply_markup=keyboards.BackToMenu()
		)
		return
	await WaitForProgram(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Age))
async def Age(message: Message, state: FSMContext):
	await state.update_data(age=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Gender))
async def Gender(message: Message, state: FSMContext):
	await state.update_data(gender=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Growth))
async def Growth(message: Message, state: FSMContext):
	await state.update_data(growth=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Weight))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(weight=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Wicknessess))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(wicknessess=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.FreeTime))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(freetime=message.text)
	await WorkoutPrograms(message, state)

@router.message(StateFilter(states.WorkoutPrograms.Preferencies))
async def Weight(message: Message, state: FSMContext):
	await state.update_data(exercise_preferencies=message.text)
	await WorkoutPrograms(message, state)

@router.callback_query(StateFilter(states.WorkoutPrograms.Goal), lambda c: c.data.startswith("btn_workout"))
async def WorkoutGoalCallback(callback: CallbackQuery, state: FSMContext):
  await callback.message.delete()
  if callback.data.split('_')[2] == 'lose':
    await state.update_data(goal='Похудеть')
  elif callback.data.split('_')[2] == 'muscular':
    await state.update_data(goal='Набрать мышечную массу')
  else:
    await state.update_data(goal='Поддерживать форму')
  await WorkoutPrograms(callback.message, state)


async def WaitForProgram(message: Message, state: FSMContext):
	text = '''
 	Sportik готовит ответ. Еще несколько секунд...
	'''
	await message.answer(
		text=text
  	)
	await Program(message, state)

async def Program(message: Message, state: FSMContext):
	userData = await state.get_data()
	age = userData['age']
	gender = userData['gender']
	growth = userData['growth']
	weight = userData['weight']
	goal = userData['goal']
	preferencies = userData['exercise_preferencies']
	freetime = userData['freetime']
	wicknessess = userData['wicknessess']
	prompt = f'''
  	Ты - мой фитнес-тренер. Составь для меня программу тренировок на неделю с учетом моих физических параметров и личных предпочтений:
	1. Возраст: {age}
	2. Пол: {gender}
	3. Рост: {growth}
	4. Вес: {weight}
	5. Цель: {goal}
	6. Предпочтения по упражнениям: {preferencies}
	7. Ограничения по здоровью: {wicknessess}
	8. Могу уделять тренировкам: {freetime}
  	'''
	promptResult = GetPlan(prompt)
	text = ''
	if promptResult.status_code == 400:
		text = '''
		Извините, технические неполадки на сервере. Повторите попытку позднее.
		'''
		await state.update_data(workout_program='')
	else:
		text = promptResult.json()['candidates'][0]['content']['parts'][0]['text'].replace('*', '- ')
		await state.update_data(workout_program=text)
	await message.answer(
  	  text=text,
      reply_markup=keyboards.MenuKeyboard()
  	)

