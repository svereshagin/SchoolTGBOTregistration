import asyncio
from src.app.handlers.handlers import register_handlers
from src.bot_instance import bot


async def start_bot():
    register_handlers(bot)
    await bot.polling()


async def main():
    await start_bot()

if __name__ == "__main__":
    asyncio.run(main())