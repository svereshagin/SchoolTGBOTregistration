# import asyncio
# from src.app.keyboards.keyboards import keyboard
# from src.app.handlers.handlers import register_handlers
# from src.bot_instance import bot
# from src.app.repository.database import reset_database
#
# async def start_bot():
#     await keyboard.set_menu()
#     # await reset_database()
#     register_handlers(bot)
#     print("Bot is running...")
#     await bot.polling()
#
# async def main():
#     await reset_database()
#     await start_bot()
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from src.app.repository.database import init_db, SessionLocal
from src.app.repository.models import User

async def main():
    await init_db()  # Инициализация базы данных

    async with SessionLocal() as session:
        new_user = User(name="Alice")
        session.add(new_user)
        await session.commit()

asyncio.run(main())
