from selene.support.shared import browser
from selene import have
from demoqa.model.controls import dropdown, uploader, checkbox, datepicker, radio


def set_first_name(value):
    browser.element('#firstName').set_value(value)


def set_last_name(value):
    browser.element('#lastName').set_value(value)


def set_email(value):
    browser.element('#userEmail').set_value(value)


def select_gender(gender):
    radio.select(f'[value={gender}]~[for^=gender-radio]')


def set_mobile_number(value):
    browser.element('#userNumber[placeholder="Mobile Number"]').set_value(value)


def set_birthday( month, year, day):
    datepicker.set_date(month=month, year=year, day=day)


def set_subjects(value):
    browser.element('#subjectsInput').set_value(value)


def select_hobbies(value):
    checkbox.select('[for^=hobbies-checkbox]', by_text=value)


def select_picture(file):
    uploader.attach('#uploadPicture', file=file)


def set_current_address(value):
    browser.element('#currentAddress[placeholder="Current Address"]').set_value(value)


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def submit():
    browser.element('.form-file').submit()


def check_results(*texts):
    browser.all('.table tr td ~td').should(have.texts(*texts))
