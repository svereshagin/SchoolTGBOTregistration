from src.app.handlers.states import RegistrateUser
from src.app.repository.models import Student, Credential, Profile
from src.app.repository.CRUD import registration
from telebot.states.asyncio.context import StateContext
from telebot import types
from src.bot_instance import bot

async def handle_registration(bot, user_id, state: StateContext):
    text = "write login"
    await bot.send_message(chat_id=user_id, text=text)
    await state.set(RegistrateUser.waiting_for_login)


@bot.message_handler(state=RegistrateUser.waiting_for_login)
async def handle_login_prompt(message: types.Message, state: StateContext):
    text = "write password"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await state.add_data(login=message.text)
    await state.set(RegistrateUser.waiting_for_password)


@bot.message_handler(state=RegistrateUser.waiting_for_password)
async def handle_password_prompt(message: types.Message, state: StateContext):
    """Обработчик ввода пароля и финального сохранения данных."""
    successful = "Вы успешно зарегистрированы!"
    error = "Похоже, что вы уже зарегестрированы, операция будет прервана."
    await state.add_data(password=message.text)

    async with state.data() as data:
        success = await registration.register_user(
            telegram_id=message.from_user.id,
            name=message.from_user.first_name,
            language=message.from_user.language_code,
            username=data.get("login"),
            password=data.get("password")
        )

    text = successful if success else error
    await bot.send_message(message.from_user.id, text)