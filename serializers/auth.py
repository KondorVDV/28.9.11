from pydantic import BaseModel, Field
import datetime

class User(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


class Token(BaseModel):
    """Токен"""
    token: str


class Book(BaseModel):

    firstname: str = Field(None)
    Lastname: str = Field(None)
    checkin: datetime.datetime = Field(None)
    chekout: datetime.datetime = Field(None)


class Bookingdates(BaseModel):
    """Модель даты при создании заказа"""
    checkin: datetime.datetime
    checkout: datetime.datetime

class CreateBooking(BaseModel):
    """Модель создания бронирования"""
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: dict
    additionalneeds: str