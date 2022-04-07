


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance=0, int_rate=0.02):
        self.balance = balance
        self.int_rate = int_rate

    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        print(f"New Balance = {self.balance}")
        return self

    def withdraw(self, amount):
        if (self.balance>amount): #States that if balance is less than amount then deduct $5 and print insufficient funds
            self.balance-=amount
        else:
            self.balance-=5
            print(f"Insufficient funds: Charging a $5 fee")
        print(f"New Balance = {self.balance}")
        return self

    def display_account_info(self):
        print(f"balance:{self.balance}")
        return self
    def yield_interest(self):
        if(self.balance>0):
            self.balance+=(self.int_rate*self.balance) #yield_interest= total balance*int_rate* (amt of time money has been in acct i.e year(s))        
            print(f"N/A") #not really necessary
        print(self)
        return self

saqqara=BankAccount(200, 0.01)
saqqara.deposit(2000).deposit(1000).deposit(5000).withdraw(200).yield_interest() #no commas

bob=BankAccount(100)
bob.deposit(1).deposit(1000).withdraw(5).withdraw(100).withdraw(100).withdraw(10)















