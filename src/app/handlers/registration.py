from src.app.handlers.states import RegistrateUser
from src.app.repository.CRUD import registration
from telebot.states.asyncio.context import StateContext
from telebot import types
from src.bot_instance import bot


async def handle_registration(bot, user_id, state: StateContext):
    text = "Введите логин. Логин должен иметь от 6 до 32 символов включительно. И не содержать спецсимволов: !@#$%^&*()-=\\/*"
    await bot.send_message(chat_id=user_id, text=text)
    await state.set(RegistrateUser.waiting_for_login)


@bot.message_handler(state=RegistrateUser.waiting_for_login)
async def handle_login_prompt(message: types.Message, state: StateContext):
    text = "Введите пароль. Пароль должен иметь от 6 до 32 символов включительно. И не содержать спецсимволов: !@#$%^&*()-=\\/*"
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
        username = data.get("login")
        password = data.get("password")

        await state.delete()
    success = await registration.register_user(
        telegram_id=message.from_user.id,
        name=message.from_user.first_name,
        language=message.from_user.language_code,
        username=data.get("login"),
        password=data.get("password")
    )
    text = successful if success else error
    await bot.send_message(message.from_user.id, text)
    await state.delete()



@bot.message_handler(state="*", commands=["cancel"])
async def handle_any_state(bot, message: types.Message, state: StateContext):
    """
    Handles cancellation of any state.

    Args:
        bot: Telegram bot instance.
        message: Incoming message object.
        state: Context of the current state.

    Returns:
        None
    """
    await state.delete()
    # text = TRAN.return_translated_text("cancel_command", id_=message.from_user.id)
    text = ""
    await bot.send_message(message.chat.id, text)