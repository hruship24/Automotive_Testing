from app.factorial import facto


def test_facto_pos_num():
    assert facto(5) == 120, 'Factorial of 5 is wrong'
    # assert facto(0) == 1, 'For factorial of 0 is wrong'
    # assert facto(-70) == 1, 'For factorial of -70 is wrong'
    # If we write like this and if one assert fails, other wont get executed also


def test_facto_zero():
    assert facto(0) == 1, 'Factorial of zero is wrong'


def test_facto_five(setup_teardown):
    num1, num2 = setup_teardown
    assert facto(num1) == 3628800, 'Factorial of 10 is wrong'


def test_facto_neg_num():
    assert facto(-23) == 1, 'Factorial of Negative number is wrong'
