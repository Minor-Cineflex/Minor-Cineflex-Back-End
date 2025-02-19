import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, ForwardRef
from datetime import datetime

Cinema = ForwardRef("Cinema")

class Maintainance(BaseModel):
    detail: str
    start_date: datetime
    end_date: datetime

class Seat(BaseModel):
    seat_id: str
    seat_type: str
    size: int
    price: float

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

class Movie(BaseModel):
    name: str
    img: str
    type: str
    movie_id: str
    detail: str
    duration: int

class Theater(BaseModel):
    theater_id: str
    theater_type: str
    seat_amount: int
    status: bool
    audio_type: str
    video_type: str
    maintainance_list: List[Maintainance]

class Showtime(BaseModel):
    start_date: datetime
    cinema: Cinema
    theater: Theater
    movie: Movie
    dub: bool
    sub: bool
    available_seat: List[Seat]
    reserved_seat: List[Seat]

class Payment(BaseModel):
    payment_type: str

class Booking(BaseModel):
    showtime: Showtime
    account_id: str
    seat_list: List[Seat]
    booking_date: datetime
    payment_method: Payment
    total: float

class CinemaManagement(BaseModel):
    theater_list: List[Theater]
    showtime_list: List[Showtime]
    booking_list: List[Booking]
    movie_list: List[Movie]
    
class Cinema(BaseModel):
    cinema_id: str
    name: str
    location: str
    opentime: datetime
    closetime: datetime
    cinema_management: CinemaManagement

class Document(BaseModel):
    booking: Booking
    document_type: str

class Account(BaseModel):
    username: str
    password: str
    account_id: str
    point: int
    registered_date: datetime
    expiration_date: datetime
    history: List[Booking]
    document_list: List[Document]

class Person(BaseModel):
    name: str
    tel_no: str
    email: str
    birthday: datetime
    gender: str
    account: Account

class MinorCineflex(BaseModel):
    cinema_list: List[Cinema]
    person_list: List[Person]

class User(Person):
    pass

class Admin(Person):
    pass

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

memory_db = MinorCineflex(cinema_list=[], person_list=[])

@app.get("/minorcineflex", response_model=MinorCineflex)
def get_system():
    return memory_db

@app.get("/person", response_model=List[Person])
def get_person():
    if not memory_db.person_list:
        return []
    return memory_db.person_list

@app.post("/person", response_model=Person)
def add_person(user: User):
    memory_db.person_list.append(user)
    return user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)