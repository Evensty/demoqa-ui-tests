from selene.support.shared import browser


class Datepicker:
    def set_date(self, month, year, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select>option[value="{month - 1}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select>option[value="{year}"]').click()
        if 0 < day < 10:
            browser.element(f'[class ^=react-datepicker__day].react-datepicker__day--00{day}').click()
        else:
            browser.element(f'[class ^=react-datepicker__day].react-datepicker__day--0{day}').click()









