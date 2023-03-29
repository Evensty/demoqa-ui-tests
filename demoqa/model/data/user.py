from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    month: int
    year: int
    day: int
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Ivan',
    last_name='Petrov',
    email='test_practice_form@mail.ru',
    phone='8999577120',
    address='Starokolpaksky alley',
    month=5,
    year=1920,
    day=21,
    gender='Other',
    subject='Maths',
    hobbies='Reading',
    image='test_image.png',
    state='Uttar Pradesh',
    city='Lucknow')


