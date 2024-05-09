import pytest

from app.user_authentication import authenticate_user


def test_correct_credentials(valid_credentials):
    username, password = valid_credentials
    actual_result = authenticate_user(username, password)
    assert actual_result == True


def test_incorrect_username(invalid_username_valid_password):
    username, password = invalid_username_valid_password
    actual_result = authenticate_user(username, password)
    assert actual_result == False


def test_incorrect_password(valid_username_invalid_password):
    username, password = valid_username_invalid_password
    actual_result = authenticate_user(username, password)
    assert actual_result == False


def test_incorrect_both(invalid_username_invalid_password):
    username, password = invalid_username_invalid_password
    actual_result = authenticate_user(username, password)
    assert actual_result == False


def test_empty_credentials(empty_credentials):
    username, password = empty_credentials
    actual_result = authenticate_user(username, password)
    assert actual_result == False
