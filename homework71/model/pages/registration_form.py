import os
from typing import Literal

from selene import browser, have

from homework71.model.pages.submitting_form_page import SubmittingFormPage
from homework71.model.users.users import User, Subject, Hobbies


class RegistrationPage:
    def __init__(self):
        self.info = SubmittingFormPage()

        self._first_name = browser.element("#firstName")
        self._last_name = browser.element("#lastName")
        self._email = browser.element("#userEmail")
        self._phone = browser.element("#userNumber")
        self._address = browser.element('#currentAddress')
        self._gender_male = browser.element('[for="gender-radio-1"]')
        self._gender_female = browser.element('[for="gender-radio-2"]')
        self._gender_others = browser.element('[for="gender-radio-3"]')

        self._dob_input = browser.element('#dateOfBirthInput')
        self._dob_year_select = browser.element('.react-datepicker__year-select')
        self._dob_month_select = browser.element('.react-datepicker__month-select')

        self._subjects = browser.element("#subjectsInput")
        self._subjects_box = browser.element('#subjectsContainer')

        self._hobby_sports = browser.element('label[for="hobbies-checkbox-1"]')
        self._hobby_reading = browser.element('label[for="hobbies-checkbox-2"]')
        self._hobby_music = browser.element('label[for="hobbies-checkbox-3"]')

        self._upload = browser.element("#uploadPicture")

        self._state = browser.element('#state')
        self._city = browser.element('#city')
        self._choose_city = browser.all('div[class*="option"]')

        self._submit = browser.element('#submit')

        self._hobbies = {
            'Sports':  self._hobby_sports,
            'Reading': self._hobby_reading,
            'Music':   self._hobby_music,
        }

        self._subject = Subject

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, name):
        self._first_name.type(name)
        return self

    def fill_last_name(self, surname):
        self._last_name.type(surname)
        return self

    def fill_email(self, email):
        self._email.type(email)
        return self

    def fill_phone(self, phone):
        self._phone.type(phone)
        return self

    def fill_gender_male(self):
        self._gender_male.click()
        return self

    def fill_date_of_birth(self, year, month, day):
        self._dob_input.click()
        self._dob_year_select.click()
        browser.element(f'option[value="{int(year)}"]').click()
        self._dob_month_select.click()
        browser.element(f'option[value="{int(month)-1}"]').click()
        browser.element(
            f'.react-datepicker__day--0{int(day):02d}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value: Literal['Music', 'Sports']):
        self._subjects_box.click()
        self._subjects.type(value).press_enter()
        return self

    def fill_hobbies(self, value: Literal['Sports', 'Reading', 'Music']):
        self._hobbies[value].click()
        return self

    def upload_file(self, value):
        self._upload.set_value(os.path.abspath(f'resources/{value}'))
        return self

    def fill_state(self, value):
        self._state.click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()
        return self

    def fill_address(self, value):
        self._address.type(value)
        return self

    def fill_city(self, value):
        self._city.click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()
        return self

    def submit_form(self):
        self._submit.click()
        return self

    def filling_form(self, user: User):
        first, last = user.full_name.split(' ', 1)
        subjects = [s.value if isinstance(s, Subject) else str(s) for s in user.subjects]
        hobbies = [h.value if isinstance(h, Hobbies) else str(h) for h in user.hobbies]
        state_city = user.state_and_city.split()
        state, city = state_city[0], state_city[1]
        (self
         .fill_first_name(first)
         .fill_last_name(last)
         .fill_email(user.email)
         .fill_phone(user.number)
         .fill_address(user.address)
         .fill_gender_male()
         .fill_date_of_birth(user.date_of_birth.year,
                             user.date_of_birth.month,
                             user.date_of_birth.day)
         )
        for s in subjects:
            self.fill_subjects(s)
        for h in hobbies:
            self.fill_hobbies(h)
        (self
         .fill_state(state)
         .fill_city(city)
         .upload_file(user.upload_file)
         )

        self.submit_form()
        return self
