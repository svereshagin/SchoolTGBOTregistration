from sqlalchemy import BIGINT, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.repository.database import Base, engine, SessionLocal

class Student(Base):

    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    created_at = None
    updated_at = None
    user_credentials: Mapped['User_credentials'] = relationship(
        back_populates="student", uselist=False, cascade="all, delete-orphan"
    )
    telegram_profile: Mapped["TelegramProfile"] = relationship(
        back_populates="student", uselist=False, cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Student= {self.telegram_id}, created_at= {self.created_at}, updated_at= {self.updated_at}"


class User_credentials(Base):
    """
    Represents a user's credentials model with next attributes
    for telegram registration.
    id, created_at, updated_at were inherited by Base
    id : int
    username : str
    password : str
    created_at : datastamp
    updated_at : datastamp
    REFERS to students table
    """
    username: Mapped[str] = mapped_column(VARCHAR)
    password: Mapped[str] = mapped_column(VARCHAR)
    student_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey('students.id'), unique=True, nullable=False
    )

    student: Mapped['Student'] = relationship(back_populates="user_credentials")

    def __repr__(self) -> str:
        return f"UserCredentials(id={self.id}, username={self.username}, password={self.password})"


class TelegramProfile(Base):
    student_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey('students.id'), unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(VARCHAR)
    language: Mapped[str] = mapped_column(VARCHAR)

    student: Mapped["Student"] = relationship(back_populates="telegram_profile")


async def create_and_commit():
    # Создаем сессию
    async with SessionLocal() as session:
        # Создаем объекты
        s = Student(telegram_id=112312312, user_credentials=User_credentials(username="test", password="<PASSWORD>"),
                    telegram_profile=TelegramProfile(name='123', language='ru'))
        # Добавляем объекты в сессию
        session.add(s)

        # Выполняем commit
        await session.commit()

        # После commit объекты будут сохранены, и id будут присвоены
        print(s.user_credentials)  # Теперь id будет не None
