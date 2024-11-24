import pytest
from faker import Faker
from gateway.domain.exceptions.users import InvalidEmailError, InvalidPasswordError
from gateway.domain.values.users import CleanPassword, Email


def test_email_value_correct(faker: Faker):
    email = faker.email()

    email_value = Email(email)

    assert email_value.value == email
    assert email_value.as_generic_type() == email


def test_email_value_incorrect():
    email = "invalid@email"

    with pytest.raises(InvalidEmailError):
        Email(email)


def test_password_value_correct(faker: Faker):
    password = faker.password(length=12)

    password_value = CleanPassword(password)

    assert password_value.value == password
    assert password_value.as_generic_type() == password


def test_password_value_incorrect(faker: Faker):
    password_without_special = faker.password(length=12, special_chars=False)
    password_without_digits = faker.password(length=12, digits=False)
    password_without_special_and_digits = faker.password(
        length=12, special_chars=False, digits=False
    )

    invalid_passwords = [
        password_without_special,
        password_without_digits,
        password_without_special_and_digits,
    ]

    for p in invalid_passwords:
        with pytest.raises(InvalidPasswordError):
            CleanPassword(p)
