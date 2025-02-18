from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.app.repository.models import Student, Profile, Credential
from src.app.repository.database import connection
import asyncio


class Registration:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = True
            return object.__new__(cls)
        else:
            raise Exception("This class is a singleton!")

    @staticmethod
    @connection
    async def register_user(telegram_id: int, name: str, language: str, username: str, password: str,
                            session: AsyncSession):
        """Добавляет нового пользователя с профилем и учетными данными в базу данных."""

        # Проверяем, есть ли уже такой пользователь
        existing_user = await session.scalar(
            select(Student).where(Student.telegram_id == telegram_id)
        )
        if existing_user:
            return False  # Пользователь уже существует

        # Создаем модели
        student = Student(telegram_id=telegram_id)
        credential = Credential(username=username, password=password, student=student)
        profile = Profile(name=name, language=language, student=student)

        # Добавляем в сессию
        session.add(student)
        session.add(credential)
        session.add(profile)

        # Коммитим изменения
        await session.commit()
        return True  # Успешно зарегистрирован


    @staticmethod
    @connection
    async def get_telegram_user_by_id(telegram_id: int, session: AsyncSession):
        try:
            stmt = select(Student).where(Student.telegram_id == telegram_id)
            request = await session.scalars(stmt)  # Используем await для выполнения запроса
            return request.first()  # Возвращаем первый результат или None
        except Exception as e:
            print(e)
            return None  # Возвращаем None в случае ошибки
    @staticmethod
    @connection
    async def add_profile(telegram_id: int, session: AsyncSession, profile: Profile):
        stmt = session.add()
registration = Registration()
print(registration)