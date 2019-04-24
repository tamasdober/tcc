from selenium.webdriver.common.by import By


class ContactPageLocators:
    FIRST_NAME = (By.XPATH, "//input[contains(@id,'firstname')]")
    JOB_TITLE = (By.XPATH, "//input[contains(@id,'jobtitle')]")
    EMAIL = (By.XPATH, "//input[contains(@id,'email')]")
    PHONE = (By.XPATH, "//input[contains(@id,'phone')]")
    COMPANY = (By.XPATH, "//input[contains(@id,'company')]")
    COMPANY_SIZE = (By.XPATH, "//input[contains(@id,'company_size')]")
    STATE = (By.XPATH, "//input[contains(@id,'state')]")
    INDUSTRY = (By.XPATH, "//input[contains(@id,'industry')]")
    SUBMIT = (By.CLASS_NAME, "hs-button")
    THANK_YOU_MESSAGE = (
        By.XPATH, "//*[contains(text(), 'Thanks for reaching out! A representative will be in touch shortly.')]")
