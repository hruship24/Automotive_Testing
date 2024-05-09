def add(num1, num2):
    return num1 + num2

def test_add():
    sum1 = add(5,9)
    assert sum1 == 15, 'add fn returned wrong value'
# assert actual_value = expected_value 'message'
