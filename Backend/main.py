from __future__ import annotations 
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, time

#instance_data
movie_data = {
    "movie_list": [
        {
        "name": "Avengers: Endgame",
        "pic": "https://preview.redd.it/1sdabp4nt2m21.jpg?auto=webp&s=1d3793ac4d16c6dfc457da2dc65cff869221cc80",
        "type": "Action",
        "movie_id": "M001",
        "detail": "Superhero movie",
        "duration": 180,
        "role": "on showing"
        },
        {
        "name": "The Boy And The Heron",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/9097ea9099114cf1b23220652c2bf864.jpg",
        "type": "Fantasy",
        "movie_id": "M002",
        "detail": "Fantasy movie",
        "duration": 124,
        "role": "recommend"
        },
        {
        "name": "Blue Giant",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/3062bae886c1445dbe99bd09f836fd19.jpg",
        "type": "Drama",
        "movie_id": "M003",
        "detail": "Drama movie",
        "duration": 120,
        "role": "recommend"
        },
        {
        "name": "The Hold Over",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/c65abd7d1b3e40ad90397076af1f26cc.jpg",
        "type": "Comedy",
        "movie_id": "M004",
        "detail": "Comedy movie",
        "duration": 133,
        "role": "comming soon"
        },
        {
        "name": "Let the Right One In",
        "pic": "https://resizing.flixster.com/SGQAjo7FxNx8IV2FQdOa0T4_rSE=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p183697_p_v12_ao.jpg",
        "type": "Horror",
        "movie_id": "M005",
        "detail": "Horror movie",
        "duration": 114,
        "role": "recommend"
        },
        {
        "name": "Kung Fu Panda 4",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/b5dffc5adfb74a0fb6b40c33a87fb52e.jpg",
        "type": "Comedy",
        "movie_id": "M006",
        "detail": "Comedy movie",
        "duration": 105,
        "role": "on showing"
        },
        {
        "name": "หลานม่า",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/6b318efc5ca74b5c952ee4ed98ee388b.jpg",
        "type": "Drama",
        "movie_id": "M007",
        "detail": "Drama movie",
        "duration": 125,
        "role": "comming soon"
        },
        {
        "name": "The First Omen",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/075827a4cf9a45958fc70fd4ddeb8a9a.jpg",
        "type": "Horror",
        "movie_id": "M008",
        "detail": "Horror movie",
        "duration": 120,
        "role": "on showing"
        },
        {
        "name": "Mother's Instinct",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/3db8c14861e84988ac45bd3d96cc5c25.jpg",
        "type": "Thriller",
        "movie_id": "M009",
        "detail": "Thriller movie",
        "duration": 94,
        "role": "recommend"
        },
        {
        "name": "Fall Guy",
        "pic": "https://img.wongnai.com/p/800x0/2024/04/11/95b0ce3451af47f3b5f7e24f847209b1.jpg",
        "type": "Action",
        "movie_id": "M010",
        "detail": "Action movie",
        "duration": 125,
        "role": "comming soon"
        },
        {
        "name": "A Quiet Place",
        "pic": "https://resizing.flixster.com/bly-yHD8oiPG0BGvpfrd9q3SPco=/206x305/v2/https://resizing.flixster.com/or3jxjzmcmu88rC-mcksfO642IU=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzNmYjhmOGMzLWU1YjctNGEyNS04OTJhLWY4YmIwMjNmZmFiMC53ZWJw",
        "type": "Horror",
        "movie_id": "M011",
        "detail": "Horror movie",
        "duration": 90,
        "role": "recommend"
        },
        {
        "name": "Talk to Me",
        "pic": "https://resizing.flixster.com/ejS3S8JOBfvZr_fQ_--6SyKKJpQ=/206x305/v2/https://resizing.flixster.com/9WxKriao1BmRamIaqig2k8hd5uM=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2YyZDQwYTM2LWZmYzEtNGUwMC05NzRkLTA3ODM0NThiNDE4Ny5qcGc=",
        "type": "Horror",
        "movie_id": "M012",
        "detail": "Horror movie",
        "duration": 95,
        "role": "recommend"
        },
        {
        "name": "When Evil Lurks",
        "pic": "https://resizing.flixster.com/pYKve2Su8tEGhH0tDOVXySIZUeQ=/206x305/v2/https://resizing.flixster.com/jRxONmZil0CTIu8L0mZJTbLLGrY=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2FiOWRlZjQ2LTY5OTctNGRmZi1hM2IwLWI5ZWQzYmQ4ZmFkYS5qcGc=",
        "type": "Horror",
        "movie_id": "M013",
        "detail": "Horror movie",
        "duration": 99,
        "role": "recommend"
        },
        {
        "name": "The Godfather",
        "pic": "https://picfiles.alphacoders.com/464/thumb-1920-464751.jpg",
        "type": "Crime",
        "movie_id": "M014",
        "detail": "Crime movie",
        "duration": 175,
        "role": "recommend"
        },
        {
        "name": "Inception",
        "pic": "https://m.media-amazon.com/images/M/MV5BMjExMjkwNTQ0Nl5BMl5BanBnXkFtZTcwNTY0OTk1Mw@@._V1_.jpg",
        "type": "Sci-fi",
        "movie_id": "M015",
        "detail": "Sci-fi movie",
        "duration": 148,
        "role": "recommend"
        }
    ]
}

