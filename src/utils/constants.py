import emoji

# Messages
MENU = '''
Выберите действие👇
'''
CONTACT = '''
📞Введите номер телефона в формате +7(xxx)xxxxxxx или нажмите на кнопку "Отправить контакт"
'''
MAIL = '''
📧Введите адрес электронной почты:
'''
AGREEMENT = '''
Чтобы начать пользоваться ботом необходимо дать согласие на обработку персональных данных.
'''
DISAGREEMENT = '''
К сожалению, без согласия вы не сможете пользоваться ботом :(
'''
FOOD_ADVICES = '''
Получите советы по питанию👇
'''
RATION = '''
Какова ваша цель?👇
'''
ACTIVITY_LEVEL = '''
Расскажите о своей активности. 

Примеры: 
1. Хожу в зал и занимаюсь силовыми тренировками 3 раза в неделю по 2 часа в день.
2. Занимаюсь спортивной ходьбой каждый день.
3. Занимаюсь йогой.
4. Бегаю по утрам по 5 км.
и тд.
'''
PREFERENCIES = '''
Есть ли у вас какие-либо аллергии или непереносимости?
'''
BUDGET = '''
Бюджет. Сколько вы можете тратить в тыс. на питание в месяц? 
'''
FOOD_CALORIES = '''
Введите название продукта или блюда:
'''
FOOD_WEIGHT = '''
Введите массу продукта или блюда в граммах:
'''
REPLACE_FOOD = '''
Напиши название своего любимого вредного продукта, и я предложу тебе здоровую замену👇
'''
ANKET_AGE = '''
Введите ваш возраст
'''
ANKET_GENDER = '''
Введите ваш пол
'''
ANKET_GROWTH = '''
Введите ваш рост в см.
'''
ANKET_WEIGHT = '''
Введите ваш вес в кг
'''
WICKNESSESS = '''
Есть ли у вас какие-то ограничения по здоровью? Напишите про них
'''
EXERCISE_PREFERENCIES = '''
Какие у вас предпочтения по упражнениям? Что вам нравится или наоборот неприязно?
'''
FREE_TIME = '''
Сколько времени вы можете уделять тренировкам? (например, 3 дня в неделю по 1 часу и т.п)
'''
WORKOUT_GOAL = '''
Какова ваша цель?👇
'''

# Buttons
BTN_AGREEMENT_YES = 'Даю согласие👌'
CALLBACK_BTN_AGREEMENT_YES = 'btn_agreement_yes'
BTN_AGREEMENT_NO = 'Нет🙅‍♂️'
CALLBACK_BTN_AGREEMENT_NO = 'btn_agreement_no'

###############
BTN_BACK_TO_MENU = 'Назад↩'
CALLBACK_BTN_BACK_TO_MENU = 'btn_back_to_menu'

###############

###############
BTN_FOOD_ADVICES = 'Рекомендации по питанию🍴'

CALLBACK_BTN_FOOD_ADVICES = 'btn_food_advices'

###############
BTN_TRAINING_PROGRAMS = 'Составить программу тренировок🏋'
CALLBACK_BTN_TRAINING_PROGRAMS = 'btn_training_programs'

###############
BTN_CALORIFIC_CALCULATOR = 'Калькулятор калорий🍲'
CALLBACK_BTN_CALORIFIC_CALCULATOR = 'btn_calorific_calculator'

###############
BTN_EXERCISES_GUIDES = 'Гайд по упражнениям📔'
CALLBACK_BTN_EXERCISES_GUIDES = 'btn_exercises_guides'

###############
BTN_BODY_PARAMETERS = 'Мои параметры🧍'
CALLBACK_BTN_BODY_PARAMETERS = 'btn_body_parameters'

###############
BTN_HELP = 'Помощь❓'
CALLBACK_BTN_HELP = 'btn_help'

###############

BTN_BACK_TO_FOOD_ADVICES = 'Назад↩'
CALLBACK_BTN_BACK_TO_FOOD_ADVICES = 'btn_back_to_food_advices'

BTN_FOOD_CALORIES = 'Калорийность продукта🥞'
CALLBACK_BTN_FOOD_CALORIES = 'btn_food_calories'

BTN_FOOD_PLAN = 'Составить план питания🗓'
CALLBACK_BTN_FOOD_PLAN = 'btn_food_plan'

BTN_RECIPES = 'Примеры рецептов🗒'
CALLBACK_BTN_RECIPES = 'btn_recipes'


##########
BTN_BACK_TO_GOAL = 'Назад↩'
CALLBACK_BTN_BACK_TO_GOAL = 'btn_back_to_goal'

BTN_LOSE_WEIGHT = 'Хочу похудеть'
CALLBACK_BTN_LOSE_WEIGHT = 'btn_goal_lose_weight'

BTN_MUSCULAR_WEIGHT = 'Набрать мышечную массу'
CALLBACK_BTN_MUSCULAR_WEIGHT = 'btn_goal_muscular_weight'

BTN_MAINTAIN_FIT = 'Поддерживать форму'
CALLBACK_BTN_MAINTAIN_FIT = 'btn_goal_maintain_fit'


################
BTN_BACK_TO_ACTIVITY_LEVEL = 'Назад↩'
CALLBACK_BTN_BACK_TO_ACTIVITY_LEVEL = 'btn_back_to_activity_level'


################
BTN_BACK_TO_PREFERENCIES = 'Назад↩'
CALLBACK_BTN_BACK_TO_PREFERENCIES = 'btn_back_to_preferencies'

BTN_BACK_TO_FOOD_NAME = 'Назад↩'
CALLBACK_BTN_BACK_TO_FOOD_NAME ='btn_back_to_food_name'

################
BTN_BACK_TO_ANKET = 'Назад↩'
CALLBACK_BTN_BACK_TO_ANKET = 'btn_back_to_anket'

BTN_AGE = 'Возраст'
CALLBACK_BTN_AGE = 'btn_age'

BTN_GENDER = 'Пол'
CALLBACK_BTN_GENDER = 'btn_gender'

BTN_GROWTH = 'Рост'
CALLBACK_BTN_GROWTH = 'btn_growth'

BTN_WEIGHT = 'Вес'
CALLBACK_BTN_WEIGHT = 'btn_weight'


###########
BTN_WORKOUT_LOSE_WEIGHT = 'Хочу похудеть'
CALLBACK_BTN_WORKOUT_LOSE_WEIGHT = 'btn_workout_lose_weight'

BTN_WORKOUT_MUSCULAR_WEIGHT = 'Набрать мышечную массу'
CALLBACK_BTN_WORKOUT_MUSCULAR_WEIGHT = 'btn_workout_muscular_weight'

BTN_WORKOUT_MAINTAIN_FIT = 'Поддерживать форму'
CALLBACK_BTN_WORKOUT_MAINTAIN_FIT = 'btn_workout_maintain_fit'