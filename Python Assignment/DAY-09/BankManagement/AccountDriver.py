import logging
from BankAccount import BankAccount
from TransactionError import TransactionError

# Configure logging
logging.basicConfig(filename='transaction_errors.log', level=logging.ERROR)

# Demonstration
account = BankAccount("Hrushi", "123456", 1000)
try:
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # This should raise TransactionError which will be recorded in log file
except TransactionError as e:
    logging.error(e)

# Display account information
account.display_info()
