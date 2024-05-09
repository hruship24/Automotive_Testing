from Project_Exception.VoterEligibilityException import VoterEligibilityException


class EligibilityCheck:
    def __init__(self,name, age):
        self.age = age
        self.name = name

    def voting_eligible(self):
        if self.age < 18:
            raise VoterEligibilityException('You are not eligible to vote friend')
        else:
            print('Congrats !!! You are eligible to Vote ')
