import dataclasses

import enum
from datetime import date


class Subject(enum.Enum):
    english = 'English'
    chemistry = 'Chemistry'


class Hobbies(enum.Enum):
    Reading = 'Reading'
    Music = 'Music'
    Sports = 'Sports'


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    gender: str
    number: str
    date_of_birth: date
    subjects: list[Subject]
    hobbies: list[Hobbies]
    upload_file: str
    address: str
    state_and_city: str


guest = User(
    full_name="John Doe",
    email="JohnDoe@gmail.com",
    gender="Male",
    number="1234567890",
    date_of_birth=date(2001, 3, 3),
    subjects=[Subject.english, Subject.chemistry],
    hobbies=[Hobbies.Music, Hobbies.Sports],
    upload_file="123123.png",
    address="Saint-Petersburg, Central Street 3",
    state_and_city="NCR Delhi",
)
