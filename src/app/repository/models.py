from sqlalchemy import BIGINT, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.app.repository.database import Base
from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, validator, ValidationError



class Student(Base):
    telegram_id: Mapped[int] = mapped_column(BIGINT, unique=True)
    created_at = None
    updated_at = None
    credentials: Mapped['Credential'] = relationship(
        back_populates="student", uselist=False, cascade="all, delete-orphan"
    )
    profile: Mapped["Profile"] = relationship(
        back_populates="student", uselist=False, cascade="all, delete-orphan"
    )


class Credential(Base):
    username: Mapped[str] = mapped_column(VARCHAR)
    password: Mapped[str] = mapped_column(VARCHAR)
    student_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey('students.id'), unique=True, nullable=False
    )

    student: Mapped['Student'] = relationship(back_populates="credentials")


class Profile(Base):
    student_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey('students.id'), unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(VARCHAR)
    language: Mapped[str] = mapped_column(VARCHAR)

    student: Mapped["Student"] = relationship(back_populates="profile")


