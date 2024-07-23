from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, DateTime, ForeignKey
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25), unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return f"User: {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()
