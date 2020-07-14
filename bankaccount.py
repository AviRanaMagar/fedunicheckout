import os
class BankAccount():

  def __init__(self):
    self.account_number = 0
    self.pin_number = ''
    self.balance = 0.0
    self.interest_rate = 0.0
    self.transaction_list = []
  '''Constructor to set account_number to '0', pin_number to an empty string,
    balance to 0.0, interest_rate to 0.0 and transaction_list to an empty list.'''

  def deposit_funds(self, amount, account_number):
    self.account_number = account_number
    file = './' + str(self.account_number) + '.txt'
    try:
      with open(file) as tran:
        line = tran.readlines()
        line[5] = str(amount) + '\n'
        current_balance = float(line[2])
        current_balance += amount
        self.balance = current_balance
        line[2] = str(current_balance) + '\n'

      with open(file, 'w') as trans:
        trans.writelines(line)
    except:
      pass
    '''Function to deposit an amount to the account balance. Raises an
           exception if it receives a value that cannot be cast to float.'''

  def withdraw_funds(self,amnt,account_number):
    self.account_number = account_number
    file = './' + str(self.account_number) + '.txt'
    try:
      with open(file) as tran:
        line = tran.readlines()
        current_balance = float(line[2])

      if current_balance-amnt<0:
        messagebox.showwarning("ERROR","Insufficient Funds !!")
        return False
      
      current_balance -= amnt
      self.balance = current_balance
      line[2]=str(current_balance) + '\n'
      line[9]=str(amnt)+ '\n'
      with open(file, 'w') as trans:
        trans.writelines(line)
    except:
      pass
    '''Function to withdraw an amount from the account balance. Raises an
    exception if it receives a value that cannot be cast to float. Raises
    an exception if the amount to withdraw is greater than the available
    funds in the account.'''
        
        
  def get_transaction_string(self):
    '''Function to create and return a string of the transaction list. Each transaction
           consists of two lines - either the word "Deposit" or "Withdrawal" on
           the first line, and then the amount deposited or withdrawn on the next line.'''


  def save_to_file(self):
    '''Function to overwrite the account text file with the current account
           details. Account number, pin number, balance and interest (in that
           precise order) are the first four lines - there are then two lines
           per transaction as outlined in the above 'get_transaction_string'
           function.'''
