import pytest
@pytest.fixture
def setup_teardown():
    num1 = 10
    num2 = 20
    print('This is setup')
    yield num1, num2
    print('This is teardown')


@pytest.fixture
def setup_teardown_listmanip():
    print('this is setup')
    yield
    print('this is teardown')