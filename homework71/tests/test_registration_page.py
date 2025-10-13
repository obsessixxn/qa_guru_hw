from homework71.model.users import users
from homework71.model.pages.registration_form import RegistrationPage


def test_registration_page(new_setup_for_browser):

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.filling_form(users.guest)
    registration_page.info.should_have_data(users.guest)
