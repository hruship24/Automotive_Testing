from Training.EligibilityCheck import EligibilityCheck
from Project_Exception.VoterEligibilityException import VoterEligibilityException
import logging

ec = EligibilityCheck('Hrushi', 12)
#It will create a logfile and write that logging msg there in that file
logging.basicConfig(level=logging.DEBUG, format='%(process)d / %(message)s', filename='logfile.log')
try:
    ec.voting_eligible()
except VoterEligibilityException as vee:
    logging.error('{} is not eligible to vote. '.format(ec.name))
    print(vee)
