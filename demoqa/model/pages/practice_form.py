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
from demoqa.model.data.user import User
from demoqa.utils.remove_ads import remove_junk_ads


class PracticePage:
    def __init__(self, user: User):
        self.user = user

    def set_fullname(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        return self

    def set_email(self, user):
        browser.element('#userEmail').type(user.email)
        return self

    def select_gender(self, user):
        gender = Radio()
        gender.select(f'[value={user.gender}]~[for^=gender-radio]')
        return self

    def set_mobile_number(self, user):
        browser.element('#userNumber[placeholder="Mobile Number"]').type(user.phone)
        return self

    def set_birthday(self, user):
        birthday = Datepicker()
        birthday.set_date(user.month, user.year, user.day)
        return self

    def set_subjects(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def select_hobbies(self, user):
        hobby = CheckBox()
        hobby.select(by_text=user.hobbies)
        return self

    def select_picture(self, user):
        uploader = Uploader()
        uploader.attach('#uploadPicture', file=user.image)
        return self

    def set_current_address(self, user):
        browser.element('#currentAddress[placeholder="Current Address"]').type(user.address)
        return self

    def select_state(self, user):
        state = Dropdown()
        state.select('#state', by_text=user.state)
        return self

    def select_city(self, user):
        city = Dropdown()
        city.select('#city', by_text=user.city)
        return self

    def submit(self):
        browser.element('.form-file').submit()
        return self

    def fill_form(self, user):
        with step("Переходим на страницу заполнения формы"):
            browser.open('https://demoqa.com/automation-practice-form')
            remove_junk_ads(browser)
        with step("Вводим имя"):
            self.set_fullname(user)
        with step("Вводим почту"):
            self.set_email(user)
        with step("Указываем пол"):
            self.select_gender(user)
        with step("Вводим номер телефона"):
            self.set_mobile_number(user)
        with step("Указываем дату рождения"):
            self.set_birthday(user)
        with step("Указываем предметы"):
            self.set_subjects(user)
        with step("Выбираем хобби"):
            self.select_hobbies(user)
        with step('Прикладываем картинку'):
            self.select_picture(user)
        with step("Указываем адрес"):
            self.set_current_address(user)
        with step("Выбираем штат"):
            self.select_state(user)
        with step("Выбираем город"):
            self.select_city(user)
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

    def check_validation_phone_number(self):
        with allure.step('Проверяем номер телефона'):
            browser.element('#userNumber') \
                .should(have.css_property('border-color', value='rgb(220, 53, 69)'))
            return self

    def check_validation_first_name(self):
        browser.element('#firstName') \
            .should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self

    def check_validation_last_name(self):
        browser.element('#lastName') \
            .should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self

    def check_validation_gender(self):
        browser.element('[for^="gender-radio"]') \
            .should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self


