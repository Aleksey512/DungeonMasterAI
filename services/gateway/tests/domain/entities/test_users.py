import pytest
from faker import Faker
from gateway.domain.entities.users import User
from gateway.domain.exceptions.users import InvalidEmailError, InvalidPasswordError
from gateway.domain.values.users import CleanPassword, Email


def test_user_create_success(faker: Faker):
    email = faker.email()
    password = faker.password(length=12)

    user = User.create(email=Email(email), password=CleanPassword(password))

    assert user
    assert user.email.as_generic_type() == email
    assert User.hash_password(password) == user.hashed_password.as_generic_type()
    assert len(user.pull_events()) == 1


def test_create_user_invalid_email(faker: Faker):
    email = "invalid@email"
    password = faker.password(length=12)

    with pytest.raises(InvalidEmailError):
        User.create(email=Email(email), password=CleanPassword(password))


def test_create_user_invalid_password(faker: Faker):
    email = faker.email()
    password = faker.password(length=12, special_chars=False, digits=False)

    with pytest.raises(InvalidPasswordError):
        User.create(email=Email(email), password=CleanPassword(password))


def test_check_user_password_func(faker: Faker):
    email = faker.email()
    password = faker.password()
    invalid_password = faker.password(special_chars=False, digits=False)

    user = User.create(email=Email(email), password=CleanPassword(password))

    assert user.check_password(password)
    assert not user.check_password(invalid_password)


def test_set_user_password_func(faker: Faker):
    email = faker.email()
    password = faker.password()

    user = User.create(email=Email(email), password=CleanPassword(password))

    assert user.check_password(password)

    new_password = faker.password()

    user.set_password(CleanPassword(new_password))

    assert user.hash_password(new_password) == user.hashed_password
    assert user.hash_password(password) != user.hashed_password
    assert user.check_password(new_password)
    assert not user.check_password(password)
