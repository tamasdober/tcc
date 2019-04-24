import logging
import time
from os import environ
from unittest import TestCase

from selenium import webdriver

from tcc.pom.pages.contact_page import ContactPage
from tcc.pom.pages.home_page import HomePage
from tcc.utilities.constants import CHROME_DRIVER
from tcc.utilities.custom_logger import custom_logger


class ContactPageTests(TestCase):
    log = custom_logger(logging.DEBUG)

    def setUp(self):
        options = webdriver.ChromeOptions()
        # no specific reason to use options.add_argument('..')
        self.driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
        self.base_path = environ.get("base_path")
        home_page = HomePage(self.driver, self.base_path)
        home_page.load()
        home_page.submit.click()

    def test_contact_page_displays(self):
        contact_page = ContactPage(self.driver, self.base_path)
        page_url = contact_page.url
        self.assertEqual(page_url, "https://taxcreditco.com/contact/")

    def test_filling_in_contact_form(self):
        contact_page = ContactPage(self.driver, self.base_path)
        contact_page.first_name.send_keys("test")
        contact_page.jobtitle.send_keys("test")
        contact_page.email.send_keys("test@test.com")
        contact_page.phone.send_keys("333-555-4444")
        contact_page.company.send_keys("test")
        contact_page.company_size.send_keys("test")
        contact_page.state.send_keys("test")
        contact_page.industry.send_keys("test")
        contact_page.submit.click()
        self.log.debug("submitted form")
        # TODO: use WebDriverWait instead of sleep
        time.sleep(5)
        message = contact_page.read_message().text
        self.assertEqual(message, "Thanks for reaching out! A representative will be in touch shortly.")

    def tearDown(self):
        self.driver.quit()
