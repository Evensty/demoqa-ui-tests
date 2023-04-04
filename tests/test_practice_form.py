import allure
import pytest
from allure_commons.types import Severity
from selene import browser

from demoqa.model.data.user import test_user
from demoqa.model.pages.practice_form import PracticePage


@allure.label('owner', 'Maxim Veselov')
@allure.severity(Severity.NORMAL)
@allure.story("Registration form")
@allure.tag('web')
@allure.feature('Successful completion of the form')
@pytest.mark.parametrize('screen_size', ["720x1280", "1920x1080"])
def test_practice_form(setup_browser, screen_size):
    width, height = screen_size.split('x')
    setup_browser.config.window_width = int(width)
    setup_browser.config.window_height = int(height)
    practice_form = PracticePage(test_user)
    practice_form.fill_form(test_user)
    practice_form.check_results()



@allure.label('owner', 'Maxim Veselov')
@allure.severity(Severity.NORMAL)
@allure.story("Registration form")
@allure.tag('web')
@allure.feature('Successful completion of the form with only required fields')
def test_fill_only_required_fields():
    practice_form = PracticePage(test_user)
    browser.open('https://demoqa.com/automation-practice-form')
    practice_form.set_fullname(test_user) \
        .select_gender(test_user) \
        .set_current_address(test_user) \
        .submit()


@allure.label('owner', 'Maxim Veselov')
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.feature('Check validation count numbers less then ten')
def test_validation_count_numbers_less_than_ten():
    practice_form = PracticePage(test_user)
    browser.open('https://demoqa.com/automation-practice-form')
    practice_form.set_fullname(test_user) \
        .select_gender(test_user) \
        .set_current_address(test_user) \
        .submit()
    practice_form.check_validation_phone_number()


@allure.label('owner', 'Maxim Veselov')
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.story("Registration form")
@allure.feature("Forms")
@allure.feature('Check validation count numbers less then ten')
def test_submit_empty_form():
    practice_form = PracticePage(test_user)
    browser.open('https://demoqa.com/automation-practice-form')
    practice_form.submit()
    practice_form.check_validation_first_name()\
        .check_validation_last_name()\
        .check_validation_gender()\
        .check_validation_phone_number()



