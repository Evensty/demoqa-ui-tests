from selene import have
from selene.support.shared import browser
import allure
from allure import step
from allure_commons.types import Severity

from demoqa.model.controls.datepicker import Datepicker
from demoqa.model.controls.checkbox import CheckBox
from demoqa.model.controls.dropdown import Dropdown
from demoqa.model.controls.radio import Radio
from demoqa.model.controls.uploader import Uploader


class PracticePage:
    def __init__(self, user):
        self.user = user

    def set_fullname(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)

    def set_email(self):
        browser.element('#userEmail').type(self.user.email)

    def select_gender(self):
        gender = Radio()
        gender.select(f'[value={self.user.gender}]~[for^=gender-radio]')

    def set_mobile_number(self):
        browser.element('#userNumber[placeholder="Mobile Number"]').type(self.user.phone)

    def set_birthday(self):
        birthday = Datepicker()
        birthday.set_date(self.user.month, self.user.year, self.user.day)

    def set_subjects(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

    def select_hobbies(self):
        hobby = CheckBox()
        hobby.select(by_text=self.user.hobbies)

    def select_picture(self):
        uploader = Uploader()
        uploader.attach('#uploadPicture', file=self.user.image)

    def set_current_address(self):
        browser.element('#currentAddress[placeholder="Current Address"]').type(self.user.address)

    def select_state(self):
        state = Dropdown()
        state.select('#state', by_text=self.user.state)

    def select_city(self):
        city = Dropdown()
        city.select('#city', by_text=self.user.city)

    def submit(self):
        browser.element('.form-file').submit()

    def fill_form(self):
        allure.dynamic.tag("web")
        allure.dynamic.severity(Severity.BLOCKER)
        allure.dynamic.story("Проверка формы регистрации")
        with step("Переходим на страницу заполнения формы"):
            browser.open('https://demoqa.com/automation-practice-form')
        with step("Вводим имя"):
            self.set_fullname()
        with step("Вводим почту"):
            self.set_email()
        with step("Указываем пол"):
            self.select_gender()
        with step("Вводим номер телефона"):
            self.set_mobile_number()
        with step("Указываем дату рождения"):
            self.set_birthday()
        with step("Указываем предметы"):
            self.set_subjects()
        with step("Выбираем хобби"):
            self.select_hobbies()
        with step('Прикладываем картинку'):
            self.select_picture()
        with step("Указываем адрес"):
            self.set_current_address()
        with step("Выбираем штат"):
            self.select_state()
        with step("Выбираем город"):
            self.select_city()
        with step("Подтверждаем регистрацию"):
            self.submit()

    def check_results(self):
        with step("Проверяем форму на корректное заполнение"):
            browser.element('.table').all('td').even.should(have.texts(
                f'{self.user.first_name} {self.user.last_name}',
                self.user.email,
                self.user.gender,
                self.user.phone,
                f'{self.user.day} May,{self.user.year}',
                self.user.subject,
                self.user.hobbies,
                self.user.image,
                self.user.address,
                f'{self.user.state} {self.user.city}'))


