import pytest

from app.division import intdiv


@pytest.mark.parametrize("num1, num2",
                         [
                             (10, 0),
                             (20, 0)
                         ])
def test_intdiv_invaliddata(num1, num2):
    # to check for exception
    with pytest.raises(ZeroDivisionError):
        intdiv(num1, num2)
