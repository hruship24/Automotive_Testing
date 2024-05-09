import pytest


@pytest.fixture
def valid_credentials():
    return "hrushi", "12345"


@pytest.fixture
def invalid_username_valid_password():
    return "wrong_username", "12345"


@pytest.fixture
def valid_username_invalid_password():
    return "hrushi","wrong_password"


@pytest.fixture
def invalid_username_invalid_password():
    return "wrong_username","wrong_password"


@pytest.fixture
def empty_credentials():
    return "", ""
