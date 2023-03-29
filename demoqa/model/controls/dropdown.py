from selene import have
from selene.support.shared import browser


class Dropdown:
    def select(self, selector, /, *, by_text):
        browser.element(selector).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(by_text)).click()



