import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

class MinorCineflex:
    def __init__(self):
        self.__cinema_list: List[Cinema] = []
        self.__person_list: List[Person] = []

    def add_cinema(self, id: int, name: str, location: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_list.append(Cinema(id, name, location, opentime, closetime, cinema_management))

    def add_person(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__person_list.append(Person(name, tel_no, email, birthday, gender, account))

    #getter
    def cinema_list(self):
        return self.__cinema_list
    def person_list(self):
        return self.__person_list

class Cinema:
    def __init__(self, cinema_id: str, name: str, location: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_id = cinema_id
        self.__name = name
        self.__location = location
        self.__opentime = opentime
        self.__closetime = closetime
        self.__cinema_management = cinema_management

    #getter
    def get_cinema_id(self):
        return self.__cinema_id
    def get_name(self):
        return self.__name
    def get_location(self):
        return self.__location
    def get_opentime(self):
        return self.__opentime
    def get_closetime(self):
        return self.__closetime
    def get_cinema_management(self):
        return self.__cinema_management

class CinemaManagement:
    def __init__(self):
        self.__theater_list: List[Theater] = []
        self.__showtime_list: List[Showtime] = []
        self.__booking_list: List[Booking] = []
        self.__movie_list: List[Movie] = []
    
    def add_theater(self, theater):
        self.__theater_list.append(theater)

    #getter
    def get_theater_list(self):
        return self.__theater_list
    def get_showtime_list(self):
        return self.__showtime_list
    def get_booking_list(self):
        return self.__booking_list
    def get_movie_list(self):
        return self.__movie_list

class Person:
    def __init__(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__name = name
        self.__tel_no = tel_no
        self.__email = email
        self.__birthday = birthday
        self.__gender = gender
        self.__account = account

    #getter
    def get_name(self):
        return self.__name
    def get_tel_no(self):
        return self.__tel_no
    def get_email(self):
        return self.__email
    def get_birthday(self):
        return self.__birthday
    def get_gender(self):
        return self.__gender
    def get_account(self):
        return self.__account

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
    def __init__(self, name: str, img: str, movie_type: str, movie_id: str, detail: str, duration: int):
        self.__name = name
        self.__img = img
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

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class CinemaManagementResponse(BaseModel):
    theater_list: List[dict] 
    showtime_list: List[dict] 
    booking_list: List[dict]  
    movie_list: List[dict] 

class CinemaResponse(BaseModel):
    cinema_id: int
    name: str
    location: str
    opentime: datetime
    closetime: datetime
    cinema_management: CinemaManagementResponse

class PersonResponse(BaseModel):
    name: str
    tel_no: str
    email: str
    birthday: datetime
    gender: str
    account: dict

class MinorCineflexResponse(BaseModel):
    cinema_list: List[CinemaResponse]
    person_list: List[PersonResponse]

memory_db = MinorCineflex()

memory_db.add_cinema(101, "minor_1", "12.001.0656", datetime.strptime("2011-12-19", "%Y-%m-%d"), datetime.strptime("2020-12-19", "%Y-%m-%d"), CinemaManagement())

#system
@app.get("/minorcineflex", response_model=MinorCineflexResponse)
def get_system():
   return {
       "cinema_list": [CinemaResponse(
            cinema_id=c.get_cinema_id(), 
            name=c.get_name(), 
            location=c.get_location(), 
            opentime=c.get_opentime(), 
            closetime=c.get_closetime(),
            cinema_management=CinemaManagementResponse(
                theater_list=[theater for theater in c.get_cinema_management().get_theater_list()],
                showtime_list=[showtime for showtime in c.get_cinema_management().get_showtime_list()],
                booking_list=[booking for booking in c.get_cinema_management().get_booking_list()],
                movie_list=[movie for movie in c.get_cinema_management().get_movie_list()] 
            )
        ) for c in memory_db.cinema_list()],
        "person_list": [PersonResponse(
            name=p.get_name(),
            tel_no=p.get_tel_no(),
            email=p.get_email,
            birthday=p.get_birthday(),
            gender=p.get_gender(),
            account=p.get_account()
        ) for p in memory_db.person_list()]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)