class MinorCineflex:
    def __init__(self):
        self.__cinema_list: List[Cinema] = []
        self.__person_list: List[Person] = []
        self.__movie_list: List[Movie] = []

    def add_cinema(self, id: int, name: str, location: str, region: str, opentime: datetime, closetime: datetime, cinema_management):
        self.__cinema_list.append(Cinema(id, name, location, region, opentime, closetime, cinema_management))

    def add_person(self, name: str, tel_no: str, email: str, birthday: datetime, gender: str, account):
        self.__person_list.append(Person(name, tel_no, email, birthday, gender, account))
    
    def add_all_movie(self, name: str, img: str, movie_type: str, movie_id: str, detail: str, duration: int, role: str):
        self.__movie_list.append(Movie(name, img, movie_type, movie_id, detail, duration, role))

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
    
    def get_cinema(self):
        return [
            CinemaResponse(
                cinema_id=c.cinema_id, 
                name=c.name, 
                location=c.location,
                region=c.region, 
                opentime=c.opentime, 
                closetime=c.closetime,
                cinema_management=CinemaManagementResponse(
                    theater_list=[TheaterResponse(
                        theater_id=t.theater_id,
                        theater_type=t.theater_type,
                        seat_amount=t.seat_amount,
                        status=t.status,
                        audio_type=t.audio_type,
                        video_type=t.video_type,
                    ) for t in c.cinema_management.theater_list],
                    showtime_list=[ShowtimeResponse(
                        showtime_id=s.showtime_id,
                        start_date=s.start_date,
                        cinema_id=s.cinema_id,
                        theater_id=s.theater_id,
                        movie_id=s.movie_id,
                        dub=s.dub,
                        sub=s.sub
                    ) for s in c.cinema_management.showtime_list],
                    booking_list=[booking for booking in c.cinema_management.booking_list],
                    movie_list=[MovieResponse(
                        name = movie.name,
                        img = movie.img,
                        type = movie.type,
                        movie_id = movie.movie_id,
                        detail = movie.detail,
                        duration = movie.duration,
                        role = movie.role
                        ) for movie in c.cinema_management.movie_list] 
                )
            ) for c in memory_db.cinema_list
        ]
    
    def get_cinema_by_id(self, cinema_id: int):
        if(len(self.__cinema_list) > 0):
            for c in self.__cinema_list:
                if c.cinema_id == cinema_id:
                    return c
        else:
            return "Failed"

    def get_movie(self):
        return {
            "movie_list":[MovieResponse(
                name = movie.name,
                img = movie.img,
                type = movie.type,
                movie_id = movie.movie_id,
                detail = movie.detail,
                duration = movie.duration,
                role = movie.role
            ) for movie in memory_db.movie_list] 
        }

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
                    movie_list=[MovieResponse(
                        name = movie.name,
                        img = movie.img,
                        type = movie.type,
                        movie_id = movie.movie_id,
                        detail = movie.detail,
                        duration = movie.duration,
                        role = movie.role
                        ) for movie in c.cinema_management.movie_list] 
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
            ) for p in memory_db.person_list],
            "movie_list":[MovieResponse(
                name = movie.name,
                img = movie.img,
                type = movie.type,
                movie_id = movie.movie_id,
                detail = movie.detail,
                duration = movie.duration,
                role = movie.role
            ) for movie in memory_db.movie_list] 
        }

    #getter
    @property
    def cinema_list(self):
        return self.__cinema_list
    @property
    def person_list(self):
        return self.__person_list
    @property
    def movie_list(self):
        return self.__movie_list

