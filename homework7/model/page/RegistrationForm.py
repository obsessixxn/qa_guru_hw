import os

from selene import browser, have


class RegistrationFormPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_name(self, name):
        browser.element("#firstName").type(name)

    def fill_surname(self, name):
        browser.element("#lastName").type(name)

    def fill_email(self, email):
        browser.element("#userEmail").type(email)

    def choose_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()

    def fill_number(self, value):
        browser.element("#userNumber").type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def choose_subject(self, value):
        browser.element("#subjectsInput").type(value).press_enter()

    def choose_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def choose_photo(self, value):
        browser.element("#uploadPicture").set_value(os.path.abspath(f'resources/{value}'))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        browser.element('#state').click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()

    def choose_city(self, value):
        browser.element('#city').click()
        browser.all('div[class*="option"]').element_by(have.text(value)).click()

    def submit_form(self):
        browser.element('#submit').click()

    def should_registered_student_with(self, full_name, email, gender, number, date_of_birth,
                                       subject, hobby, photo, address, state, city):
        browser.element('.table').all('td').even.should(have.texts([
            full_name,
            email,
            gender,
            number,
            date_of_birth,
            subject,
            hobby,
            photo,
            address,
            state + ' ' + city
        ]
        ))
