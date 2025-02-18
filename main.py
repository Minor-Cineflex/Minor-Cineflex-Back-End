from datetime import datetime
from typing import List

class MinorCineflex:
    def __init__(self):
        self.__cinema_list: List[Cinema] = []
        self.__person_list: List[Person] = []
    
    def add_cinema(self, cinema):
        self.__cinema_list.append(cinema)

    def get_person(self, username, password):
        pass

    def get_cinema_list(self):
        pass

class Cinema:
    def __init__(self, cinema_id: str, name: str, location: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_id = cinema_id
        self.__name = name
        self.__location = location
        self.__opentime = opentime
        self.__closetime = closetime
        self.__cinema_management = cinema_management

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

class Person:
    def __init__(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__name = name
        self.__tel_no = tel_no
        self.__email = email
        self.__birthday = birthday
        self.__gender = gender
        self.__account = account

    def checkAccountUsernameAndPassword(self, username, password):
        pass

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

class Movie:
    def __init__(self, name: str, movie_type: str, movie_id: str, detail: str, duration: int):
        self.__name = name
        self.__type = movie_type
        self.__movie_id = movie_id
        self.__detail = detail
        self.__duration = duration

class Theater:
    def __init__(self, theater_id: str, theater_type: str, seat_amount: int, status: bool, audio_type: str, video_type: str):
        self.__theater_id = theater_id
        self.__theater_type = theater_type
        self.__seat_amount = seat_amount
        self.__status = status
        self.__audio_type = audio_type
        self.__video_type = video_type
        self.__maintainance_list: List[Maintainance] = []

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

class Payment:
    def __init__(self, payment_type: str):
        self.__payment_type = payment_type

class Seat:
    def __init__(self, seat_id: str, seat_type: str, size: int, price: float):
        self.__seat_id = seat_id
        self.__seat_type = seat_type
        self.__size = size
        self.__price = price

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

class Booking:
    def __init__(self, showtime, account_id: str, seat_list: List[Seat], booking_date: datetime, payment_method, total: float):
        self.__showtime = showtime
        self.__account_id = account_id
        self.__seat_list = seat_list
        self.__booking_date = booking_date
        self.__payment_method = payment_method
        self.__total = total

class Document:
    def __init__(self, booking, document_type: str):
        self.__booking = booking
        self.__document_type = document_type

def create_mock_data():
    minor_cineflex = MinorCineflex()
    cinema_mgmt = CinemaManagement()
    
    theater1 = Theater("T001", "IMAX", 100, True, "Dolby Atmos", "4K")
    theater2 = Theater("T002", "Standard", 150, True, "Dolby Surround", "2K")
    cinema_mgmt.add_theater(theater1)
    cinema_mgmt.add_theater(theater2)
    
    cinema1 = Cinema("C001", "Central Cineplex", "Downtown", datetime(2023, 1, 1, 10, 0), datetime(2023, 1, 1, 22, 0), cinema_mgmt)
    cinema2 = Cinema("C002", "Grand Mall Cinema", "Uptown", datetime(2023, 1, 1, 9, 0), datetime(2023, 1, 1, 23, 0), cinema_mgmt)
    minor_cineflex.add_cinema(cinema1)
    minor_cineflex.add_cinema(cinema2)
    
    print("Mock data created successfully!")

create_mock_data()
