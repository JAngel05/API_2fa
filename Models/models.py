from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from sqlalchemy import Column, BigInteger
from datetime import datetime, timedelta


class Usuarios(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password: str 
    rol: str = Field(default="usuario")
    email: str = Field(default="usuario@ejemplo.com") 
    otp_length: int = Field(default=6)
    otp_type: str = Field(default="numeric") 

class TwoFactorCodes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id", index=True)
    hashed_code: str
    is_used: bool = Field(default=False)
    attempts: int = Field(default=0)
    expires_at: datetime = Field(default_factory=lambda: datetime.utcnow() + timedelta(minutes=5))