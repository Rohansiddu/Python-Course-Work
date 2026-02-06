from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    
    def check_balance(self):
        print("you can check the balance")
    def view_statement(self):
        print("you can view the statement")
    def set_pin(self):
        print("you can change the pin")

class SavingsAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: You can withdraw as many times upto 50k")
    def deposit(self):
        print("[Depost]: you can deposti 50k")
class CurrentAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: You can withdraw as many times upto 52k")
    def deposit(self):
        print("[Depost]: you can deposti 52k")
class SalaryAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: max 1L")
    def deposit(self):
        print("[Depost]: once in a month and 21")
class JointAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: You can withdraw upto 40k from both parties")
    def deposit(self):
        print("[Depost]: you can deposti 40k")
class FixedDepositAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: You can withdraw once")
    def deposit(self):
        print("[Depost]: you can deposti only once")
class ZeroBalanceAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]: You can withdraw once")
    def deposit(self):
        print("[Depost]: you can deposti only once")


dhanush=SavingsAccount()
print('Dhanush - Savings Account')
dhanush.withdraw()
dhanush.deposit()
dhanush.check_balance()
dhanush.set_pin()
dhanush.view_statement()

abhi=CurrentAccount()
print('abhi - Current Account')
abhi.withdraw()
abhi.deposit()
abhi.check_balance()
abhi.set_pin()
abhi.view_statement()

subhash=JointAccount()
print('subhash - Joint Account')
subhash.withdraw()
subhash.deposit()
subhash.check_balance()
subhash.set_pin()
subhash.view_statement()

kamal=SalaryAccount()
print('kamal - Salary Account')
kamal.withdraw()
kamal.deposit()
kamal.check_balance()
kamal.set_pin()
kamal.view_statement()

surya=FixedDepositAccount()
print('surya - Fixed Deposit Account')
surya.withdraw()
surya.deposit()
surya.check_balance()
surya.set_pin()
surya.view_statement()

kowshik=ZeroBalanceAccount()
print('Kowshik - Fixed Deposit Account')
kowshik.withdraw()
kowshik.deposit()
kowshik.check_balance()
kowshik.set_pin()
kowshik.view_statement()