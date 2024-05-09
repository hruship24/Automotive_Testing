import pytest

from app.calculator import add, sub, intdiv, floatdiv


@pytest.mark.parametrize("num1, num2",
                         [
                             (10, 0),
                             (20, 0)
                         ])
def test_intdiv_invaliddata(num1, num2):
    # to check for exception
    with pytest.raises(ZeroDivisionError):
        intdiv(num1, num2)
    # No need to write assert statement when dealing with exception
    # assert intdiv(num1, num2) == , 'Failed for valid data'


'''
This fixture code is written in conftest.py . Even though it will
run properly without throwing any error
@pytest.fixture
def setup_teardown():
    num1 = 10
    num2 = 20
    print('This is setup')
    yield num1, num2
    print('This is teardown')
'''

# Instead of writing two functions for setup and teardown, use yield to combine them
# @pytest.fixture
# def teardown():
#     print('This is teardown')


def test_add_two_pos_nums(setup_teardown):
    # arrange
    num1 = 10
    num2 = 20
    # act
    res = add(num1, num2)
    # assert
    assert res == 30, 'Adding 2 Positive throws Error'


# Getting values from setup_teardown function
def test_add_two_neg_nums(setup_teardown):
    num1, num2 = setup_teardown
    res = add(-num1, -num2)
    assert res == -30, 'Adding 2 Negative throws Error'


def test_add_one_pos_one_neg_nums():
    res = add(10, -20)
    assert res == -10, 'Adding 1 Positive and 1 negative throws Error'


def test_add_one_neg_one_pos_nums():
    res = add(-10, 20)
    assert res == 10, 'Adding 1 negative and 1 Positive throws Error'
  
    
def test_sub_two_pos_nums():
    res = sub(10, 20)
    assert res == -10, 'Subtract 2 Positive throws Error'


def test_sub_two_neg_nums():
    res = sub(-10, -20)
    assert res == 10, 'Subtract 2 Negative throws Error'


def test_sub_one_pos_one_neg_nums():
    res = sub(10, -20)
    assert res == 30, 'Subtract 1 Positive and 1 negative throws Error'


def test_sub_one_neg_one_pos_nums():
    res = sub(-10, 20)
    assert res == -30, 'Subtract 1 negative and 1 Positive throws Error'
