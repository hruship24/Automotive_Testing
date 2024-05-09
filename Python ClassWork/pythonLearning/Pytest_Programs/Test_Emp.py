import pytest

from app.login import Emp


class Test_Emp:
    @pytest.mark.parametrize("user, pwd",
                             [
                                 ('admin', 'password')
                             ])
    def test_logincheck(self, user, pwd):
        emp = Emp()
        assert emp.logincheck(user, pwd) == True, 'Logincheck not working'

    @pytest.mark.parametrize("user, pwd, actual_result",
                             [
                                 ('admin', 'wrong_password', False),
                                 ('wrong_username', 'password', False),
                                 ('wrong_username', 'wrong_password', False)
                             ])
    def test_logincheck_invaliddata(self, user, pwd, actual_result):
        emp = Emp()
        assert  emp.logincheck(user, pwd) == actual_result, 'logincheck for invalid data not working'

    @pytest.mark.parametrize("user, pwd",
                             [
                                 (' ', ' ')
                             ])
    def test_logincheck_nulldata(self, user, pwd):
        emp = Emp()
        assert emp.logincheck(user, pwd) == False, 'logincheck for null data not working'
