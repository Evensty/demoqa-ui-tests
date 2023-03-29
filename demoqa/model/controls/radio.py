from selene.support.shared import browser


class Radio:
    def select(self, selector):
        browser.element(selector).click()