class Cinema:
    def __init__(self, cinema_id: str, name: str, location: str,region: str, opentime: time, closetime: time, cinema_management):
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
    
    def add_cinema_theater(self, theater: Theater):
        self.__theater_list.append(theater)

    def get_theater(self):
        return [
            TheaterResponse(
                theater_id=t.theater_id,
                theater_type=t.theater_type,
                seat_amount=t.seat_amount,
                status=t.status,
                audio_type=t.audio_type,
                video_type=t.video_type,
                maintainance_list=[MaintainanceResponse(
                    detail=m.detail,
                    start_date=m.start_date,
                    end_date=m.end_date
                ) for m in t.maintainance_list]
            ) for t in self.__theater_list
        ]

    def get_theater_by_id(self, theater_id: str):
        if(len(self.__theater_list) > 0):
            for t in self.__theater_list:
                if t.theater_id == theater_id:
                    return t
        else:
            return "Failed"
        
    def add_cinema_showtime(self, showtime: Showtime):
        self.__showtime_list.append(showtime)

    def get_showtime(self):
        return [
            ShowtimeResponse(
                showtime_id=s.showtime_id,
                start_date=s.start_date,
                cinema_id=s.cinema_id,
                theater_id=s.theater_id,
                movie_id=s.movie_id,
                dub=s.dub,
                sub=s.sub
            ) for s in self.__showtime_list
        ]

    def get_showtime_by_id(self, showtime_id: str):
        if(len(self.__showtime_list) > 0):
            for s in self.__showtime_list:
                if s.showtime_id == showtime_id:
                    return s
        else:
            return "Failed"
    
    def add_cinema_booking(self, booking: Booking):
        self.__booking_list.append(booking)
    
    def add_cinema_movie(self, movie_id: str):
        for m in memory_db.movie_list:
            if movie_id == m.movie_id:
                self.__movie_list.append(m)
                return

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

    #getter
    @property
    def name(self):
        return self.__name
    @property
    def img(self):
        return self.__img
    @property
    def type(self):
        return self.__type
    @property
    def movie_id(self):
        return self.__movie_id
    @property
    def detail(self):
        return self.__detail
    @property
    def duration(self):
        return self.__duration
    @property
    def role(self):
        return self.__role

class Theater:
    def __init__(self, theater_id: str, theater_type: str, seat_amount: int, status: bool, audio_type: str, video_type: str):
        self.__theater_id = theater_id
        self.__theater_type = theater_type
        self.__seat_amount = seat_amount
        self.__status = status
        self.__audio_type = audio_type
        self.__video_type = video_type
        self.__maintainance_list: List[Maintainance] = []

    @property
    def theater_id(self):
        return self.__theater_id
    
    @property
    def theater_type(self):
        return self.__theater_type
    
    @property
    def seat_amount(self): 
        return self.__seat_amount
    
    @property
    def status(self):
        return self.__status
    
    @property
    def audio_type(self):
        return self.__audio_type
    
    @property
    def video_type(self):
        return self.__video_type
    
    @property
    def maintainance_list(self):
        return self.__maintainance_list

class Showtime:
    def __init__(self,showtime_id: str, start_date: datetime, cinema_id: str, theater_id: str, movie_id: str, dub: bool, sub: bool):
        self.__showtime_id = showtime_id
        self.__start_date = start_date
        self.__cinema_id = cinema_id
        self.__theater_id = theater_id
        self.__movie_id = movie_id
        self.__dub = dub
        self.__sub = sub
        self.__available_seat: List[Seat] = []
        self.__reserved_seat: List[Seat] = []

    @property
    def showtime_id(self):
        return self.__showtime_id
    
    @property
    def start_date(self):
        return self.__start_date
    
    @property
    def cinema_id(self):
        return self.__cinema_id
    
    @property
    def theater_id(self):
        return self.__theater_id
    
    @property
    def movie_id(self):
        return self.__movie_id
    
    @property
    def dub(self):
        return self.__dub
    
    @property
    def sub(self):
        return self.__sub
    
    @property
    def available_seat(self):
        return self.__available_seat
    
    @property
    def reserved_seat(self):
        return self.__reserved_seat

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
    cinema_id: str
    theater_id: str
    movie_id: str
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
    opentime: time
    closetime: time
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

