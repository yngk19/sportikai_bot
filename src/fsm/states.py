from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State



class RationPlan(StatesGroup):
    Goal = State()
    ActivityLevel = State()
    Preferencies = State()
    Budget = State()

    
class FoodCalories(StatesGroup):
    FoodName = State()
    FoodWeight = State()

class Anket(StatesGroup):
    Age = State()
    Gender = State()
    Growth = State()
    Weight = State()

class Calculator(StatesGroup):
    ActivityLevel = State()
    Age = State()
    Gender = State()
    Growth = State()
    Weight = State()

class WorkoutPrograms(StatesGroup):
    ActivityLevel = State()
    Age = State()
    Gender = State()
    Growth = State()
    Weight = State()
    Goal = State()
    Preferencies = State()
    Wicknessess = State()
    FreeTime = State()

