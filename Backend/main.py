from __future__ import annotations 
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, time

#instance_data
movie_data = {
    "movie_list": [
        {
        "name": "Avengers: Endgame",
        "img": "https://preview.redd.it/1sdabp4nt2m21.jpg?auto=webp&s=1d3793ac4d16c6dfc457da2dc65cff869221cc80",
        "type": "Action",
        "movie_id": "M001",
        "detail": "Superhero movie",
        "duration": 180,
        "role": "on showing"
        },
        {
        "name": "The Boy And The Heron",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/9097ea9099114cf1b23220652c2bf864.jpg",
        "type": "Fantasy",
        "movie_id": "M002",
        "detail": "Fantasy movie",
        "duration": 124,
        "role": "recommend"
        },
        {
        "name": "Blue Giant",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/3062bae886c1445dbe99bd09f836fd19.jpg",
        "type": "Drama",
        "movie_id": "M003",
        "detail": "Drama movie",
        "duration": 120,
        "role": "recommend"
        },
        {
        "name": "The Hold Over",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/c65abd7d1b3e40ad90397076af1f26cc.jpg",
        "type": "Comedy",
        "movie_id": "M004",
        "detail": "Comedy movie",
        "duration": 133,
        "role": "coming soon"
        },
        {
        "name": "Let the Right One In",
        "img": "https://resizing.flixster.com/SGQAjo7FxNx8IV2FQdOa0T4_rSE=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p183697_p_v12_ao.jpg",
        "type": "Horror",
        "movie_id": "M005",
        "detail": "Horror movie",
        "duration": 114,
        "role": "recommend"
        },
        {
        "name": "Kung Fu Panda 4",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/b5dffc5adfb74a0fb6b40c33a87fb52e.jpg",
        "type": "Comedy",
        "movie_id": "M006",
        "detail": "Comedy movie",
        "duration": 105,
        "role": "on showing"
        },
        {
        "name": "หลานม่า",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/6b318efc5ca74b5c952ee4ed98ee388b.jpg",
        "type": "Drama",
        "movie_id": "M007",
        "detail": "Drama movie",
        "duration": 125,
        "role": "coming soon"
        },
        {
        "name": "The First Omen",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/075827a4cf9a45958fc70fd4ddeb8a9a.jpg",
        "type": "Horror",
        "movie_id": "M008",
        "detail": "Horror movie",
        "duration": 120,
        "role": "on showing"
        },
        {
        "name": "Mother's Instinct",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/3db8c14861e84988ac45bd3d96cc5c25.jpg",
        "type": "Thriller",
        "movie_id": "M009",
        "detail": "Thriller movie",
        "duration": 94,
        "role": "recommend"
        },
        {
        "name": "Fall Guy",
        "img": "https://img.wongnai.com/p/800x0/2024/04/11/95b0ce3451af47f3b5f7e24f847209b1.jpg",
        "type": "Action",
        "movie_id": "M010",
        "detail": "Action movie",
        "duration": 125,
        "role": "coming soon"
        },
        {
        "name": "A Quiet Place",
        "img": "https://resizing.flixster.com/bly-yHD8oiPG0BGvpfrd9q3SPco=/206x305/v2/https://resizing.flixster.com/or3jxjzmcmu88rC-mcksfO642IU=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzNmYjhmOGMzLWU1YjctNGEyNS04OTJhLWY4YmIwMjNmZmFiMC53ZWJw",
        "type": "Horror",
        "movie_id": "M011",
        "detail": "Horror movie",
        "duration": 90,
        "role": "recommend"
        },
        {
        "name": "Talk to Me",
        "img": "https://resizing.flixster.com/ejS3S8JOBfvZr_fQ_--6SyKKJpQ=/206x305/v2/https://resizing.flixster.com/9WxKriao1BmRamIaqig2k8hd5uM=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2YyZDQwYTM2LWZmYzEtNGUwMC05NzRkLTA3ODM0NThiNDE4Ny5qcGc=",
        "type": "Horror",
        "movie_id": "M012",
        "detail": "Horror movie",
        "duration": 95,
        "role": "recommend"
        },
        {
        "name": "When Evil Lurks",
        "img": "https://resizing.flixster.com/pYKve2Su8tEGhH0tDOVXySIZUeQ=/206x305/v2/https://resizing.flixster.com/jRxONmZil0CTIu8L0mZJTbLLGrY=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2FiOWRlZjQ2LTY5OTctNGRmZi1hM2IwLWI5ZWQzYmQ4ZmFkYS5qcGc=",
        "type": "Horror",
        "movie_id": "M013",
        "detail": "Horror movie",
        "duration": 99,
        "role": "recommend"
        },
        {
        "name": "The Godfather",
        "img": "https://picfiles.alphacoders.com/464/thumb-1920-464751.jpg",
        "type": "Crime",
        "movie_id": "M014",
        "detail": "Crime movie",
        "duration": 175,
        "role": "recommend"
        },
        {
        "name": "Inception",
        "img": "https://m.media-amazon.com/images/M/MV5BMjExMjkwNTQ0Nl5BMl5BanBnXkFtZTcwNTY0OTk1Mw@@._V1_.jpg",
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

    def search_person_account_id(self, account_id: str):
        for p in self.person_list:
            if p.account.account_id == account_id:
                return p
        
    def search_person_email(self, email: str):
        for p in self.person_list:
            if p.email == email:
                return p
        return False

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
        return { "Cinema_list" : [
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
                        theater_name=t.theater_name,
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
            ) for c in memory_db.cinema_list]

        }
    
    def get_cinema_by_id(self, cinema_id: int):
        for c in self.__cinema_list:
            if str(c.cinema_id) == str(cinema_id):  # Ensure comparison works for both int and str
                return c
        return None  # Return None explicitly if not found

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
                    theater_list=[TheaterResponse(
                        theater_id=t.theater_id,
                        theater_name=t.theater_name,
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
    

    def get_showtime_from_showtime_id(self,sh_id):
        for c in self.cinema_list:
            cm = c.cinema_management
            for s in cm.showtime_list:
                if s.showtime_id == sh_id:
                    return s
        return None


    def get_seat(self,showtime_id:str):
        sh = self.get_showtime_from_showtime_id(showtime_id)
        if sh :
            return {
                "Seat" :[SeatResponse(seat_id= seat.seat_id,
                                       seat_type=seat.seat_type,
                                       size=seat.size,
                                       price=seat.price,
                                       status=True,
                                       row = seat.seat_pos[0],
                                       col = int(seat.seat_pos[1:])
                                       ) for seat in sh.available_seat
                        ] 
                        + 
                        [SeatResponse(seat_id= seat.seat_id,
                                       seat_type=seat.seat_type,
                                       size=seat.size,
                                       price=seat.price,
                                       status=False,
                                       row = seat.seat_pos[0],
                                       col = int(seat.seat_pos[1:])
                                       ) for seat in sh.reserved_seat
                        ]
            }

    def get_account_from_userId(self,user_id):
        for p in self.person_list :
            if p.account.account_id == user_id:
                return p.account
        return None

    def delete_person_by_account_id(self, account_id: str):
        for p in self.person_list:
            if p.account.account_id == account_id:
                self.person_list.remove(p)
                return True
        return False
    
    def delete_movie_by_movie_id(self, movie_id: str):
        for m in self.movie_list:
            if m.movie_id == movie_id:
                self.movie_list.remove(m)
                return True
        return False

    def delete_cinema_by_cinema_id(self, cinema_id: int):
        for c in self.cinema_list:
            if c.cinema_id == cinema_id:
                self.cinema_list.remove(c)
                return True
        return False
    
    def update_cinema_by_cinema_id(self, cinema_id, name, location, region, opentime, closetime, cinema_management):
        for c in self.cinema_list:
            if c.cinema_id == cinema_id:
                c.name = name
                c.location = location
                c.region = region
                c.opentime = opentime
                c.closetime = closetime
                c.cinema_management = cinema_management
                return True
        return False
    
    def update_movie_by_movie_id(self, movie_id, name, img, movie_type, detail, duration, role):
        for m in self.movie_list:
            if m.movie_id == movie_id:
                m.name = name
                m.img = img
                m.type = movie_type
                m.detail = detail
                m.duration = duration
                m.role = role
                return True
        return False
    def put_seat(self,seat_list,user_id,showtime_id):
        acc = memory_db.get_account_from_userId(user_id)
        show = memory_db.get_showtime_from_showtime_id(showtime_id)
        for s in seat_list:
            acc.append_to_reserve_seat(s)
            show.move_seat_from_avai_to_res(s)
        return "success"
    

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
    @cinema_id.setter
    def cinema_id(self, cinema_id):
        self.__cinema_id = cinema_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def region(self):
        return self.__region
    @region.setter
    def region(self, region):
        self.__region = region

    @property
    def opentime(self):
        return self.__opentime
    @opentime.setter
    def opentime(self, opentime):
        self.__opentime = opentime

    @property
    def closetime(self):
        return self.__closetime
    @closetime.setter
    def closetime(self, closetime):
        self.__closetime = closetime

    @property
    def cinema_management(self):
        return self.__cinema_management
    @cinema_management.setter
    def cinema_management(self, cinema_management):
        self.__cinema_management = cinema_management

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
                theater_name=t.theater_name,
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
        
    def delete_theater_by_theater_id(self, theater_id: str):
        for t in self.theater_list:
            if t.theater_id == theater_id:
                self.theater_list.remove(t)
                return True
        return False

    def update_theater_by_theater_id(self, theater_id, theater_name, theater_type, seat_amount, status, audio_type, video_type, maintainance_list):
        for t in self.theater_list:
            if t.theater_id == theater_id:
                t.theater_id = theater_id
                t.theater_name = theater_name
                t.theater_type = theater_type
                t.seat_amount = seat_amount
                t.status = status
                t.audio_type = audio_type
                t.video_type = video_type
                t.maintainance_list = maintainance_list
                return True
        return False
        
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

    def update_person(self, person_to_update):
        self.account.update_account(person_to_update.account)

    def check_account_password(self, password):
        if(self.account.password == password and self.account.password != ""):
            return PersonResponse(
                name=self.name,
                tel_no=self.tel_no,
                email=self.email,
                birthday=self.birthday,
                gender=self.gender,
                account={
                    "username": self.account.username,
                    "password": self.account.password,
                    "account_id": self.account.account_id,
                    "point": self.account.point,
                    "registered_date": self.account.registered_date,
                    "expiration_date": self.account.expiration_date,
                    "history": self.account.history,
                    "document_list": self.account.document_list,
                    "reserved_list": self.account.reserved_list
                }
            )
        return False

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
        self.__reserved_list: List[str] = []

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

    def append_to_reserve_seat(self,seat_id: str):
        self.__reserved_list.append(seat_id)

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
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img):
        self.__img = img

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, movie_type):
        self.__type = movie_type

    @property
    def movie_id(self):
        return self.__movie_id
    @movie_id.setter
    def movie_id(self, movie_id):
        self.__movie_id = movie_id

    @property
    def detail(self):
        return self.__detail
    @detail.setter
    def detail(self, detail):
        self.__detail = detail

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role):
        self.__role = role

class Theater:
    def __init__(self, theater_id: str, theater_name: str, theater_type: str, seat_amount: int, status: bool, audio_type: str, video_type: str):
        self.__theater_id = theater_id
        self.__theater_name = theater_name
        self.__theater_type = theater_type
        self.__seat_amount = seat_amount
        self.__status = status
        self.__audio_type = audio_type
        self.__video_type = video_type
        self.__maintainance_list: List[Maintainance] = []

    @property
    def theater_id(self):
        return self.__theater_id
    @theater_id.setter
    def theater_id(self, theater_id):
        self.__theater_id = theater_id
    
    @property
    def theater_name(self):
        return self.__theater_name
    @theater_name.setter
    def theater_name(self, theater_name):
        self.__theater_name = theater_name
    
    @property
    def theater_type(self):
        return self.__theater_type
    @theater_type.setter
    def theater_type(self, theater_type):
        self.__theater_type = theater_type
    
    @property
    def seat_amount(self): 
        return self.__seat_amount
    @seat_amount.setter
    def seat_amount(self, seat_amount):
        self.__seat_amount = seat_amount
    
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status
    
    @property
    def audio_type(self):
        return self.__audio_type
    @audio_type.setter
    def audio_type(self, audio_type):
        self.__audio_type = audio_type
    
    @property
    def video_type(self):
        return self.__video_type
    @video_type.setter
    def video_type(self, video_type):
        self.__video_type = video_type
    
    @property
    def maintainance_list(self):
        return self.__maintainance_list
    @maintainance_list.setter
    def maintainance_list(self, maintainance_list):
        self.__maintainance_list = maintainance_list

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

    @property
    def showtime_id(self):
        return self.__showtime_id
    
    @property
    def available_seat(self):
        return self.__available_seat
    
    @property
    def reserved_seat(self):
        return self.__reserved_seat
    
    def append_avaliable_seat(self,seat:Seat):
        self.__available_seat.append(seat)

    def append_reserved_seat(self,seat:Seat):
        self.__reserved_seat.append(seat)

    def move_seat_from_avai_to_res(self, seat_id):
        for seat in self.available_seat[:]:  # Use a copy of the list to avoid modification issues
            if seat.seat_id == seat_id:
                self.available_seat.remove(seat)
                self.reserved_seat.append(seat)
                print(f"[DEBUG] Seat {seat_id} moved from available to reserved")  # Debugging
                return
        print(f"[ERROR] Seat {seat_id} was not found in available seats, cannot reserve")  # Debugging  
        
        
    def get_seat_from_id(self, seat_id):
        print(f"Searching for Seat ID: {seat_id} in Showtime {self.showtime_id}")

        # Check in available seats
        for seat in self.available_seat:
            print(f"Checking (Available) Seat ID: {seat.seat_id}")
            if seat.seat_id == seat_id:
                return seat

        # Check in reserved seats
        for seat in self.reserved_seat:
            print(f"Checking (Reserved) Seat ID: {seat.seat_id}")
            if seat.seat_id == seat_id:
                return seat

        print(f"[ERROR] Seat ID: {seat_id} NOT FOUND in Showtime {self.showtime_id}")  # Debugging
        return None

class Payment:
    def __init__(self, payment_type: str):
        self.__payment_type = payment_type

class Seat:
    def __init__(self, seat_id: str, seat_type: str, size: int, price: float, seat_pos: str):
        self.__seat_id = seat_id
        self.__seat_pos = seat_pos   # A1, A2, B1, ...............
        self.__seat_type = seat_type
        self.__size = size
        self.__price = price

    @property
    def seat_id(self):
        return self.__seat_id
    
    @property
    def seat_pos(self):
        return self.__seat_pos
    
    @property
    def seat_type(self):
        return self.__seat_type
    
    @property
    def size(self):
        return self.__size
    
    @property
    def price(self):
        return self.__price
    

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
    status: bool
    row: str
    col : int

class MaintainanceResponse(BaseModel):
    detail: str
    start_date: datetime
    end_date: datetime

class TheaterResponse(BaseModel):
    theater_id: str
    theater_name: str
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
    movie_list: List[MovieResponse]

class PersonLoginRequest(BaseModel):
    email: str
    password: str

class SeatReservationRespnd(BaseModel):
    user_id: str
    showtime_id : str
    outputSeat: List[str] 


#temporary_database
memory_db = MinorCineflex()

#create_instance
memory_db.add_person("person1", "", "person1@gmail.com", datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z"), "male", 
    Account(
        "user1", 
        "1111", 
        "Gxcw1A4e", 
        0, 
        datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z"), 
        datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z")
        )
    )
memory_db.add_person("person2", "", "person2@gmail.com", datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z"), "female", 
    Account(
        "user2", 
        "2222", 
        "sZXe32A",
        0, 
        datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z"), 
        datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S.%f%z")
        )
    )
memory_db.add_cinema(101, "minor_1", "12.001.0656", "ภาคเหนือ", time(11,00,00), time(23,00,00), CinemaManagement())
memory_db.add_cinema(102, "minor_2", "13.675.3356", "ภาคตะวันออก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(103, "minor_3", "13.675.3356", "ภาคกลาง", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(104, "minor_4", "13.675.3356", "ภาคตะวันตก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(105, "minor_5", "13.675.3356", "ภาคตะวันออกเฉียงเหนือ", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(106, "minor_6", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(107, "minor_7", "13.675.3356", "ภาคตะวันออก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(108, "minor_8", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(109, "minor_9", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(110, "minor_10", "13.675.3356", "ภาคเหนือ", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(111, "minor_11", "13.675.3356", "ภาคเหนือ", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(112, "minor_12", "13.675.3356", "ภาคตะวันออก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(113, "minor_13", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(114, "minor_14", "13.675.3356", "ภาคตะวันออก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(115, "minor_15", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(116, "minor_16", "13.675.3356", "ภาคตะวันออก", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(117, "minor_17", "13.675.3356", "กรุงเทพและปริมณฑล", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(118, "minor_18", "13.675.3356", "ภาคตะวันออกเฉียงเหนือ", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(119, "minor_19", "13.675.3356", "ภาคใต้", time(11,30,00), time(23,30,00), CinemaManagement())
memory_db.add_cinema(120, "minor_20", "13.675.3356", "ภาคใต้", time(11,30,00), time(23,30,00), CinemaManagement())
for m in movie_data["movie_list"]:
    memory_db.add_all_movie(
        m["name"], 
        m["img"],
        m["type"],
        m["movie_id"],
        m["detail"],
        m["duration"],
        m["role"]
    )
memory_db.cinema_list[0].cinema_management.add_cinema_movie("M001")
memory_db.cinema_list[0].cinema_management.add_cinema_movie("M010")

#create_theater
memory_db.cinema_list[0].cinema_management.add_cinema_theater(Theater("T-101-01", "01", "IMAX", 32, True, "Dolby", "IMAX"))
memory_db.cinema_list[0].cinema_management.add_cinema_theater(Theater("T-101-02", "02", "Standard", 32, True, "Dolby", "Standard"))
memory_db.cinema_list[1].cinema_management.add_cinema_theater(Theater("T-102-01", "01", "VIP", 32, True, "Dolby", "VIP"))
memory_db.cinema_list[1].cinema_management.add_cinema_theater(Theater("T-102-02", "02", "Standard", 32, True, "Dolby", "Standard"))

#create_showtime
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-01-001", datetime(2025, 3, 3, 12, 30, 00), "101", "T-101-01", "M001", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-01-011", datetime(2025, 3, 3, 15, 30, 00), "101", "T-101-01", "M001", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-02-002", datetime(2025, 3, 3, 15, 30, 00), "101", "T-101-02", "M010", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-02-012", datetime(2025, 3, 3, 18, 30, 00), "101", "T-101-02", "M010", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-01-003", datetime(2025, 3, 4, 18, 30, 00), "101", "T-101-01", "M002", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-02-004", datetime(2025, 3, 4, 21, 30, 00), "101", "T-101-02", "M003", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-01-005", datetime(2025, 3, 5, 21, 30, 00), "101", "T-101-01", "M004", True, False))
memory_db.cinema_list[0].cinema_management.add_cinema_showtime(Showtime("S-101-02-006", datetime(2025, 3, 5, 12, 30, 00), "101", "T-101-02", "M005", True, False))

#name_protocol
#theater_id = T-{cinema_id}-{theater_name} ex. T-101-01 T-101-02
#showtime_id = S-{cinema_id}-{theater_name}-{showtime_number} ex. S-101-01-001 S-101-01-002
#seat_id = ST-{cinema_id}-{theater_name}-{showtime_number}-{seat_number} ex. ST-101-01-001-001 ST-101-01-001-002 

#create seat instance ;-;
for show in memory_db.cinema_list[0].cinema_management.showtime_list:
    s_id = show.showtime_id
    s_id = s_id[1:]
    for row in range(1,5):
        for col in range(1,9):
            show.append_avaliable_seat(Seat(
                seat_id = f"ST{s_id}-{str(8*(row-1) + col).zfill(3)}",
                seat_type = "Delux",
                size = 1,
                price = 100,
                seat_pos = f"{chr(64 + row)}{col}"
            ))

#temp
sh = memory_db.get_showtime_from_showtime_id("S-101-01-001")            
sh.move_seat_from_avai_to_res("ST-101-01-001-001")
sh.move_seat_from_avai_to_res("ST-101-01-001-002")
sh.move_seat_from_avai_to_res("ST-101-01-001-003")
sh.move_seat_from_avai_to_res("ST-101-01-001-004")
sh.move_seat_from_avai_to_res("ST-101-01-001-018")
sh.move_seat_from_avai_to_res("ST-101-01-001-019")

#system
@app.get("/minorcineflex")
def system():
    return memory_db.get_system()

#person
@app.get("/minorcineflex/person")
def person():
    return memory_db.get_person()

@app.get("/minorcineflex/person/email/{account_id}")
def account_id(account_id: str):
    p = memory_db.search_person_account_id(account_id)
    return PersonResponse(name=p.name, tel_no=p.tel_no, email=p.email, birthday=p.birthday, gender=p.gender, account={
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
                )

@app.get("/minorcineflex/person/{email}")
def email(email: str):
    p = memory_db.search_person_email(email)
    if(p):
        return PersonResponse(name=p.name, tel_no=p.tel_no, email=p.email, birthday=p.birthday, gender=p.gender, account={
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
                    )

@app.post("/minorcineflex/add_person")
def add_person(person: PersonRequest):
    memory_db.add_person(
        name=person.name,
        tel_no=person.tel_no,
        email=person.email,
        birthday=str(person.birthday),
        gender=person.gender,
        account=Account
            (
                username=person.account.username,
                password=person.account.password,
                account_id=person.account.account_id,
                point=person.account.point,
                registered_date=str(person.account.registered_date),
                expiration_date=str(person.account.expiration_date)
            )
    )
    return {"message": "Person added successfully"}

@app.put("/minorcineflex/update_person")
def update_person(person: PersonRequest):
    p = memory_db.search_person_account_id(person.account.account_id)
    if(p):
        p.update_person(person)
        return {"message": "Person and account updated successfully"}
    return {"error": "Person not found"}

@app.delete("/minorcineflex/delete_person/{account_id}")
def delete_person(account_id: str):
    person = memory_db.search_person_account_id(account_id)
    if person:
        if memory_db.delete_person_by_account_id(account_id):
            return {"message": "Person deleted successfully"}
        else:
            return {"error": "Person not found"}
    return {"error": "Person not found"}

#Login 
@app.post("/minorcineflex/login")
def login(login_request: PersonLoginRequest):
    p = memory_db.search_person_email(login_request.email)
    if not p:
        raise HTTPException(status_code=404, detail="Not found an email ")
    is_valid = p.check_account_password(login_request.password)
    print(is_valid)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return is_valid

#movie
@app.get("/minorcineflex/movie")
def movie():
    return memory_db.get_movie()

@app.post("/minorcineflex/add_movie")
def add_movie(movie: MovieResponse):
    memory_db.add_all_movie(
        name=movie.name,
        img=movie.img,
        movie_type=movie.type,
        movie_id=movie.movie_id,
        detail=movie.detail,
        duration=movie.duration,
        role=movie.role
    )
    return {"message": "Movie added successfully"}

@app.put("/minorcineflex/update_movie/{movie_id}")
def update_movie(movie_id: str, updated_movie: MovieResponse):
    success = memory_db.update_movie_by_movie_id(
        movie_id=movie_id,
        name=updated_movie.name,
        img=updated_movie.img,
        movie_type=updated_movie.type,
        detail=updated_movie.detail,
        duration=updated_movie.duration,
        role=updated_movie.role
    )
    if success:
        return {"message": "Movie updated successfully"}
    return {"error": "Movie not found"}

@app.delete("/minorcineflex/delete_movie/{movie_id}")
def delete_movie(movie_id: str):
    if memory_db.delete_movie_by_movie_id(movie_id):
        return {"message": "Movie deleted successfully"}
    return {"error": "Movie not found"}

#cinema
@app.get("/minorcineflex/cinema")
def cinema():
    return memory_db.get_cinema()

@app.post("/minorcineflex/add_cinema")
def add_cinema(cinema: CinemaResponse):
    memory_db.add_cinema(
        id=cinema.cinema_id,
        name=cinema.name,
        location=cinema.location,
        region=cinema.region,
        opentime=cinema.opentime,
        closetime=cinema.closetime,
        cinema_management=cinema.cinema_management
    )
    return {"message": "Cinema added successfully"}

@app.delete("/minorcineflex/delete_cinema/{cinema_id}")
def delete_cinema(cinema_id: int):
    if memory_db.delete_cinema_by_cinema_id(cinema_id):
        return {"message": "Cinema deleted successfully"}
    return {"error": "Cinema not found"}

@app.put("/minorcineflex/update_cinema/{cinema_id}")
def update_cinema(cinema_id: int, updated_cinema: CinemaResponse):
    success = memory_db.update_cinema_by_cinema_id(
        cinema_id=cinema_id,
        name=updated_cinema.name,
        location=updated_cinema.location,
        region=updated_cinema.region,
        opentime=updated_cinema.opentime,
        closetime=updated_cinema.closetime,
        cinema_management=updated_cinema.cinema_management
    )
    if success:
        return {"message": "Cinema updated successfully"}
    return {"error": "Cinema not found"}

#theater
@app.get("/minorcineflex/cinema/{cinema_id}/theater")
def theater_list(cinema_id: int):
    return memory_db.get_cinema_by_id(cinema_id).cinema_management.get_theater()

@app.post("/minorcineflex/cinema/{cinema_id}/add_theater")
def add_theater(cinema_id: int, theater: TheaterResponse):
    memory_db.get_cinema_by_id(cinema_id).cinema_management.add_cinema_theater(Theater(
        theater_id=theater.theater_id,
        theater_name=theater.theater_name,
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

@app.put("/minorcineflex/cinema/{cinema_id}/update_theater/{theater_id}")
def update_theater(cinema_id: int, theater_id: str, updated_theater: TheaterResponse):
    if memory_db.get_cinema_by_id(cinema_id).cinema_management.update_theater_by_theater_id(
        theater_id=theater_id,
        theater_name=updated_theater.theater_name,
        theater_type=updated_theater.theater_type,
        seat_amount=updated_theater.seat_amount,
        status=updated_theater.status,
        audio_type=updated_theater.audio_type,
        video_type=updated_theater.video_type,
        maintainance_list=updated_theater.maintainance_list
    ):
        return {"message": "Theater updated successfully"}
    return {"error": "Theater not found"}

@app.delete("/minorcineflex/cinema/{cinema_id}/delete_theater/{theater_id}")
def delete_theater(cinema_id: int, theater_id: str):
    if memory_db.get_cinema_by_id(cinema_id).cinema_management.delete_theater_by_theater_id(theater_id):
        return {"message": "Theater deleted successfully"}
    return {"error": "Theater not found"}

#getseat
@app.get("/minorcineflex/seat/{showtime_id}")
def seat(showtime_id:str):
    return memory_db.get_seat(showtime_id)



@app.put("/minorcineflex/reserve_seat")
def reserved_seat(input: SeatReservationRespnd):
    seat_list = input.outputSeat
    user_id = input.user_id
    showtime_id  = input.showtime_id

    memory_db.put_seat(seat_list,user_id,showtime_id)

    return 
        
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

# -------------------------------------------------------------------------------------- payment page --------------------------------------------------------------------------------------
# Initiate payment - returns the amount to be paid
@app.post("/minorcineflex/base_payment")
def base_payment(user_id: str, movie_id: str, showtime_id: str, payment_type: str):
    # Retrieve user account
    account = memory_db.get_account_from_userId(user_id)
    if not account:
        raise HTTPException(status_code=404, detail="User not found")

    # Retrieve showtime
    showtime = memory_db.get_showtime_from_showtime_id(showtime_id)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    # Retrieve movie
    movie = next((m for m in memory_db.movie_list if m.movie_id == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Fetch reserved seats
    reserved_seat_ids = account.reserved_list
    if not reserved_seat_ids:
        raise HTTPException(status_code=400, detail="No seats reserved for this user")
    print(f"Reserved Seat IDs: {reserved_seat_ids}")
    
    reserved_seat_ids = account.reserved_list
    print(f"[DEBUG] Reserved seats for user {user_id}: {reserved_seat_ids}")
    # Calculate total price
    total_price = 0
    for seat_id in reserved_seat_ids:
        seat_obj = memory_db.get_showtime_from_showtime_id(showtime_id).get_seat_from_id(seat_id)
        if seat_obj:
            print(f"Seat ID: {seat_id}, Price: {seat_obj.price}")  # Debugging
            total_price += seat_obj.price
        else:
            print(f"Seat ID: {seat_id} NOT FOUND")  # Debugging

    return {
        "message": "Proceed to payment",
        "user_id": user_id,
        "movie_id": movie_id,
        "showtime_id": showtime_id,
        "total_price": total_price,
        "payment_method": payment_type,
        "reserved_seats": reserved_seat_ids
    }


# Finalize payment - Creates booking if payment is successful
@app.post("/minorcineflex/done_payment")
def done_payment(user_id: str, movie_id: str, showtime_id: str, payment_type: str):
    # Retrieve user account
    account = memory_db.get_account_from_userId(user_id)
    if not account:
        raise HTTPException(status_code=404, detail="User not found")

    # Retrieve showtime
    showtime = memory_db.get_showtime_from_showtime_id(showtime_id)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    # Retrieve movie
    movie = next((m for m in memory_db.movie_list if m.movie_id == movie_id), None)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Fetch reserved seats
    reserved_seat_ids = account.reserved_list
    if not reserved_seat_ids:
        raise HTTPException(status_code=400, detail="No seats reserved for this user")

    # Check if cinema exists
    cinema = memory_db.get_cinema_by_id(showtime.cinema_id)
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")

    # Ensure seats are not already booked
    if reserved_seat_ids in cinema.cinema_management.booking_list:
        raise HTTPException(status_code=400, detail="Seats have already been booked")

    # Calculate total price
    total_price = sum(
        memory_db.get_showtime_from_showtime_id(showtime_id).get_seat_from_id(seat_id).price
        for seat_id in reserved_seat_ids
        if memory_db.get_showtime_from_showtime_id(showtime_id).get_seat_from_id(seat_id) is not None
    )

    # Create a payment instance
    payment = Payment(payment_type=payment_type)

    # Retrieve actual Seat objects
    seat_objects = [
        memory_db.get_showtime_from_showtime_id(showtime_id).get_seat_from_id(seat_id)
        for seat_id in reserved_seat_ids
        if memory_db.get_showtime_from_showtime_id(showtime_id).get_seat_from_id(seat_id) is not None
    ]

    # Create a booking instance
    booking = Booking(
        showtime=showtime,
        account_id=user_id,
        seat_list=seat_objects,
        booking_date=datetime.now(),
        payment_method=payment,
        total=total_price
    )

    # Add booking to user history
    account.history.append(booking)

    # Add booking to cinema management's booking list
    cinema.cinema_management.booking_list.append(booking)

    return {
        "message": "Payment completed and booking created successfully",
        "user_id": user_id,
        "movie_id": movie_id,
        "showtime_id": showtime_id,
        "total_price": total_price,
        "payment_method": payment_type,
        "reserved_seats": reserved_seat_ids
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)