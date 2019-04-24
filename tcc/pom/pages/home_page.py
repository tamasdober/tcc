from tcc.pom.locators.home_page_locators import HomePageLocators
from tcc.pom.pages.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return super().url

    @property
    def submit(self):
        return self.driver.find_element(*HomePageLocators.CONTACT_BUTTON)

    def contact_button(self):
        return self.driver.find_element(*HomePageLocators.CONTACT_BUTTON)
