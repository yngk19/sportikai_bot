from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardBuilder
from utils import constants
import emoji

def MenuKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_FOOD_ADVICES, callback_data=constants.CALLBACK_BTN_FOOD_ADVICES))
	builder.add(InlineKeyboardButton(text=constants.BTN_TRAINING_PROGRAMS, callback_data=constants.CALLBACK_BTN_TRAINING_PROGRAMS))
	builder.add(InlineKeyboardButton(text=constants.BTN_CALORIFIC_CALCULATOR, callback_data=constants.CALLBACK_BTN_CALORIFIC_CALCULATOR))
	builder.add(InlineKeyboardButton(text=constants.BTN_EXERCISES_GUIDES, callback_data=constants.CALLBACK_BTN_EXERCISES_GUIDES))
	builder.add(InlineKeyboardButton(text=constants.BTN_BODY_PARAMETERS, callback_data=constants.CALLBACK_BTN_BODY_PARAMETERS))
	builder.adjust(1)
	return builder.as_markup()

def AgreementKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_AGREEMENT_YES, callback_data=constants.CALLBACK_BTN_AGREEMENT_YES))
	builder.add(InlineKeyboardButton(text=constants.BTN_AGREEMENT_NO, callback_data=constants.CALLBACK_BTN_AGREEMENT_NO))
	builder.adjust(2)
	return builder.as_markup()


def ContactKeyboard():
	builder = ReplyKeyboardBuilder()
	builder.row(KeyboardButton(text="Отправить контакт", request_contact=True))
	return builder.as_markup()

def FoodAdvicesKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_FOOD_PLAN, callback_data=constants.CALLBACK_BTN_FOOD_PLAN))
	builder.add(InlineKeyboardButton(text=constants.BTN_RECIPES, callback_data=constants.CALLBACK_BTN_RECIPES))
	builder.add(InlineKeyboardButton(text=constants.BTN_FOOD_CALORIES, callback_data=constants.CALLBACK_BTN_FOOD_CALORIES))
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_MENU, callback_data=constants.CALLBACK_BTN_BACK_TO_MENU))
	builder.adjust(1)
	return builder.as_markup()

def GoalKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_LOSE_WEIGHT, callback_data=constants.CALLBACK_BTN_LOSE_WEIGHT))
	builder.add(InlineKeyboardButton(text=constants.BTN_MUSCULAR_WEIGHT, callback_data=constants.CALLBACK_BTN_MUSCULAR_WEIGHT))
	builder.add(InlineKeyboardButton(text=constants.BTN_MAINTAIN_FIT, callback_data=constants.CALLBACK_BTN_MAINTAIN_FIT))
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_FOOD_ADVICES, callback_data=constants.CALLBACK_BTN_BACK_TO_FOOD_ADVICES))
	builder.adjust(1)
	return builder.as_markup()

def ActivityLevelKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_GOAL, callback_data=constants.CALLBACK_BTN_BACK_TO_GOAL))
	builder.adjust(1)
	return builder.as_markup()

def PreferenciesKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_ACTIVITY_LEVEL, callback_data=constants.CALLBACK_BTN_BACK_TO_ACTIVITY_LEVEL))
	builder.adjust(1)
	return builder.as_markup()

def BudgetKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_PREFERENCIES, callback_data=constants.CALLBACK_BTN_BACK_TO_PREFERENCIES))
	builder.adjust(1)
	return builder.as_markup()

def FoodCaloriesKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_FOOD_ADVICES, callback_data=constants.CALLBACK_BTN_BACK_TO_FOOD_ADVICES))
	builder.adjust(1)
	return builder.as_markup()

def FoodWeightKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_FOOD_NAME, callback_data=constants.CALLBACK_BTN_BACK_TO_FOOD_NAME))
	builder.adjust(1)
	return builder.as_markup()

def AnketKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_AGE, callback_data=constants.CALLBACK_BTN_AGE))
	builder.add(InlineKeyboardButton(text=constants.BTN_GENDER, callback_data=constants.CALLBACK_BTN_GENDER))
	builder.add(InlineKeyboardButton(text=constants.BTN_GROWTH, callback_data=constants.CALLBACK_BTN_GROWTH))
	builder.add(InlineKeyboardButton(text=constants.BTN_WEIGHT, callback_data=constants.CALLBACK_BTN_WEIGHT))	
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_MENU, callback_data=constants.CALLBACK_BTN_BACK_TO_MENU))
	builder.adjust(1)
	return builder.as_markup()

def BackToAnketKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_ANKET, callback_data=constants.CALLBACK_BTN_BACK_TO_ANKET))
	builder.adjust(1)
	return builder.as_markup()

def BackToMenu():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_MENU, callback_data=constants.CALLBACK_BTN_BACK_TO_MENU))
	builder.adjust(1)
	return builder.as_markup()

def WorkoutProgramsKeyboard():
	builder = InlineKeyboardBuilder()
	builder.add(InlineKeyboardButton(text=constants.BTN_WORKOUT_LOSE_WEIGHT, callback_data=constants.CALLBACK_BTN_WORKOUT_LOSE_WEIGHT))
	builder.add(InlineKeyboardButton(text=constants.BTN_WORKOUT_MUSCULAR_WEIGHT, callback_data=constants.CALLBACK_BTN_WORKOUT_MUSCULAR_WEIGHT))
	builder.add(InlineKeyboardButton(text=constants.BTN_WORKOUT_MAINTAIN_FIT, callback_data=constants.CALLBACK_BTN_WORKOUT_MAINTAIN_FIT))
	builder.add(InlineKeyboardButton(text=constants.BTN_BACK_TO_MENU, callback_data=constants.CALLBACK_BTN_BACK_TO_MENU))
	builder.adjust(1)
	return builder.as_markup()