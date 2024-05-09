from app.addition import add


def test_add_two_pos_nums(setup_teardown_addition):
    num1, num2 = setup_teardown_addition
    # act
    actual_result = add(num1, num2)
    expected_result = 30
    # assert
    assert actual_result == expected_result, 'During adding 2 Positive throws Error'


# Getting values from setup_teardown function
def test_add_two_neg_nums(setup_teardown_addition):
    num1, num2 = setup_teardown_addition
    actual_result = add(-num1, -num2)
    expected_result = -30
    assert actual_result == expected_result, 'During adding 2 Negative throws Error'


def test_add_one_pos_one_neg_nums(setup_teardown_addition):
    num1, num2 = setup_teardown_addition
    actual_result = add(num1, -num2)
    expected_result = -10
    assert actual_result == expected_result, 'During adding 1 Positive and 1 negative throws Error'


def test_add_one_neg_one_pos_nums(setup_teardown_addition):
    num1, num2 = setup_teardown_addition
    actual_result = add(-num1, num2)
    expected_result = 10
    assert actual_result == expected_result, 'During adding 1 negative and 1 Positive throws Error'


def test_add_zero():
    num1, num2 = 0, 0
    actual_result = add(num1, num2)
    expected_result = 0
    assert actual_result == expected_result, 'During addition of zeroes got error'
