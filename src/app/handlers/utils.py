from telebot import types
from telebot.states.asyncio import StateContext


async def handle_start(bot, user_id, state: StateContext):
    is_registrated = True
    # is_registrated = get_user_by_telegram_id(user_id)
    if is_registrated:
        bot.send_message()
