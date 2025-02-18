from telebot import types
from telebot.states.asyncio.context import StateContext
from src.app.repository.CRUD import registration
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