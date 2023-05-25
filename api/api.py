import requests


class RestfulBooker:
    url = "https://restful-booker.herokuapp.com"

    def api_key(self, user):
        """Получение токена"""
        return requests.post(self.url + '/auth', json=user)


    def booking_create_booking(self, booking):
        """Создает новое бронирование в API"""

        headers = {
            'Content-Type': 'application/json',
            }

        return requests.post(self.url +'/booking', headers=headers, json=booking)


    def booking_get_bookingids(self,id):
        """Возвращает конкретное бронирование на основе предоставленного идентификатора бронирования"""
        headers = {
            'Accept': 'application/json',
        }


        return requests.get(self.url + f'/booking/{id}')







rest_ful_booker = RestfulBooker()

