from selene import have
from selene.support.shared import browser


class CheckBox:
    def select(self, by_text):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(by_text)).click()


