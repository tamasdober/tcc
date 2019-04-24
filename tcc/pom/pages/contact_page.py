from tcc.pom.locators.contact_page_locators import ContactPageLocators
from tcc.pom.pages.base_page import BasePage


class ContactPage(BasePage):

    @property
    def url(self):
        return super().url + "/contact/"

    @property
    def first_name(self):
        return self.driver.find_element(*ContactPageLocators.FIRST_NAME)

    @property
    def jobtitle(self):
        return self.driver.find_element(*ContactPageLocators.JOB_TITLE)

    @property
    def email(self):
        return self.driver.find_element(*ContactPageLocators.EMAIL)

    @property
    def phone(self):
        return self.driver.find_element(*ContactPageLocators.PHONE)

    @property
    def company(self):
        return self.driver.find_element(*ContactPageLocators.COMPANY)

    @property
    def company_size(self):
        return self.driver.find_element(*ContactPageLocators.COMPANY_SIZE)

    @property
    def state(self):
        return self.driver.find_element(*ContactPageLocators.STATE)

    @property
    def industry(self):
        return self.driver.find_element(*ContactPageLocators.INDUSTRY)

    @property
    def message(self):
        return self.driver.find_element(*ContactPageLocators.MESSAGE)

    @property
    def submit(self):
        return self.driver.find_element(*ContactPageLocators.SUBMIT)

    def read_message(self):
        return self.driver.find_element(*ContactPageLocators.THANK_YOU_MESSAGE)