#create_instance
memory_db.add_cinema(101, "minor_1", "12.001.0656", "north", time(11,00,00), time(23,00,00), CinemaManagement())
memory_db.add_cinema(102, "minor_2", "13.675.3356", "east", time(11,30,00), time(23,30,00), CinemaManagement())
for m in movie_data["movie_list"]:
    memory_db.add_all_movie(
        m["name"], 
        m["pic"],
        m["type"],
        m["movie_id"],
        m["detail"],
        m["duration"],
        m["role"]
    )
memory_db.cinema_list[0].cinema_management.add_cinema_movie("M001")
memory_db.cinema_list[0].cinema_management.add_cinema_movie("M010")

#create_theater
memory_db.cinema_list[0].cinema_management.add_cinema_theater(Theater("T-M101", "IMAX", 32, True, "Dolby Atmos", "IMAX"))
memory_db.cinema_list[0].cinema_management.add_cinema_theater(Theater("T-M102", "Standard", 32, True, "Dolby", "Standard"))
memory_db.cinema_list[1].cinema_management.add_cinema_theater(Theater("T-M201", "VIP", 32, True, "Dolby Atmos", "VIP"))
memory_db.cinema_list[1].cinema_management.add_cinema_theater(Theater("T-M202", "Standard", 32, True, "Dolby", "Standard"))

#create_showtime
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S001", datetime(2025, 3, 3, 12, 30, 00), "101", "T-M101", "M001", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S002", datetime(2025, 3, 3, 15, 30, 00), "101", "T-M102", "M010", True, False))

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

#movie
@app.get("/minorcineflex/movie")
def movie():
    return memory_db.get_movie()

#cinema
@app.get("/minorcineflex/cinema")
def cinema():
    return memory_db.get_cinema()

#theater
@app.get("/minorcineflex/cinema/{cinema_id}/theater")
def theater_list(cinema_id: int):
    return memory_db.get_cinema_by_id(cinema_id).cinema_management.get_theater()

@app.post("/moinorcineflex/cinema/{cinema_id}/add_theater")
def add_theater(cinema_id: int, theater: TheaterResponse):
    memory_db.get_cinema_by_id(cinema_id).cinema_management.add_cinema_theater(Theater(
        theater_id=theater.theater_id,
        theater_type=theater.theater_type,
        seat_amount=theater.seat_amount,
        status=theater.status,
        audio_type=theater.audio_type,
        video_type=theater.video_type
    ))
    return {"message": "Theater added successfully"}

@app.get("/minorcineflex/cinema/{cinema_id}/theater/{theater_id}")
def theater_by_id(cinema_id: int, theater_id: str):
    return memory_db.get_cinema_by_id(cinema_id).cinema_management.get_theater_by_id(theater_id)

#Showtime
@app.get("/minorcineflex/cinema/{cinema_id}/showtime")
def showtime_list(cinema_id: int):
    return memory_db.get_cinema_by_id(cinema_id).cinema_management.get_showtime()

@app.post("/minorcineflex/cinema/{cinema_id}/add_showtime")
def add_showtime(cinema_id: int, showtime: ShowtimeResponse):
    memory_db.get_cinema_by_id(cinema_id).cinema_management.add_cinema_showtime(Showtime(
        showtime_id=showtime.showtime_id,
        start_date=showtime.start_date,
        cinema_id=showtime.cinema_id,
        theater_id=showtime.theater_id,
        movie_id=showtime.movie_id,
        dub=showtime.dub,
        sub=showtime.sub
    ))
    return {"message": "Showtime added successfully"}

@app.get("/minorcineflex/cinema/{cinema_id}/showtime/{showtime_id}")
def showtime_by_id(cinema_id: int, showtime_id: str):
    return memory_db.get_cinema_by_id(cinema_id).cinema_management.get_showtime_by_id(showtime_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)