import os
import time

from selene import browser, have, be
from selene.support.shared import browser
from selene.support.conditions import be
from selenium.webdriver.common.by import By


def test_sending_form(new_setup_for_browser):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element("#firstName").type("Daniil")
    browser.element("#lastName").type("Zhuravlev")
    browser.element("#userEmail").type("butmanovich@yandex.ru")

    browser.element('[for="gender-radio-1"]').click()

    browser.element("#userNumber").type("7999512555")

    browser.element("#dateOfBirthInput").click()
    browser.element("option[value='2'").click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2002"]').click()
    browser.element('.react-datepicker__day--023').click()

    browser.element("#subjectsInput").type("English").press_enter()
    browser.element("#subjectsInput").type("Computer Science").press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element("#uploadPicture").set_value(os.path.abspath('img/123123.png'))

    browser.element('#currentAddress').type("г.Москва, Покровка, 5")

    browser.element('#state').click()
    browser.all('div[class*="option"]').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.all('div[class*="option"]').element_by(have.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))

    browser.all('td').should(have.texts([
        'Student Name', 'Daniil Zhuravlev',
        'Student Email', 'butmanovich@yandex.ru',
        'Gender', 'Male',
        'Mobile', '7999512555',
        'Date of Birth', '23 March,2002',
        'Subjects', 'English, Computer Science',
        'Hobbies', 'Sports',
        'Picture', '123123.png',
        'Address', 'г.Москва, Покровка, 5',
        'State and City', 'NCR Delhi'
        ]
    ))
    browser.element('#closeLargeModal').click()
    time.sleep(2)
