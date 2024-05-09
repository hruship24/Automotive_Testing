import pytest


@pytest.fixture
def setup_teardown_addition():
    num1 = 10
    num2 = 20
    print('This is setup part')
    yield num1, num2
    print('This is teardown part')

