from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.app.repository.models import User
from src.app.repository.database import connection
import asyncio

# class UserRepository:
#     @staticmethod
#     @connection
#     async def add_user(username: str, password: str, session: AsyncSession):
#         # Проверяем, существует ли пользователь с таким же username
#         stmt = select(User).where(User.username == username)
#         result = await session.execute(stmt)
#         existing_user = result.scalar_one_or_none()
#
#         if existing_user:
#             raise ValueError("Пользователь с таким username уже существует!")
#
#         # Создаем нового пользователя
#         new_user = User(username=username, password=password)
#         session.add(new_user)
#         await session.commit()  # Фиксируем изменения
#         await session.refresh(new_user)  # Обновляем объект, чтобы получить ID
#
#         return new_user  # Возвращаем созданного пользователя
#
# async def add():
#     new_user = await UserRepository.add_user(username="testuser", password="securepassword")
#     print(f"Пользователь создан: {new_user.id}, {new_user.username}")
#
# asyncio.run(add())


@connection
async def get_users(session):
    return await session.execute(select(User))