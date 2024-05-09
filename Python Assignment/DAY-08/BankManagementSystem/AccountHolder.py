class AccountHolder:
    def __init__(self, accHoldName):
        self._accHoldName = accHoldName

    def get_accHoldName(self):
        return self._accHoldName

    def set_accHoldName(self,name):
        self._accHoldName = name
