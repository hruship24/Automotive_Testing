import pytest

from calc import add


@pytest.mark.parametrize("num1, num2, expected_result",
                         [
                             (10, 5, 15),
                             (1, 1, 3)  # this is for fail in cmd terminal pytest --maxfaill=1
                                        # it will run till one test case fails
                         ])
def test_add(num1, num2, expected_result):
    actual_result = add(num1, num2)
    assert actual_result == expected_result, 'Error while doing add'


@pytest.mark.smoke
def test_add_two_positive(setup_teardown):
    num1, num2 = setup_teardown
    actual_result = add(num1, num2)
    assert actual_result == 22, 'Failed : Adding two positive number'


@pytest.mark.important # important is defined in pytest.ini that we created
def test_add_two_negative(setup_teardown):
    num1, num2 = setup_teardown
    actual_result = add(-num1, -num2)
    assert actual_result == -22, 'Failed : Adding two negative number'


@pytest.mark.skipif(condition=True, reason='Skipping test')
def test_add_one_positive_one_negative(setup_teardown):
    num1, num2 = setup_teardown
    actual_result = add(num1, -num2)
    assert actual_result == 2, 'Failed : Adding two negative number'


@pytest.mark.xfail(reason='It is expected to fail')
def test_expected_to_fail():
    assert 5 != 5

'''
to generate a xml file which contain detailed report 
on cmd write pytest --junitxml=filename.xml
             pytest --html=filename.html
'''