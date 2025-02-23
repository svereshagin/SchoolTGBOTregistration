from telebot import types
from telebot.states.asyncio.context import StateContext
from src.app.repository.CRUD import registration, UserProfile
from src.app.handlers.registration import handle_registration


def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    async def start_handler(message: types.Message, state: StateContext):
        is_registrated = await registration.get_telegram_user_by_id(message.from_user.id)
        print(is_registrated)
        if not is_registrated:
            await bot.send_message(message.chat.id, "starts registration")
            await handle_registration(bot, message.from_user.id, state)
        else:
            await bot.send_message(message.chat.id, "u are registrated")

    @bot.message_handler(commands=["profile"])
    async def profile_handler(message: types.Message):
        user_id = message.from_user.id
        profiles = await UserProfile.get_profile(user_id)  # Вызов через класс
        print('OK')

        if not profiles:  # Проверяем, что profiles не None и не пустой список
            await bot.send_message(message.chat.id, "User  does not exist or has no profiles.")
        else:
            # Если найден хотя бы один профиль, обрабатываем его
            for profile in profiles:
                await bot.send_message(
                    message.chat.id,
                    f"Your profile:\nName: {profile['name']}\nLanguage: {profile['language']}\nUsername: {profile['username']}\nPassword: {profile['password']}"
                )

    @bot.message_handler(commands=["school"])
    async def profile_handler(message: types.Message):
        bot.send_message(message.chat.id, "https://www.google.com/")



    @bot.message_handler(commands=["lang"])
    async def change_language_handler(message: types.Message, state: StateContext):
        # await handle_command_selection(bot, message, state)
        pass