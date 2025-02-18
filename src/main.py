import asyncio
from src.app.handlers.handlers import register_handlers
from src.bot_instance import bot
from src.app.keyboards.keyboards import keyboard

async def start_bot():
    register_handlers(bot)
    await bot.polling()


async def main():
    await keyboard.set_menu()
    await start_bot()

if __name__ == "__main__":
    asyncio.run(main())