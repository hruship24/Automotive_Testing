class Emp:
    # def __init__(self):
    #     self.username = ''
    #     self.password = ''

    def logincheck(self, username, password):
        if username.lower() == 'admin' and password.lower() == 'password':
            return True
        else:
            return False