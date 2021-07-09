from . import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

# ----------------------------------------


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    last_name: str
    email: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String(127), nullable=False)
    last_name = Column(String(511), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(511), nullable=False)
