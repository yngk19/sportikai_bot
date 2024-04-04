from aiogram.types.bot_command import BotCommand
from typing import List


def SetupCommands() -> List:
	start_command = BotCommand(command='start', description='Начать работу с ботом')
	cancel_command = BotCommand(command='cancel', description='Отменить действие и вернуться в меню')
	help_command = BotCommand(command='help', description='Помощь')
	return [start_command, help_command, cancel_command]