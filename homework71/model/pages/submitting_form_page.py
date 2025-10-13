from datetime import date

from selene import have, browser

from homework71.model.users.users import User, Hobbies, Subject

MONTHS = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def format_date(d) -> str:
    if isinstance(d, date):
        return f"{d.day:02d} {MONTHS[d.month]},{d.year}"
    return str(d)


def format_hobbies(hobbies) -> str:
    if isinstance(hobbies, list):
        return ', '.join(h.value if isinstance(h, Hobbies) else str(h) for h in hobbies)
    if isinstance(hobbies, Hobbies):
        return hobbies.value


def format_subject(subject) -> str:
    if isinstance(subject, list):
        return ', '.join(s.value if isinstance(s, Subject) else str(s) for s in Subject)
    if isinstance(subject, Hobbies):
        return subject.value


class SubmittingFormPage:

    def should_have_data(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.full_name,
                user.email,
                user.gender,
                user.number,
                format_date(user.date_of_birth),
                format_subject(user.subjects),
                format_hobbies(user.hobbies),
                user.upload_file,
                user.address,
                user.state_and_city,
            )
        )
        return self
