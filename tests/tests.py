from api.api import rest_ful_booker
from base_data.base import booking_data, user_data
import json
import pytest
from serializers.auth import Token, User, Bookingdates, CreateBooking


def test_auth_key():
    """Получение токена"""

    user_1 = User(**user_data)
    user = user_1.dict()
    auth_key_token = rest_ful_booker.api_key(user)
    key = auth_key_token.json()['token']
    token = auth_key_token.json()

    assert Token(**token).dict() == Token(**auth_key_token.json()).dict()
    assert auth_key_token.status_code == 200, f'{auth_key_token.json()}'



def test_booking_create_booking_1():
    """Создание бронирования"""


    booking_1 = CreateBooking(**booking_data)
    booking = booking_1.dict()
    res = rest_ful_booker.booking_create_booking(booking)
    result = res.json()
    status = res.status_code
    id = result['bookingid']

    assert status == 200
    assert 'bookingid' in result


def test_booking_post_bookingIds():
    """Возвращает конкретное бронирование на основе предоставленного идентификатора бронирования"""

    booking_1 = CreateBooking(**booking_data)
    booking = booking_1.dict()
    res = rest_ful_booker.booking_create_booking(booking)
    get_id = res.json()
    id = get_id['bookingid']
    r = rest_ful_booker.booking_get_bookingids(id)
    result = r.json()
    status = r.status_code

    assert status == 200
    assert 'firstname' in result

    return result




