from telebot.states import State, StatesGroup


class RegistrateUser(StatesGroup):
    waiting_for_start: State = State()
    waiting_for_login: State = State()
    waiting_for_password: State = State()

class LanguageChanger(StatesGroup):
    language: State = State()