from __future__ import annotations 
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MinorCineflex:
    def __init__(self):
        self.__cinema_list: List[Cinema] = []
        self.__person_list: List[Person] = []

    def add_cinema(self, id: int, name: str, location: str, region: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_list.append(Cinema(id, name, location, region, opentime, closetime, cinema_management))

    def add_person(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__person_list.append(Person(name, tel_no, email, birthday, gender, account))

    def get_person(self):
        return [
            PersonResponse(
                name=p.name,
                tel_no=p.tel_no,
                email=p.email,
                birthday=p.birthday,
                gender=p.gender,
                account={
                    "username": p.account.username,
                    "password": p.account.password,
                    "account_id": p.account.account_id,
                    "point": p.account.point,
                    "registered_date": p.account.registered_date,
                    "expiration_date": p.account.expiration_date,
                    "history": p.account.history,
                    "document_list": p.account.document_list,
                    "reserved_list": p.account.reserved_list
                }
            ) for p in memory_db.person_list
        ]

    def get_system(self):
        return {
            "cinema_list": [CinemaResponse(
                cinema_id=c.cinema_id, 
                name=c.name, 
                location=c.location,
                region=c.region, 
                opentime=c.opentime, 
                closetime=c.closetime,
                cinema_management=CinemaManagementResponse(
                    theater_list=[theater for theater in c.cinema_management.theater_list],
                    showtime_list=[showtime for showtime in c.cinema_management.showtime_list],
                    booking_list=[booking for booking in c.cinema_management.booking_list],
                    movie_list=[movie for movie in c.cinema_management.movie_list] 
                )
            ) for c in memory_db.cinema_list],
            "person_list": [PersonResponse(
                name=p.name,
                tel_no=p.tel_no,
                email=p.email,
                birthday=p.birthday,
                gender=p.gender,
                account={
                    "username": p.account.username,
                    "password": p.account.password,
                    "account_id": p.account.account_id,
                    "point": p.account.point,
                    "registered_date": p.account.registered_date,
                    "expiration_date": p.account.expiration_date,
                    "history": p.account.history,
                    "document_list": p.account.document_list,
                    "reserved_list": p.account.reserved_list
                }
            ) for p in memory_db.person_list]
        }

    #getter
    @property
    def cinema_list(self):
        return self.__cinema_list
    @property
    def person_list(self):
        return self.__person_list

class Cinema:
    def __init__(self, cinema_id: str, name: str, location: str,region: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_id = cinema_id
        self.__name = name
        self.__location = location
        self.__region = region
        self.__opentime = opentime
        self.__closetime = closetime
        self.__cinema_management = cinema_management

    #getter
    @property
    def cinema_id(self):
        return self.__cinema_id
    @property
    def name(self):
        return self.__name
    @property
    def location(self):
        return self.__location
    @property
    def region(self):
        return self.__region
    @property
    def opentime(self):
        return self.__opentime
    @property
    def closetime(self):
        return self.__closetime
    @property
    def cinema_management(self):
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
    @property
    def theater_list(self):
        return self.__theater_list
    @property
    def showtime_list(self):
        return self.__showtime_list
    @property
    def booking_list(self):
        return self.__booking_list
    @property
    def movie_list(self):
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
    @property
    def name(self):
        return self.__name
    @property
    def tel_no(self):
        return self.__tel_no
    @property
    def email(self):
        return self.__email
    @property
    def birthday(self):
        return self.__birthday
    @property
    def gender(self):
        return self.__gender
    @property
    def account(self):
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
        self.__reserved_list: List[Seat] = []

    def update_account(self, new_dict_data):
        self.__username = new_dict_data.username
        self.__password = new_dict_data.password
        self.__account_id = new_dict_data.account_id
        self.__point = new_dict_data.point
        self.__registered_date = new_dict_data.registered_date
        self.__expiration_date = new_dict_data.expiration_date
        self.__history = new_dict_data.history
        self.__document_list = new_dict_data.document_list
        self.__reserved_list = new_dict_data.reserved_list

    #getter
    @property
    def username(self):
        return self.__username
    @property
    def password(self):
        return self.__password
    @property
    def account_id(self):
        return self.__account_id
    @property
    def point(self):
        return self.__point
    @property
    def registered_date(self):
        return self.__registered_date
    @property
    def expiration_date(self):
        return self.__expiration_date
    @property
    def history(self):
        return self.__history
    @property
    def document_list(self):
        return self.__document_list
    @property
    def reserved_list(self):
        return self.__reserved_list

class Movie:
    def __init__(self, name: str, img: str, movie_type: str, movie_id: str, detail: str, duration: int, role: str):
        self.__name = name
        self.__img = img
        self.__type = movie_type
        self.__movie_id = movie_id
        self.__detail = detail
        self.__duration = duration
        self.__role = role

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
    def __init__(self,showtime_id: str, start_date: datetime, cinema, theater, movie, dub: bool, sub: bool):
        self.__showtime_id = showtime_id
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

class Maintainance:
    def __init__(self, detail: str, start_date: datetime, end_date: datetime):
        self.__detail = detail
        self.__start_date = start_date
        self.__end_date = end_date

class Booking:
    def __init__(self, showtime: Showtime, account_id: str, seat_list: List[Seat], booking_date: datetime, payment_method: Payment, total: float):
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

#BaseModel for API route
class SeatResponse(BaseModel):
    seat_id: str
    seat_type: str
    size: int
    price: float

class MaintainanceResponse(BaseModel):
    detail: str
    start_date: datetime
    end_date: datetime


class TheaterResponse(BaseModel):
    theater_id: str
    theater_type: str
    seat_amount: int
    status: bool
    audio_type: str
    video_type: str
    maintainance_list: List[MaintainanceResponse] = []

class MovieResponse(BaseModel):
    name: str
    img: str
    type: str
    movie_id: str
    detail: str
    duration: int
    role: str

class ShowtimeResponse(BaseModel):
    showtime_id: str
    start_date: datetime
    cinema: CinemaResponse
    theater: TheaterResponse
    movie: MovieResponse
    dub: bool
    sub: bool
    available_seat: List[SeatResponse] = [] 
    reserved_seat: List[SeatResponse] = []

class CinemaManagementResponse(BaseModel):
    theater_list: List[TheaterResponse] = []
    showtime_list: List[ShowtimeResponse] = []
    booking_list: List[BookingResponse] = []
    movie_list: List[MovieResponse] = []

class CinemaResponse(BaseModel):
    cinema_id: int
    name: str
    location: str
    region: str
    opentime: datetime
    closetime: datetime
    cinema_management: CinemaManagementResponse

class PaymentResponse(BaseModel):
    payment_type: str

class BookingResponse(BaseModel):
    showtime: ShowtimeResponse
    account_id: str
    seat_list: List[SeatResponse] = []
    booking_date: datetime
    payment_method: PaymentResponse
    total: float

class PersonResponse(BaseModel):
    name: str
    tel_no: str
    email: str
    birthday: str
    gender: str
    account: dict

class DocumentResponse(BaseModel):
    booking: BookingResponse
    document_type: str

class AccountRequest(BaseModel):
    username: str
    password: str
    account_id: str
    point: int
    registered_date: Optional[datetime]
    expiration_date: Optional[datetime]
    history: List[BookingResponse] = []
    document_list: List[DocumentResponse] = []
    reserved_list: List[SeatResponse] = []

class PersonRequest(BaseModel):
    name: str
    tel_no: str
    email: str
    birthday: Optional[datetime]
    gender: str
    account: AccountRequest

class MinorCineflexResponse(BaseModel):
    cinema_list: List[CinemaResponse]
    person_list: List[PersonResponse]

#temporary_database
memory_db = MinorCineflex()
memory_db.add_cinema(101, "minor_1", "12.001.0656", "nort", datetime.strptime("2011-12-19", "%Y-%m-%d"), datetime.strptime("2020-12-19", "%Y-%m-%d"), CinemaManagement())

#system
@app.get("/minorcineflex")
def system():
    return memory_db.get_system()

#person
@app.get("/minorcineflex/person")
def person():
    return memory_db.get_person()

@app.post("/minorcineflex/add_person")
def add_person(person: PersonRequest):
    new_account = Account(
        username=person.account.username,
        password=person.account.password,
        account_id=person.account.account_id,
        point=person.account.point,
        registered_date=str(person.account.registered_date),
        expiration_date=str(person.account.expiration_date)
    )

    memory_db.add_person(
        name=person.name,
        tel_no=person.tel_no,
        email=person.email,
        birthday=str(person.birthday),
        gender=person.gender,
        account=new_account
    )
    return {"message": "Person added successfully"}

@app.put("/minorcineflex/update_person")
def update_person(person: PersonRequest):
    person_to_update = None
    for p in memory_db.person_list:
        if p.account.account_id == person.account.account_id:
            person_to_update = p
            break

    if person_to_update:
        person_to_update.account.update_account(person.account)
        return {"message": "Person and account updated successfully"}
    else:
        return {"error": "Person not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)