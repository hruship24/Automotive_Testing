import pytest


@pytest.fixture
def setup_teardown():
    num1 = 12
    num2 = 10
    print('This is setup')
    yield num1, num2
    print('this is teardown')
