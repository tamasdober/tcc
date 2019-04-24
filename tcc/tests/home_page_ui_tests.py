import logging
from os import environ
from unittest import TestCase

from selenium import webdriver

from tcc.pom.pages.home_page import HomePage
from tcc.utilities.constants import CHROME_DRIVER
from tcc.utilities.custom_logger import custom_logger


class HomePageTests(TestCase):
    log = custom_logger(logging.DEBUG)

    def setUp(self):
        options = webdriver.ChromeOptions()
        # no specific reason to use options.add_argument('..')
        self.driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=options)
        self.base_path = environ.get("base_path")

    def test_home_page_displays(self):
        home_page = HomePage(self.driver, self.base_path)
        home_page.load()
        page_url = home_page.url
        self.assertEqual(page_url, "https://taxcreditco.com")

    def test_home_page_contact_button_available(self):
        home_page = HomePage(self.driver, self.base_path)
        home_page.load()
        contact_button_text = home_page.contact_button().text
        self.assertEqual(contact_button_text, "Contact")

    def tearDown(self):
        self.driver.quit()
