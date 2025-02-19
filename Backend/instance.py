import requests
from datetime import datetime
from typing import List

class MinorCineflex:
    def __init__(self):
        self.__cinema_list: List[Cinema] = []
        self.__person_list: List[Person] = []

    def cinema_list(self):
        return self.__cinema_list
    
    def person_list(self):
        return self.__person_list
    
    def to_dic(self):
        return {
            "cinema_list": self.cinema_list,
            "person_list": [person.to_dic() for person in self.__person_list]
        }

class Cinema:
    def __init__(self, cinema_id: str, name: str, location: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_id = cinema_id
        self.__name = name
        self.__location = location
        self.__opentime = opentime
        self.__closetime = closetime
        self.__cinema_management = cinema_management.to_dic()

    def to_dic(self):
        return{
            []
        }

class CinemaManagement:
    def __init__(self):
        self.__theater_list: List[Theater] = []
        self.__showtime_list: List[Showtime] = []
        self.__booking_list: List[Booking] = []
        self.__movie_list: List[Movie] = []
    
    def add_theater(self, theater):
        self.__theater_list.append(theater)

    def get_Movies_list(self):
        pass

    def to_dic(self):
        return {
            "theater_list": self.__theater_list.todic(),
            "showtime": self.__showtime_list.todic(),
            "booking_list": self.__booking_list.todic(),
            "movie_list": self.__movie_list.todic()
        }

class Person:
    def __init__(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__name = name
        self.__tel_no = tel_no
        self.__email = email
        self.__birthday = birthday
        self.__gender = gender
        self.__account = account

    def to_dic(self):
        return {
            "name": self.__name,
            "tel_no": self.__tel_no,
            "email": self.__email,
            "birthday": self.__birthday,
            "gender": self.__gender,
            "account": self.__account.to_dic()
        }


class User(Person):
    pass

class Admin(Person):
    pass

class Account:
    def __init__(self, username: str, password: str, account_id: str, point: int, registered_date: datetime, expiration_date: datetime):
        self.__username = username
        self.__password = password
        self.__account_id = account_id
        self.__point = point
        self.__registered_date = registered_date
        self.__expiration_date = expiration_date
        self.__history: List[Booking] = []
        self.__document_list: List[Document] = []

    def to_dic(self):
        return {
            "username": self.__username,
            "password": self.__password,
            "account_id": self.__account_id,
            "point": self.__point,
            "registered_date": self.__registered_date,
            "expiration_date": self.__expiration_date,
            "history": self.__history,        
            "document_list": self.__document_list 
        }

class Movie:
    def __init__(self, name: str, img: str, movie_type: str, movie_id: str, detail: str, duration: int):
        self.__name = name
        self.__img = img
        self.__type = movie_type
        self.__movie_id = movie_id
        self.__detail = detail
        self.__duration = duration

    def todic(self):
        return {
            "name": self.__name,
            "img": self.__img,
            "type": self.__type,
            "movie_id": self.__movie_id,
            "details": self.__detail,
            "duration": self.__duration
        }

class Theater:
    def __init__(self, theater_id: str, theater_type: str, seat_amount: int, status: bool, audio_type: str, video_type: str):
        self.__theater_id = theater_id
        self.__theater_type = theater_type
        self.__seat_amount = seat_amount
        self.__status = status
        self.__audio_type = audio_type
        self.__video_type = video_type
        self.__maintainance_list: List[Maintainance] = []

    def to_dic(self):
        return{
            "theater_id": self.__theater_id,
            "theater_type": self.__theater_type,
            "seat_amount": self.__seat_amount,
            "status": self.__status,
            "audio_type": self.__audio_type,
            "video_type": self.__video_type,
            "maintainance_list": self.__maintainance_list
        }

class Showtime:
    def __init__(self, start_date: datetime, cinema, theater, movie, dub: bool, sub: bool):
        self.__start_date = start_date
        self.__cinema = cinema
        self.__theater = theater
        self.__movie = movie
        self.__dub = dub
        self.__sub = sub
        self.__available_seat: List[Seat] = []
        self.__reserved_seat: List[Seat] = []

    def to_dic(self):
        return {
            "start_date": self.__start_date,
            "cinema": self.__cinema.to_dic(),
            "theater": self.__theater.to_dic(),
            "movie": self.__movie.to_dic(),
            "dub": self.__dub,
            "sub": self.__sub,
            "available_seat": self.__available_seat,
            "reserved_seat": self.__reserved_seat
        }

class Payment:
    def __init__(self, payment_type: str):
        self.__payment_type = payment_type

    def to_dic(self):
        return{
            "payment_type": self.__payment_type
        }

class Seat:
    def __init__(self, seat_id: str, seat_type: str, size: int, price: float):
        self.__seat_id = seat_id
        self.__seat_type = seat_type
        self.__size = size
        self.__price = price

    def to_dic(self):
        return{
            "seat_id": self.__seat_id,
            "seat_type": self.__seat_type,
            "size": self.__size,
            "price": self.__price
        }

class DeluxeSeat(Seat):
    pass

class PremiumSeat(Seat):
    pass

class HoneymoonSeat(Seat):
    pass

class FirstClass(Seat):
    pass

class IMAXSeat(Seat):
    pass

class Maintainance:
    def __init__(self, detail: str, start_date: datetime, end_date: datetime):
        self.__detail = detail
        self.__start_date = start_date
        self.__end_date = end_date

    def to_dic(self):
        return{
            "detail": self.__detail,
            "start_date": self.__start_date,
            "end_date": self.__end_date
        }

class Booking:
    def __init__(self, showtime, account_id: str, seat_list: List[Seat], booking_date: datetime, payment_method, total: float):
        self.__showtime = showtime
        self.__account_id = account_id
        self.__seat_list = seat_list
        self.__booking_date = booking_date
        self.__payment_method = payment_method
        self.__total = total

    def to_dic(self):
        return{
            "showtime": self.__showtime.to_dic(),
            "account_id": self.__account_id,
            "seat_list": self.__seat_list,
            "booking_date": self.__booking_date,
            "payment_method": self.__payment_method.to_dic(),
            "total": self.__total
        }

class Document:
    def __init__(self, booking, document_type: str):
        self.__booking = booking
        self.__document_type = document_type

    def to_dic(self):
        return{
            "booking": self.__booking.todic(),
            "document_type": self.__document_type
        }

data = [
    {
        "name": "Khom",
        "tel_no": "1224",
        "email": "xyz",
        "birthday": "2025-02-19",
        "gender": "male",
        "account": {
            "username": "khom",
            "password": "123",
            "account_id": "001",
            "point": 0,
            "registered_date": "2025-02-19",
            "expiration_date": "2025-02-19",
            "history": [],
            "document_list": []
        }
    },
    {
        "name": "Tan",
        "tel_no": "12506",
        "email": "abc",
        "birthday": "2025-02-18",
        "gender": "male",
        "account": {
            "username": "Tan",
            "password": "789",
            "account_id": "002",
            "point": 0,
            "registered_date": "2025-02-18",
            "expiration_date": "2025-02-18",
            "history": [],
            "document_list": []
        }
    }
]

system = MinorCineflex()

for i in data:
    user = User(
        i["name"], i["tel_no"], i["email"], i["birthday"], i["gender"],
        Account(
            i["account"]["username"], i["account"]["password"], i["account"]["account_id"],
            i["account"]["point"], i["account"]["registered_date"], i["account"]["expiration_date"]
        )
    )
    system.person_list().append(user)

    response = requests.post("http://localhost:8000/person" , json=user.to_dic())
    print("Status Code:", response.status_code)
    print("Response:", response.json())